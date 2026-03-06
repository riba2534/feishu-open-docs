#!/usr/bin/env python3
"""飞书开放平台 Server API 文档全量爬取脚本"""

import asyncio
import json
import os
import re
import sys
import time
import urllib.parse
from pathlib import Path

import aiohttp

BASE_URL = "https://open.larkoffice.com"
DIRECTORY_API = f"{BASE_URL}/api/tools/docment/directory_list"
CONTENT_API = f"{BASE_URL}/document_portal/v1/document/get_detail"
SERVER_API_ID = "103"
OUTPUT_DIR = Path("/home/hepengcheng/airepo/feishu-open-docs")
CONCURRENCY = 8
RETRY_COUNT = 3
BATCH_DELAY = 0.3  # seconds between batches

# fullPath -> local relative path mapping
path_mapping: dict[str, str] = {}
# All doc entries
all_docs: list[dict] = []
# Failed downloads
failed_docs: list[dict] = []


def fetch_directory_tree() -> dict:
    """Phase 1: Fetch complete directory tree synchronously."""
    import urllib.request
    req = urllib.request.Request(DIRECTORY_API)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    if data.get("code") != 0:
        raise RuntimeError(f"Directory API error: {data}")
    return data["data"]


def find_server_api_node(tree: dict) -> dict:
    """Find the Server API node (id=103) in the tree."""
    for item in tree.get("items", []):
        if str(item.get("id")) == SERVER_API_ID:
            return item
    raise RuntimeError("Server API node not found")


def slugify(name: str) -> str:
    """Convert a name to a filesystem-safe slug."""
    # Keep alphanumeric, Chinese chars, hyphens, underscores
    s = name.strip()
    # Replace spaces and special chars with hyphens
    s = re.sub(r'[/\\:*?"<>|]+', '-', s)
    s = re.sub(r'\s+', '-', s)
    s = s.strip('-')
    return s if s else 'unnamed'


def extract_docs(node: dict, parent_local_path: str = "", depth: int = 0):
    """Recursively extract all documents and build path mapping."""
    node_type = node.get("type", "")
    full_path = node.get("fullPath", "")
    name = node.get("name", "unnamed")
    children = node.get("items", [])

    if node_type == "DocumentType":
        # Leaf document - use last segment of fullPath as filename
        last_segment = full_path.rstrip("/").split("/")[-1] if full_path else slugify(name)
        local_path = f"{parent_local_path}/{last_segment}.md" if parent_local_path else f"{last_segment}.md"
        local_path = local_path.lstrip("/")
        path_mapping[full_path] = local_path
        all_docs.append({
            "fullPath": full_path,
            "name": name,
            "localPath": local_path,
            "updateTime": node.get("updateTime", ""),
        })
    elif node_type == "DirectoryType":
        # Directory node
        last_segment = full_path.rstrip("/").split("/")[-1] if full_path else slugify(name)
        if depth == 0:
            # Top-level: use the last segment directly
            local_path = last_segment
        else:
            local_path = f"{parent_local_path}/{last_segment}" if parent_local_path else last_segment
        local_path = local_path.lstrip("/")
        path_mapping[full_path] = local_path

        for child in children:
            extract_docs(child, local_path, depth + 1)


def deduplicate_paths():
    """Resolve local path collisions by appending disambiguating segments from fullPath."""
    from collections import Counter
    counter = Counter(d["localPath"] for d in all_docs)
    dupes = {k for k, v in counter.items() if v > 1}
    if not dupes:
        return

    for doc in all_docs:
        if doc["localPath"] in dupes:
            # Use second-to-last segment of fullPath to disambiguate
            parts = doc["fullPath"].rstrip("/").split("/")
            if len(parts) >= 2:
                disambig = parts[-2]
            else:
                disambig = slugify(doc["name"])
            base = doc["localPath"]
            # Insert disambiguator before .md extension
            new_path = base[:-3] + f"-{disambig}.md"
            doc["localPath"] = new_path
            path_mapping[doc["fullPath"]] = new_path

    # Verify no remaining collisions
    counter2 = Counter(d["localPath"] for d in all_docs)
    remaining = {k: v for k, v in counter2.items() if v > 1}
    if remaining:
        # Further disambiguate with index
        for path, count in remaining.items():
            matches = [d for d in all_docs if d["localPath"] == path]
            for i, doc in enumerate(matches[1:], 1):
                new_path = doc["localPath"][:-3] + f"-{i}.md"
                doc["localPath"] = new_path
                path_mapping[doc["fullPath"]] = new_path

    print(f"Resolved {len(dupes)} path collisions")


def create_directory_structure():
    """Phase 2: Create local directory structure."""
    dirs_created = set()
    for doc in all_docs:
        local_path = OUTPUT_DIR / doc["localPath"]
        parent = local_path.parent
        if parent not in dirs_created:
            parent.mkdir(parents=True, exist_ok=True)
            dirs_created.add(parent)
    print(f"Created {len(dirs_created)} directories")


def post_process_content(content: str, doc_info: dict) -> str:
    """Phase 4: Post-process markdown content."""
    # Add frontmatter
    frontmatter = f"""---
title: "{doc_info['name'].replace('"', '\\"')}"
fullPath: "{doc_info['fullPath']}"
updateTime: "{doc_info.get('updateTime', '')}"
---

"""
    # Fix image URLs: //sf3-cn.feishucdn.com/... -> https://sf3-cn.feishucdn.com/...
    content = re.sub(r'(!\[[^\]]*\]\()//([^)]+\))', r'\1https://\2', content)
    content = re.sub(r'(src=")//([^"]+)', r'\1https://\2', content)

    # Convert internal links: /ssl:ttdoc/... or relative paths
    def replace_internal_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        # Check if it maps to a local file
        if link_path in path_mapping:
            # Calculate relative path from current doc
            current_dir = str(Path(doc_info["localPath"]).parent)
            target = path_mapping[link_path]
            try:
                rel = os.path.relpath(target, current_dir)
            except ValueError:
                rel = target
            return f"[{link_text}]({rel})"
        return match.group(0)

    content = re.sub(r'\[([^\]]*)\]\((/[^)]+)\)', replace_internal_link, content)

    return frontmatter + content


async def download_doc(session: aiohttp.ClientSession, semaphore: asyncio.Semaphore, doc: dict) -> bool:
    """Download a single document."""
    async with semaphore:
        url = f"{CONTENT_API}?fullPath={urllib.parse.quote(doc['fullPath'], safe='/')}"
        headers = {"Accept-Language": "zh-CN,zh;q=0.9"}

        for attempt in range(RETRY_COUNT):
            try:
                async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                    if resp.status != 200:
                        if attempt < RETRY_COUNT - 1:
                            await asyncio.sleep(1 * (attempt + 1))
                            continue
                        failed_docs.append({**doc, "error": f"HTTP {resp.status}"})
                        return False

                    data = await resp.json()
                    if data.get("code") != 0:
                        if attempt < RETRY_COUNT - 1:
                            await asyncio.sleep(1 * (attempt + 1))
                            continue
                        failed_docs.append({**doc, "error": f"API code {data.get('code')}"})
                        return False

                    content = data.get("data", {}).get("content", "")
                    if not content:
                        # Some pages may have no content, record but don't retry
                        content = f"# {doc['name']}\n\n> 此页面无内容。\n"

                    # Update doc info with server data
                    server_data = data.get("data", {})
                    if server_data.get("updateTime"):
                        doc["updateTime"] = server_data["updateTime"]

                    processed = post_process_content(content, doc)
                    output_path = OUTPUT_DIR / doc["localPath"]
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_text(processed, encoding="utf-8")
                    return True

            except (aiohttp.ClientError, asyncio.TimeoutError, json.JSONDecodeError) as e:
                if attempt < RETRY_COUNT - 1:
                    await asyncio.sleep(1 * (attempt + 1))
                    continue
                failed_docs.append({**doc, "error": str(e)})
                return False

    return False


async def download_all_docs():
    """Phase 3: Download all documents concurrently."""
    semaphore = asyncio.Semaphore(CONCURRENCY)
    connector = aiohttp.TCPConnector(limit=CONCURRENCY * 2, ttl_dns_cache=300)

    async with aiohttp.ClientSession(connector=connector) as session:
        total = len(all_docs)
        completed = 0
        success = 0
        batch_size = 50

        for i in range(0, total, batch_size):
            batch = all_docs[i:i + batch_size]
            tasks = [download_doc(session, semaphore, doc) for doc in batch]
            results = await asyncio.gather(*tasks)
            batch_success = sum(1 for r in results if r)
            success += batch_success
            completed += len(batch)
            print(f"  Progress: {completed}/{total} ({success} ok, {completed - success} failed)")

            if i + batch_size < total:
                await asyncio.sleep(BATCH_DELAY)

    print(f"\nDownload complete: {success}/{total} succeeded, {len(failed_docs)} failed")


def generate_index(server_api_node: dict):
    """Phase 5: Generate README.md index file."""
    lines = [
        "# 飞书开放平台 Server API 文档",
        "",
        f"> 自动爬取于 {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 文档总数: {len(all_docs)} | 目录数: {len([p for p in path_mapping.values() if not p.endswith('.md')])}",
        "",
        "## 目录",
        "",
    ]

    def gen_toc(node: dict, indent: int = 0):
        node_type = node.get("type", "")
        full_path = node.get("fullPath", "")
        name = node.get("name", "")
        children = node.get("items", [])
        prefix = "  " * indent

        if node_type == "DocumentType":
            local = path_mapping.get(full_path, "")
            if local:
                lines.append(f"{prefix}- [{name}]({local})")
            else:
                lines.append(f"{prefix}- {name}")
        elif node_type == "DirectoryType":
            lines.append(f"{prefix}- **{name}**")
            for child in children:
                gen_toc(child, indent + 1)

    for child in server_api_node.get("items", []):
        gen_toc(child, 0)

    # Add failed docs section if any
    if failed_docs:
        lines.extend([
            "",
            "## 下载失败的文档",
            "",
        ])
        for doc in failed_docs:
            lines.append(f"- `{doc['fullPath']}` — {doc.get('error', 'unknown')}")

    readme_path = OUTPUT_DIR / "README.md"
    readme_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {readme_path}")


def verify():
    """Phase 6: Verify results."""
    md_files = list(OUTPUT_DIR.rglob("*.md"))
    # Exclude README.md from count
    doc_files = [f for f in md_files if f.name != "README.md"]
    empty_files = [f for f in doc_files if f.stat().st_size < 50]

    print(f"\n=== Verification ===")
    print(f"Expected documents: {len(all_docs)}")
    print(f"Actual .md files: {len(doc_files)}")
    print(f"Empty/tiny files: {len(empty_files)}")
    print(f"Failed downloads: {len(failed_docs)}")

    if empty_files:
        print(f"\nEmpty files (first 10):")
        for f in empty_files[:10]:
            print(f"  {f.relative_to(OUTPUT_DIR)}")

    # Save failed docs list for retry
    if failed_docs:
        failed_path = OUTPUT_DIR / "failed_docs.json"
        with open(failed_path, "w") as f:
            json.dump(failed_docs, f, ensure_ascii=False, indent=2)
        print(f"\nFailed docs saved to {failed_path}")


def main():
    print("Phase 1: Fetching directory tree...")
    tree = fetch_directory_tree()
    server_api = find_server_api_node(tree)
    print(f"Found Server API node: {server_api['name']} (id={server_api['id']})")

    print("\nPhase 1b: Extracting document paths...")
    # Process top-level items of server API
    for child in server_api.get("items", []):
        extract_docs(child, "", depth=0)
    print(f"Found {len(all_docs)} documents, {len(path_mapping)} total paths")

    print("\nPhase 1c: Deduplicating paths...")
    deduplicate_paths()

    print("\nPhase 2: Creating directory structure...")
    create_directory_structure()

    print("\nPhase 3: Downloading all documents...")
    asyncio.run(download_all_docs())

    print("\nPhase 5: Generating index...")
    generate_index(server_api)

    print("\nPhase 6: Verification...")
    verify()

    print("\nDone!")


if __name__ == "__main__":
    main()
