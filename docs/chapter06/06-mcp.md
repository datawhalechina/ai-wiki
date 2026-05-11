# 六、MCP

[← 上一章：五、好用的 Skill](../chapter05/05-skills.md) | [返回总览](../index.md) | [下一章：七、编程工具 IDE →](../chapter07/07-ide-tools.md)

MCP（模型上下文协议）是 Anthropic 提出的开放协议，为 LLM 应用与外部数据源、工具之间提供标准化集成方式，被形象地称为"AI 应用的 USB-C 接口"。

MCP 协议已支持 **Streamable HTTP** 传输方式（替代早期的 stdio/SSE），提升了远程 MCP Server 的稳定性和可扩展性。

## 热门 MCP 服务器

扩展的 MCP 生态（收录标准：GitHub 活跃度 + 实用性）：

| MCP Server | 功能领域 |
|-----------|---------|
| **[GitHub](https://github.com/github/github-mcp-server)**（30K star） | Issues、PRs、仓库管理，GitHub 官方维护 |
| **[Playwright](https://github.com/microsoft/playwright-mcp)**（32K star） | 微软官方，AI 精确控制网页、自动化测试与抓取 |
| **[Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp)**（39K star） | Chrome 开发者工具集成，调试、性能分析 |
| **[Context7](https://github.com/upstash/context7)**（55K star） | 实时获取最新库文档和代码示例，编码必备 |
| **[Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** | 网页抓取、内容提取为 Markdown |
| **[Jina AI](https://github.com/jina-ai/mcp)** | 语义搜索、图像搜索、跨模态搜索 |
| **[Notion](https://github.com/makenotion/notion-mcp-server)** | Notion 页面创建、编辑、搜索 |
| **[飞书 Lark](https://github.com/larksuite/lark-openapi-mcp)** | 飞书消息、日历、文档、通讯录 |
| **[Figma](https://github.com/GLips/Figma-Context-MCP)** | 向 Agent 提供 Figma 布局和设计信息 |
| **[Serena](https://github.com/oraios/serena)**（24K star） | 语义级代码检索与编辑，给 Agent 装上 IDE 级理解力 |
| **[FastMCP](https://github.com/PrefectHQ/fastmcp)**（25K star） | 极速构建 MCP Server 的 Python 框架 |
| **[n8n](https://github.com/n8n-io/n8n)**（187K star） | 工作流自动化平台，400+ 集成，原生 MCP 支持 |

> 更多 MCP Server 参见 [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)（87K star），收录了社区贡献的大量 MCP 服务器。

## MCP Server 场景分类

按使用场景快速定位：

| 场景 | 推荐 MCP Server |
|------|----------------|
| **代码托管** | GitHub MCP |
| **Web 自动化** | Playwright、Chrome DevTools |
| **实时文档查询** | Context7 |
| **网页抓取** | Firecrawl、Jina AI |
| **知识管理** | Notion、飞书 Lark |
| **设计协作** | Figma |
| **代码理解** | Serena |
| **工作流自动化** | n8n |
| **自建 MCP Server** | FastMCP |

## MCP 选型建议

- **编码场景必备** → **Context7**（实时文档）+ **GitHub MCP**（仓库操作）+ **Playwright**（端到端测试）
- **设计师协作** → **Figma MCP**：AI 可直接读取设计稿的布局和样式信息
- **团队协作** → **Notion MCP** / **飞书 Lark MCP**：知识库和 IM 打通
- **自建 MCP Server** → **FastMCP**：Python 一行装饰器就能把函数变成 MCP 工具

## 支持 MCP 的客户端

| MCP Client                                                                    | 简介                    |
| ----------------------------------------------------------------------------- | --------------------- |
| **[Claude Desktop](https://claude.ai/)**                                      | Anthropic 官方桌面客户端     |
| **[Claude Code](https://code.claude.com/docs/zh-CN/overview)** | Anthropic 终端级 AI 编程助手 |
| **[Cursor](https://www.cursor.com/)**                                         | AI 原生 IDE（基于 VSCode）  |
| **[Windsurf](https://www.windsurf.com/)**                                     | Codeium 出品 AI IDE     |
| **[Trae](https://www.trae.cn/)**                                              | 字节 出品 AI IDE          |
| **[Cherry Studio](https://www.cherry-ai.com/)**                               | 支持多模型并行对话的跨平台AI桌面客户端  |

## 相关文章

- **MCP 官方规范**：[modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP 协议详解**：[腾讯云开发者社区](https://developer.cloud.tencent.com/article/2508227)
- **[MCP Server 市场（mcp.so）](https://mcp.so/zh)**
