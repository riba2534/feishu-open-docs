<div align="center">

<img src="public/logo.png" alt="飞书开放平台 Server API 文档" width="120" height="120" />

# 飞书开放平台 Server API 中文文档镜像

[![Deploy](https://github.com/riba2534/feishu-open-docs/actions/workflows/deploy.yml/badge.svg)](https://github.com/riba2534/feishu-open-docs/actions/workflows/deploy.yml)
[![Site](https://img.shields.io/badge/site-feishu.fate.red-2c84e8)](https://feishu.fate.red)
[![Docs](https://img.shields.io/badge/docs-2,173_篇-00d6b9)](https://feishu.fate.red)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#许可)

把飞书开放平台 (`open.larkoffice.com`) 的 Server API 全量文档自动镜像为标准 Markdown，并以一个干净、可搜索的中文文档站点对外提供。

🌐 **在线访问**：[https://feishu.fate.red](https://feishu.fate.red)

</div>

---

## 这个仓库做什么

飞书官方文档站使用前端动态渲染，内容里嵌入了大量私有自定义组件（`<md-table>`、`<md-alert>`、`<md-dt-table>`、`:::html` 块等），不便于离线阅读、AI 检索或工具集成。本仓库通过两步流水线把官方文档转成纯净 Markdown 镜像：

1. **`crawl.py`** — 调用飞书公开 API 抓取目录树和每篇文档，按目录结构落到本地。
2. **`convert.py`** — 把飞书自定义 HTML 组件转换成标准 Markdown 表格 / 引用块 / 代码块；规范化所有内部链接为标准 HTTPS URL。

输出可以：

- 在 GitHub 直接浏览源码（带 frontmatter 的 clean Markdown）
- 通过 [VitePress 站点](https://feishu.fate.red) 检索阅读
- 灌进 RAG / Agent / IDE 插件做上下文检索

## 主要特性

- 全量爬取 **2,173 篇** Server API 文档（48 个一级分类）
- 标准 Markdown 输出，每篇带 YAML frontmatter（`title` / `fullPath` / `updateTime`）
- 飞书自定义组件全部规范化（`<md-*>` / `:::html` / `:::note` / `{尝试一下}` 等）
- 链接规范化：`/ssl:ttdoc/...` 等 470+ 处内部路径全部修复为 `https://open.larkoffice.com/...`
- VitePress 文档站点：6 组中文导航、自动 sidebar、本地全文搜索、深色模式
- GitHub Actions 自动部署：push `main` 触发 build + deploy
- 自定义域名 + Let's Encrypt HTTPS

## 仓库结构

```
feishu-open-docs/
├── README.md                   # 本文件（项目说明）
├── INDEX.md                    # 自动生成的全量文档树索引（由 crawl.py 产出）
├── crawl.py                    # 抓取脚本（飞书公开 API）
├── convert.py                  # 标准化脚本（HTML 组件 → Markdown）
├── index.md                    # VitePress 首页（48 个分类卡片）
├── package.json                # VitePress 依赖与脚本
├── public/                     # 站点静态资产（logo / favicon / CNAME）
├── .vitepress/
│   ├── config.mts              # 站点配置（nav / search / 主题）
│   └── sidebar.ts              # 自动生成 path-based sidebar
├── .github/workflows/
│   └── deploy.yml              # GitHub Actions 自动部署到 GitHub Pages
├── contact-v3/                 # 通讯录
├── im-v1/  im-v2/              # 即时消息
├── approval-v4/                # 审批
├── corehr-v1/                  # 飞书人事
├── calendar-v4/  vc-v1/        # 日历 / 视频会议
├── uUDN04SN0QjL1QDN/           # 云文档（docs / sheets / wiki）
└── ...                         # 共 48 个一级分类目录
```

## 使用方式

### 直接浏览文档

打开 [feishu.fate.red](https://feishu.fate.red)，按分类导航或顶部搜索框查关键词。

### 离线浏览源 Markdown

```bash
git clone https://github.com/riba2534/feishu-open-docs.git
cd feishu-open-docs
```

每个文档都带 frontmatter：

```yaml
---
title: "创建用户"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/create"
updateTime: "1748337476000"
---
```

### 重新爬取最新文档

```bash
pip3 install aiohttp beautifulsoup4   # 仅首次

python3 crawl.py     # 爬取（约 2-3 分钟，并发 8）
python3 convert.py   # 标准化（约 1 分钟）
```

下载失败的 URL 会被记录到 `failed_docs.json`。如遇限流（HTTP 429），把 `crawl.py` 顶部的 `CONCURRENCY` 调到 3-5。

### 本地预览站点

```bash
npm install            # 或 pnpm install
npm run docs:dev       # 本地 dev server  http://localhost:5173
npm run docs:build     # 生产构建（约 2 分钟）
npm run docs:preview   # 预览构建产物
```

## 数据来源

- 官方文档站：<https://open.larkoffice.com/document>
- 爬取 API（公开，无需认证）：
  - `GET /api/tools/docment/directory_list` — 获取整棵目录树
  - `GET /document_portal/v1/document/get_detail?fullPath=<path>` — 获取单篇文档

## 部署

每次 `push main` 时，GitHub Actions 会自动构建 VitePress 站点并发布到 GitHub Pages，绑定自定义域名 `feishu.fate.red`。HTTPS 证书由 GitHub Pages 自动签发（Let's Encrypt）。

## 免责声明

- 本仓库仅作为**学习与查阅用途**的镜像，文档版权归飞书所有
- 内容自动从官方爬取，可能存在与官方版本的延迟
- 如发现内容错误或链接异常，欢迎提 [Issue](https://github.com/riba2534/feishu-open-docs/issues) 或 PR

## 许可

文档内容版权归飞书所有；本仓库的爬取脚本（`crawl.py` / `convert.py`）与站点配置以 **MIT** 许可发布。

---

<div align="center">

如果这个仓库对你有帮助，欢迎点一个 ⭐ Star 支持。

</div>
