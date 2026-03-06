# 飞书开放平台 Server API 文档仓库

## 仓库概述

本仓库存储飞书开放平台 **Server API** 的全量文档（标准 Markdown 格式），通过 `crawl.py` + `convert.py` 两步流程从飞书文档站自动爬取并转换。

- 文档来源：`https://open.larkoffice.com` Server API 分类（节点 ID: `103`）
- 当前规模：约 2065 个文档，48 个一级分类，52MB
- 文件格式：标准 Markdown + YAML frontmatter（title / fullPath / updateTime）

## 数据源 API

两个无需认证的公开 API：

| API | 用途 |
|-----|------|
| `GET https://open.larkoffice.com/api/tools/docment/directory_list` | 获取完整目录树（递归 JSON） |
| `GET https://open.larkoffice.com/document_portal/v1/document/get_detail?fullPath=<path>` | 获取单个文档的 Markdown 内容 |

关键行为：
- 默认返回中文版（由 `Accept-Language: zh-CN` 控制）
- `data.content` 字段返回的是混合了飞书自定义 HTML 组件的 Markdown（非标准格式），需要 `convert.py` 二次转换
- 目录树中 `type=DocumentType` 为文档页面，`type=DirectoryType` 为目录节点
- Server API 在目录树顶层 `items` 中，`id=103`，`fullPath=/uAjLw4CM/ukTMukTMukTM`

## 更新文档

### 全量更新（两步）

```bash
# 1. 安装依赖（仅首次）
pip3 install aiohttp beautifulsoup4

# 2. 爬取原始文档（约 2-3 分钟）
python3 crawl.py

# 3. 转换为标准 Markdown（约 1 分钟）
python3 convert.py

# 4. 检查结果
# crawl.py 输出验证信息：文件数、失败数、空文件数
# convert.py 输出处理数和错误数
# 失败的文档会记录在 failed_docs.json

# 5. 提交推送
git add -A
git commit -m "docs: update all server API docs"
git push
```

### crawl.py — 爬取原始文档

```
Phase 1  — fetch_directory_tree()       从 API 获取完整目录树
Phase 1b — extract_docs()               递归提取 Server API 下所有文档的 fullPath
Phase 1c — deduplicate_paths()          解决本地路径冲突（约 83 个同名文件）
Phase 2  — create_directory_structure() 创建本地目录
Phase 3  — download_all_docs()          并发下载（8 并发，50 个一批，批间 0.3s）
Phase 4  — post_process_content()       添加 frontmatter、修复图片 URL、转换内部链接
Phase 5  — generate_index()             生成 README.md 索引
Phase 6  — verify()                     校验文件数量和完整性
```

### convert.py — 转换飞书自定义组件为标准 Markdown

API 返回的内容包含大量飞书自定义 HTML 组件（`<md-*>` 标签），不是标准 Markdown。`convert.py` 使用 BeautifulSoup 解析并转换：

| 原始格式 | 转换结果 |
|---------|---------|
| `:::html <md-table>...</md-table> :::` | 标准 Markdown 表格 |
| `:::html <md-dt-table>...</md-dt-table> :::` | 带 `└` 缩进的 Markdown 表格（表示嵌套字段） |
| `<md-alert type="tip/warn/error">` | `> **Tip/Warning/Error**: ...` blockquote |
| `<md-code-json>` | ` ```json ``` ` 代码块 |
| `<md-code-tab-group>` | 按语言标签分隔的多个代码块 |
| `<md-tag>` / `<md-text>` | `` `inline code` `` |
| `<md-perm name="x">text` | `` `x` text `` |
| `<md-enum>` / `<md-enum-item>` | Markdown 列表 |
| `<md-tooltip>` / `<md-app-support>` | 提取纯文本或移除 |
| `{尝试一下}(url=...)` | 移除 |
| `/ssl:ttdoc/...` 链接 | `https://open.larkoffice.com/document/...` |

`convert.py` 可独立重复运行，只处理包含自定义标签的文件，跳过已转换的文件。

### 关键参数

在 `crawl.py` 顶部可调整：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `CONCURRENCY` | `8` | 并发下载数 |
| `RETRY_COUNT` | `3` | 单个文档失败重试次数 |
| `BATCH_DELAY` | `0.3` | 批次间延迟（秒），防限流 |
| `SERVER_API_ID` | `"103"` | 目录树中 Server API 节点的 ID |
| `OUTPUT_DIR` | 脚本所在目录 | 输出目录路径 |

## 目录结构

```
feishu-open-docs/
├── CLAUDE.md                  # 本文件
├── README.md                  # 自动生成的索引（含完整目录树链接）
├── crawl.py                   # 爬取脚本（Phase 1-6）
├── convert.py                 # 格式转换脚本（飞书 HTML → 标准 Markdown）
├── api-call-guide/            # API 调用指南
├── contact-v3/                # 通讯录
├── im-v1/                     # 消息
├── group/                     # 群组
├── approval-v4/               # 审批
├── ...                        # 共 48 个一级分类
└── failed_docs.json           # 下载失败记录（仅失败时生成）
```

每个 .md 文件的 frontmatter 示例：

```yaml
---
title: "创建用户"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/create"
updateTime: "1745206930000"
---
```

## 注意事项

- `OUTPUT_DIR` 硬编码为绝对路径，在其他机器运行需修改
- 图片未下载到本地，仍引用飞书 CDN（`sf3-cn.feishucdn.com`）
- 如遇 API 限流（HTTP 429），可降低 `CONCURRENCY` 至 3-5
- `convert.py` 依赖 `beautifulsoup4`，`crawl.py` 依赖 `aiohttp`
