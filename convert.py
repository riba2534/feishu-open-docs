#!/usr/bin/env python3
"""将飞书自定义 HTML 组件转换为标准 Markdown。

处理 crawl.py 下载的 .md 文件中的 :::html 块和自定义 <md-*> 标签。
"""

import re
import sys
import urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

OUTPUT_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# 1. Helper: extract clean text from a BeautifulSoup element
# ---------------------------------------------------------------------------

def extract_text(el) -> str:
    """Extract text from an element, preserving markdown formatting inside."""
    if el is None:
        return ""
    if isinstance(el, NavigableString):
        return str(el)

    parts = []
    for child in el.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif isinstance(child, Tag):
            tag = child.name
            if tag == "md-text":
                # <md-text type="field-name">name</md-text> → `name`
                ft = child.get("type", "")
                inner = child.get_text()
                if ft in ("field-name", "field-type"):
                    parts.append(f"`{inner}`")
                else:
                    parts.append(inner)
            elif tag == "md-tag":
                parts.append(f"`{child.get_text()}`")
            elif tag == "md-perm":
                # <md-perm name="x" desc="d">text</md-perm> → `name` text
                name = child.get("name", "")
                text = child.get_text().strip()
                if name:
                    parts.append(f"`{name}` {text}")
                else:
                    parts.append(text)
            elif tag == "md-tooltip":
                parts.append(child.get_text())
            elif tag == "md-app-support":
                types = child.get("types", "")
                parts.append(types)
            elif tag == "md-enum":
                parts.append(convert_enum(child))
            elif tag == "md-enum-item":
                key = child.get("key", "")
                text = child.get_text().strip()
                parts.append(f"- `{key}`: {text}")
            elif tag == "md-alert":
                parts.append(convert_alert_tag(child))
            elif tag in ("md-code-json",):
                code = child.get_text()
                parts.append(f"\n```json\n{code.strip()}\n```\n")
            elif tag == "md-event-list":
                parts.append(child.get_text())
            elif tag == "md-scope-list":
                parts.append(child.get_text())
            elif tag == "md-server-api-list":
                parts.append(child.get_text())
            elif tag in ("div", "span", "p", "br"):
                parts.append(extract_text(child))
            else:
                # Fallback: just get text
                parts.append(extract_text(child))
    return "".join(parts)


# ---------------------------------------------------------------------------
# 2. Convert <md-enum> to markdown list
# ---------------------------------------------------------------------------

def convert_enum(el) -> str:
    items = el.find_all("md-enum-item")
    lines = []
    for item in items:
        key = item.get("key", "")
        text = item.get_text().strip()
        lines.append(f"- `{key}`: {text}")
    return "\n" + "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# 3. Convert <md-alert> to blockquote
# ---------------------------------------------------------------------------

ALERT_TYPE_MAP = {
    "tip": "Tip",
    "warn": "Warning",
    "warning": "Warning",
    "error": "Error",
    "info": "Info",
    "note": "Note",
}


def convert_alert_tag(el) -> str:
    alert_type = el.get("type", "info")
    label = ALERT_TYPE_MAP.get(alert_type, alert_type.capitalize())
    content = extract_text(el).strip()
    if not content:
        return ""
    lines = content.split("\n")
    quoted = "\n".join(f"> {line}" for line in lines)
    return f"\n> **{label}**: {lines[0]}\n" + ("\n".join(f"> {l}" for l in lines[1:]) + "\n" if len(lines) > 1 else "")


# ---------------------------------------------------------------------------
# 4. Convert <md-table> (key-value / simple table)
# ---------------------------------------------------------------------------

def convert_md_table(el) -> str:
    """Convert <md-table> to markdown table or key-value list."""
    thead = el.find("md-thead")
    tbody = el.find("md-tbody")

    # Extract header
    headers = []
    if thead:
        for tr in thead.find_all(["md-tr", "tr"]):
            for th in tr.find_all("md-th"):
                headers.append(extract_text(th).strip())

    # Extract rows
    rows = []
    if tbody:
        for tr in tbody.find_all("md-tr"):
            cells = []
            for cell in tr.find_all(["md-td", "md-th"]):
                cell_text = extract_text(cell).strip()
                # Collapse multi-line to single line for table cells
                cell_text = re.sub(r'\n+', ' ', cell_text)
                cells.append(cell_text)
            if cells:
                rows.append(cells)

    if not rows:
        return ""

    # Check if it's a 2-column key-value table (like the "基本" info table)
    if len(headers) == 2 and headers[0] in ("基本", ""):
        # Render as key-value pairs
        lines = []
        for row in rows:
            if len(row) >= 2:
                lines.append(f"| {row[0]} | {row[1]} |")
            elif len(row) == 1:
                lines.append(f"| {row[0]} | |")
        return "\n| 项目 | 值 |\n| --- | --- |\n" + "\n".join(lines) + "\n"

    # General table
    if not headers:
        # Infer headers from first row
        if rows:
            ncols = max(len(r) for r in rows)
            headers = [f"列{i+1}" for i in range(ncols)]

    ncols = len(headers)
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * ncols) + " |")
    for row in rows:
        # Pad row to match header count
        while len(row) < ncols:
            row.append("")
        lines.append("| " + " | ".join(row[:ncols]) + " |")

    return "\n" + "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# 5. Convert <md-dt-table> (data type table with nesting)
# ---------------------------------------------------------------------------

def convert_md_dt_table(el) -> str:
    """Convert <md-dt-table> to markdown table with indentation for nesting."""
    thead = el.find("md-dt-thead")
    tbody = el.find("md-dt-tbody")

    # Extract headers
    headers = []
    if thead:
        for tr in thead.find_all("md-dt-tr"):
            for th in tr.find_all("md-dt-th"):
                text = extract_text(th).strip()
                headers.append(text)

    if not headers:
        headers = ["名称", "类型", "描述"]

    # Extract rows
    rows = []
    if tbody:
        for tr in tbody.find_all("md-dt-tr"):
            level = int(tr.get("level", "0"))
            cells = []
            for td in tr.find_all("md-dt-td"):
                cell_text = extract_text(td).strip()
                cells.append(cell_text)
            if cells:
                rows.append({"level": level, "cells": cells})

    if not rows:
        return ""

    ncols = len(headers)
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * ncols) + " |")

    for row in rows:
        cells = row["cells"]
        level = row["level"]

        # Pad cells
        while len(cells) < ncols:
            cells.append("")

        # Add indentation to first cell (field name) based on level
        indent = "&nbsp;&nbsp;" * level
        if level > 0:
            cells[0] = indent + "└ " + cells[0]

        # Collapse multi-line in description cell (last cell) to preserve table format
        # But keep it readable - use <br> for line breaks
        for i in range(len(cells)):
            cells[i] = re.sub(r'\n{2,}', '<br>', cells[i])
            cells[i] = re.sub(r'\n', ' ', cells[i])

        lines.append("| " + " | ".join(cells[:ncols]) + " |")

    return "\n" + "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# 6. Convert <md-code-json> and <md-code-tab-*>
# ---------------------------------------------------------------------------

def convert_code_json(el) -> str:
    code = el.get_text()
    return f"\n```json\n{code.strip()}\n```\n"


def convert_code_tabs(el) -> str:
    """Convert <md-code-tab-group> to labeled code blocks."""
    panels = el.find_all("md-code-tab-panel")
    parts = []
    for panel in panels:
        label = panel.get("label", "")
        lang = panel.get("language", panel.get("lang", ""))
        if not lang and label:
            lang_map = {"Go": "go", "Java": "java", "Python": "python",
                        "Node.js": "javascript", "JavaScript": "javascript",
                        "cURL": "bash", "C#": "csharp", "PHP": "php"}
            lang = lang_map.get(label, label.lower())
        code = panel.get_text().strip()
        if label:
            parts.append(f"\n**{label}**\n\n```{lang}\n{code}\n```\n")
        else:
            parts.append(f"\n```{lang}\n{code}\n```\n")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# 7. Process a single :::html ... ::: block
# ---------------------------------------------------------------------------

def process_html_block(html_content: str) -> str:
    """Convert a single HTML block content to markdown."""
    soup = BeautifulSoup(html_content, "html.parser")

    parts = []
    for el in soup.children:
        if isinstance(el, NavigableString):
            text = str(el).strip()
            if text:
                parts.append(text)
            continue
        if not isinstance(el, Tag):
            continue

        tag = el.name
        if tag == "md-table":
            parts.append(convert_md_table(el))
        elif tag == "md-dt-table":
            parts.append(convert_md_dt_table(el))
        elif tag == "md-alert":
            parts.append(convert_alert_tag(el))
        elif tag == "md-code-json":
            parts.append(convert_code_json(el))
        elif tag in ("md-code-tab-group", "md-code-tabs"):
            parts.append(convert_code_tabs(el))
        elif tag == "md-code-tab-panel":
            # Standalone panel (not in group)
            lang = el.get("language", el.get("lang", ""))
            label = el.get("label", "")
            code = el.get_text().strip()
            if label:
                parts.append(f"\n**{label}**\n\n```{lang}\n{code}\n```\n")
            else:
                parts.append(f"\n```{lang}\n{code}\n```\n")
        elif tag == "md-enum":
            parts.append(convert_enum(el))
        elif tag == "md-perm":
            name = el.get("name", "")
            text = el.get_text().strip()
            parts.append(f"`{name}` {text}" if name else text)
        elif tag == "md-tag":
            parts.append(f"`{el.get_text()}`")
        elif tag == "md-event-list":
            parts.append(extract_text(el))
        elif tag == "md-scope-list":
            parts.append(extract_text(el))
        elif tag == "md-server-api-list":
            parts.append(extract_text(el))
        else:
            parts.append(extract_text(el))

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# 8. Process a full markdown file
# ---------------------------------------------------------------------------

# Match many broken/relative URL forms emitted by upstream:
#   /ssl:ttdoc/...                (canonical internal ref)
#   /ssl:ttdoc%2F...              (URL-encoded variant)
#   /ssl:/ttdoc/...               (extra slash typo)
#   /ssl：ttdoc/...               (Chinese full-width colon typo)
#   /ssl:ttdc/...                 (typo: ttdoc → ttdc)
#   /ssl:ttdocopen-apis/...       (typo: missing slash)
#   /:ssltoken/...                (alternate marker)
#   /document-mod/index?fullPath=... (portal redirect)
#   /uAjLw4CM/...                 (bare doc-tree path)
#   //sf3-cn.feishucdn.com/...    (protocol-relative CDN)
SSL_PREFIX_RE = re.compile(
    r'^[a-z]?/?ssl[:：]/{0,2}'           # ssl: with 0-2 leading slashes
    r'(?:ttdo?cs?[:：]?)?'                # optional ttdoc/ttdc/ttdocs marker
    r'(?:%2F|%2f|/|(?=open|uAjLw|ukTM|home|server-docs|reference))'
)
DOC_MOD_RE    = re.compile(r'^/document-mod/index\?fullPath=(.*)$')
SSLTOKEN_RE   = re.compile(r'^/:ssltoken/(.*)$')
BARE_DOC_RE   = re.compile(r'^/(uAjLw4CM|ukTMukTMukTM)/')
DOCUMENT_RE   = re.compile(r'^/document/')

LARK_DOC_BASE = 'https://open.larkoffice.com/document/'


def normalize_link_url(url: str) -> str:
    """Convert non-standard internal/relative URLs to canonical https URLs."""
    raw = url
    url = url.strip()
    # Protocol-relative (//host/path) → https://host/path
    if url.startswith('//'):
        return 'https:' + url
    # /document-mod/index?fullPath=XXX → decoded path under /document/
    m = DOC_MOD_RE.match(url)
    if m:
        path = urllib.parse.unquote(m.group(1)).lstrip('/')
        return LARK_DOC_BASE + path
    # /:ssltoken/home/... → /document/home/...
    m = SSLTOKEN_RE.match(url)
    if m:
        return LARK_DOC_BASE + m.group(1).strip()
    # /ssl:ttdoc/... and all its typo variants
    m = SSL_PREFIX_RE.match(url)
    if m:
        path = url[m.end():]
        path = urllib.parse.unquote(path.replace('%2F', '/').replace('%2f', '/')).lstrip('/')
        return LARK_DOC_BASE + path
    # Bare /uAjLw4CM/... → /document/uAjLw4CM/...
    if BARE_DOC_RE.match(url):
        return LARK_DOC_BASE.rstrip('/') + url
    # Already a document path but missing host: /document/... → https://open.larkoffice.com/document/...
    if DOCUMENT_RE.match(url):
        return 'https://open.larkoffice.com' + url
    # No known pattern matched — return stripped form (drops stray surrounding spaces)
    return url


# Markdown link/image: capture optional `!`, [text], (url possibly with surrounding spaces).
# Permits whitespace between `]` and `(` (some upstream payloads emit `[t] (url)`).
LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\s*\(\s*([^)\s][^)]*?)\s*\)')


def normalize_links(content: str) -> str:
    """Rewrite all markdown link/image URLs through normalize_link_url."""
    def repl(m):
        bang, text, url = m.group(1), m.group(2), m.group(3)
        new_url = normalize_link_url(url)
        return f"{bang}[{text}]({new_url})"
    content = LINK_RE.sub(repl, content)

    # Also fix raw HTML href="/internal/path" inside SDK code comments etc.
    # Only rewrites URLs that match a known Feishu internal pattern — leaves
    # other site-relative anchors (e.g. <a href="/login">) untouched.
    def fix_href(m):
        quote, url = m.group(1), m.group(2)
        new_url = normalize_link_url(url)
        if new_url == url:
            return m.group(0)
        return f'href={quote}{new_url}{quote}'
    content = re.sub(r'href=(["\'])([^"\']+)\1', fix_href, content)
    return content


def process_file(content: str) -> str:
    """Process a full markdown file, converting all custom components."""

    # 1. Remove Feishu doc-portal action buttons: {尝试一下}(url=...), {使用示例}(url=...), etc.
    content = re.sub(r'\{[^}\n]+\}\(url=[^)]*\)', '', content)

    # 2. Process :::html ... ::: blocks
    def replace_html_block(match):
        html = match.group(1)
        return process_html_block(html)

    content = re.sub(r':::html\s*\n(.*?):::', replace_html_block, content, flags=re.DOTALL)

    # 2b. Remove any unmatched/dangling :::html or ::: markers that survived
    # (some upstream payloads omit the closing :::, leaving the opener orphaned)
    content = re.sub(r'^:::html\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^:::\s*$', '', content, flags=re.MULTILINE)

    # 2c. Convert orphan callout openers (:::note / :::warning / :::tip / :::error)
    # to a one-line blockquote label. Upstream omits the closing :::, so we cannot
    # wrap the whole block — but the label keeps the semantic hint.
    callout_labels = {'note': 'Note', 'tip': 'Tip', 'warning': 'Warning',
                      'warn': 'Warning', 'error': 'Error', 'info': 'Info',
                      'caution': 'Caution', 'danger': 'Danger'}
    def replace_callout_opener(m):
        kind = m.group(1).lower()
        label = callout_labels.get(kind, kind.capitalize())
        return f'> **{label}**'
    content = re.sub(r'^:::\s*([a-zA-Z]+)\s*$', replace_callout_opener,
                     content, flags=re.MULTILINE)

    # 3. Handle any remaining inline <md-*> tags outside :::html blocks
    # <md-tag>
    content = re.sub(r'<md-tag[^>]*>(.*?)</md-tag>', r'`\1`', content)
    # <md-text>
    content = re.sub(r'<md-text[^>]*>(.*?)</md-text>', r'`\1`', content)
    # <md-perm name="x">text</md-perm>
    def replace_perm(m):
        name = re.search(r'name="([^"]*)"', m.group(0))
        text = m.group(1).strip()
        if name:
            return f"`{name.group(1)}` {text}"
        return text
    content = re.sub(r'<md-perm[^>]*>(.*?)</md-perm>', replace_perm, content)
    # <md-tooltip>
    content = re.sub(r'<md-tooltip[^>]*>(.*?)</md-tooltip>', r'\1', content)
    # <md-app-support>
    content = re.sub(r'<md-app-support[^>]*></md-app-support>', '', content)
    # <md-alert> (inline, not in :::html block)
    def replace_inline_alert(m):
        atype = re.search(r'type="([^"]*)"', m.group(0))
        label = ALERT_TYPE_MAP.get(atype.group(1), "Note") if atype else "Note"
        inner = m.group(1).strip()
        if not inner:
            return ""
        return f"\n> **{label}**: {inner}\n"
    content = re.sub(r'<md-alert[^>]*>(.*?)</md-alert>', replace_inline_alert, content, flags=re.DOTALL)
    # <md-enum-item>
    def replace_enum_item(m):
        key = re.search(r'key="([^"]*)"', m.group(0))
        text = m.group(1).strip()
        if key:
            return f"- `{key.group(1)}`: {text}"
        return f"- {text}"
    content = re.sub(r'<md-enum-item[^>]*>(.*?)</md-enum-item>', replace_enum_item, content, flags=re.DOTALL)
    # <md-enum> wrapper
    content = re.sub(r'</?md-enum>', '', content)

    # Remove any remaining self-closing or empty md-* tags
    content = re.sub(r'<md-[a-z_-]+[^>]*/>', '', content)
    content = re.sub(r'</?md-[a-z_-]+[^>]*>', '', content)

    # 4. Fix non-standard / broken links → https://open.larkoffice.com/...
    content = normalize_links(content)

    # 5. Clean up excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    return content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    md_files = sorted(OUTPUT_DIR.rglob("*.md"))
    md_files = [f for f in md_files if f.name not in ("README.md", "CLAUDE.md")]

    total = len(md_files)
    print(f"Processing {total} files...")

    processed = 0
    errors = []

    for i, fpath in enumerate(md_files):
        try:
            content = fpath.read_text(encoding="utf-8")
            new_content = process_file(content)
            if new_content != content:
                fpath.write_text(new_content, encoding="utf-8")
            processed += 1

        except Exception as e:
            errors.append((str(fpath.relative_to(OUTPUT_DIR)), str(e)))
            processed += 1

        if (i + 1) % 200 == 0 or i + 1 == total:
            print(f"  Progress: {i+1}/{total}")

    print(f"\nDone: {processed} processed, {len(errors)} errors")
    if errors:
        print("\nErrors:")
        for path, err in errors[:20]:
            print(f"  {path}: {err}")


if __name__ == "__main__":
    main()
