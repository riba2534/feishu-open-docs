import { defineConfig } from 'vitepress'
import { generateSidebar, firstDocLinks, TOP_DIR_LABELS } from './sidebar'

const sidebar = generateSidebar()
const firstDocs = firstDocLinks()

// 顶部 nav：把 48 个一级目录按主题分组（中文有意义的标签）
const NAV_GROUPS: Array<{ text: string; dirs: string[] }> = [
  {
    text: '协作通讯',
    dirs: [
      'contact-v3', 'im-v1', 'im-v2', 'group', 'cardkit-v1', 'bot-v3',
      'application-v6', 'authentication-management',
      'human_authentication-v1', 'verification-v1',
    ],
  },
  {
    text: '办公协作',
    dirs: [
      'calendar-v4', 'vc-v1', 'minutes-v1', 'mail-v1', 'moments-v1',
      'uUDN04SN0QjL1QDN', 'spark-v1', 'lingo-v1', 'search-v2', 'helpdesk-v1',
    ],
  },
  {
    text: '人事招聘',
    dirs: [
      'corehr-v1', 'ehr-v1', 'hire-v1', 'attendance-v1', 'payroll-v1',
      'performance-v1', 'okr-v1', 'report-v1', 'elearning-v2', 'acs-v1',
    ],
  },
  {
    text: '业务流程',
    dirs: ['approval-v4', 'task-v2', 'mdm-v1', 'apaas-v1', 'security_and_compliance-v1'],
  },
  {
    text: '平台管理',
    dirs: [
      'ai', 'aily-v1', 'workplace-v1', 'personal_settings-v1',
      'admin-v1', 'tenant-v2', 'tenant-tag', 'directory-v1', 'trust_party-v1',
    ],
  },
  {
    text: '开发指南',
    dirs: ['api-call-guide', 'event-subscription-guide', 'server-side-sdk', 'historic-version'],
  },
]

const navDropdowns = NAV_GROUPS.map((g) => ({
  text: g.text,
  items: g.dirs.map((d) => ({
    text: TOP_DIR_LABELS[d] ?? d,
    link: firstDocs[d] ?? `/${d}/`,
  })),
}))

export default defineConfig({
  title: '飞书开放平台 Server API 文档',
  description: '飞书开放平台 Server API 中文文档镜像（自动同步）',
  lang: 'zh-CN',
  base: '/',
  cleanUrls: true,
  ignoreDeadLinks: true,
  lastUpdated: true,
  srcExclude: ['README.md', 'CLAUDE.md'],

  head: [
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
  ],

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      ...navDropdowns,
    ],

    sidebar,

    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索文档', buttonAriaLabel: '搜索文档' },
          modal: {
            displayDetails: '显示详情',
            resetButtonTitle: '重置搜索',
            backButtonTitle: '关闭搜索',
            noResultsText: '未找到相关结果',
            footer: {
              selectText: '选择',
              selectKeyAriaLabel: '回车',
              navigateText: '切换',
              navigateUpKeyAriaLabel: '向上',
              navigateDownKeyAriaLabel: '向下',
              closeText: '关闭',
              closeKeyAriaLabel: 'Esc',
            },
          },
        },
      },
    },

    outline: {
      level: [2, 3],
      label: '本页目录',
    },

    editLink: {
      pattern: 'https://github.com/riba2534/feishu-open-docs/edit/main/:path',
      text: '在 GitHub 上编辑此页',
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/riba2534/feishu-open-docs' },
    ],

    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdatedText: '最后更新',
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '导航菜单',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',

    footer: {
      message: '内容来源：<a href="https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/server-api">飞书开放平台</a> · 自动爬取整理',
      copyright: '本镜像仅供学习与查阅，文档版权归飞书所有',
    },
  },

  markdown: {
    lineNumbers: false,
    config(md) {
      // 飞书原始内容里偶有未闭合或非白名单的 raw HTML，会让 Vue SFC 解析失败。
      // 实践中表格 cell 内的 <br> 是几乎唯一不能放弃的 inline HTML（飞书用它做软换行），
      // 其余 raw HTML 全部 escape 为字面文本，避免未闭合标签问题。
      const ALLOW = new Set(['br'])
      const escapeAttrs = (s: string) =>
        s.replace(/[&<>]/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[ch] as string)
      const filterRaw = (raw: string) =>
        raw.replace(/<\/?([a-zA-Z][a-zA-Z0-9]*)[^>]*\/?>/g, (m, tag) =>
          ALLOW.has(tag.toLowerCase()) ? m : escapeAttrs(m)
        )
      md.renderer.rules.html_inline = (tokens, idx) => filterRaw(tokens[idx].content)
      md.renderer.rules.html_block = (tokens, idx) => filterRaw(tokens[idx].content)
    },
  },
})
