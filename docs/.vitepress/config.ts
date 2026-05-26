import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'AI-Wiki',
  description: 'AI开发者全景式工具与资源导航',
  base: '/ai-wiki/',

  head: [['link', { rel: 'icon', href: '/datawhale-logo.png' }]],

  themeConfig: {
    logo: '/datawhale-logo.png',

    nav: [
      { text: '首页', link: '/' },
      { text: 'GitHub', link: 'https://github.com/datawhalechina/ai-wiki' },
    ],

    sidebar: [
      {
        text: '总览',
        items: [{ text: '目录与学习路径', link: '/' }],
      },
      {
        text: '模型与数据层',
        items: [
          { text: '三方模型（API）', link: '/chapter03/03-model-api' },
          { text: 'Embedding 模型', link: '/chapter11/11-embedding-models' },
          { text: '向量知识库', link: '/chapter10/10-vector-databases' },
        ],
      },
      {
        text: '框架与协议层',
        items: [
          { text: 'Agent 框架', link: '/chapter08/08-agent-frameworks' },
          { text: 'RAG 框架', link: '/chapter09/09-rag-frameworks' },
          { text: 'MCP', link: '/chapter06/06-mcp' },
        ],
      },
      {
        text: '工具与平台层',
        items: [
          { text: 'CLI 种类', link: '/chapter04/04-cli-tools' },
          { text: '编程工具 IDE', link: '/chapter07/07-ide-tools' },
          { text: '好用的 Skill', link: '/chapter05/05-skills' },
          { text: '龙虾 Claw 产品系列', link: '/chapter01/01-openclaw-ecosystem' },
          { text: 'Coding Plan', link: '/chapter02/02-coding-plan' },
        ],
      },
      {
        text: '范式与方法论层',
        items: [
          { text: 'Vibe Coding 四种', link: '/chapter12/12-vibe-coding' },
          { text: 'Prompt Engineering', link: '/chapter14/14-prompt-engineering' },
        ],
      },
      {
        text: '资源与实战',
        items: [
          { text: '资源导航', link: '/chapter13/13-resources' },
          { text: '端到端实战项目', link: '/chapter15/15-hands-on-projects' },
        ],
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/datawhalechina/ai-wiki' },
    ],

    search: {
      provider: 'local',
    },

    footer: {
      message: '基于 CC BY-NC-SA 4.0 发布',
    },

    editLink: {
      pattern: 'https://github.com/datawhalechina/ai-wiki/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页',
    },

    lastUpdated: {
      text: '最后更新',
    },
  },
})
