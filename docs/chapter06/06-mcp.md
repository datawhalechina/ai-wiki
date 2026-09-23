# 六、MCP

[← 上一章：五、好用的 Skill](../chapter05/05-skills.md) | [返回总览](../index.md) | [下一章：七、编程工具 IDE →](../chapter07/07-ide-tools.md)

MCP（模型上下文协议）是 Anthropic 提出的开放协议，为 LLM 应用与外部数据源、工具之间提供标准化集成方式，被形象地称为"AI 应用的 USB-C 接口"。

## 协议演进：从 Streamable HTTP 到无状态化

MCP 的传输与状态模型经历了两轮重要变化，选型和排错前建议先理解这条线索：

| 阶段 | 传输方式 | 状态模型 |
|------|---------|---------|
| 早期 | stdio（本地）/ HTTP+SSE（远程） | Server 维护会话状态 |
| 2025 年 | **Streamable HTTP** 取代 HTTP+SSE，统一本地与远程接入 | 仍依赖会话 |
| **2026-07-28 规范** | Streamable HTTP 继续演进 | **协议核心转为无状态** |

**2026-07-28 规范**是 MCP 发布以来最大的一次修订，核心是**去状态化**：

- **移除握手与会话**：删除 `initialize` / `initialized` 握手（SEP-2575）与 `Mcp-Session-Id` 会话标识（SEP-2567）。Server 不再需要维护连接级状态，可直接水平扩展、按请求无服务化部署
- **请求头路由**：新增 `Mcp-Method` / `Mcp-Name` 请求头，网关与负载均衡器无需解析 body 即可按方法、工具名精确路由
- **能力发现与缓存**：新增 `server/discover` 方法；列表类结果变为可缓存，减少重复往返
- **多轮请求**：新增 Multi Round-Trip Requests（SEP-2322），支持在单次交互中多次往返确认
- **Extensions 框架**：引入可选的扩展机制（首批为 Tasks / MCP Apps / EMA）
- **安全与治理**：OAuth 2.1 加固；确立正式弃用政策，被弃用能力保留 **12 个月**过渡窗口

**同时被弃用的能力**：`Roots`、`Sampling`、`Logging` 三个早期能力，以及旧的 **HTTP+SSE 传输方式**。

> **迁移提示**：旧版实现仍可运行（弃用窗口内），但新项目建议直接按 2026-07-28 规范实现；若你的 Server 依赖会话状态，需改为把状态放入显式参数或外部存储。

## 热门 MCP 服务器

扩展的 MCP 生态（收录标准：GitHub 活跃度 + 实用性）：

| MCP Server | 功能领域 |
|-----------|---------|
| **[GitHub](https://github.com/github/github-mcp-server)**（33.1K star） | Issues、PRs、仓库管理，GitHub 官方维护 |
| **[Playwright](https://github.com/microsoft/playwright-mcp)**（37.5K star） | 微软官方，AI 精确控制网页、自动化测试与抓取 |
| **[Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp)**（52.5K star） | Chrome 开发者工具集成，调试、性能分析 |
| **[Context7](https://github.com/upstash/context7)**（62.4K star） | 实时获取最新库文档和代码示例，编码必备 |
| **[Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** | 网页抓取、内容提取为 Markdown |
| **[Jina AI](https://github.com/jina-ai/mcp)** | 语义搜索、图像搜索、跨模态搜索 |
| **[Notion](https://github.com/makenotion/notion-mcp-server)** | Notion 页面创建、编辑、搜索 |
| **[飞书 Lark](https://github.com/larksuite/lark-openapi-mcp)** | 飞书消息、日历、文档、通讯录 |
| **[Figma](https://github.com/GLips/Figma-Context-MCP)** | 向 Agent 提供 Figma 布局和设计信息 |
| **[Serena](https://github.com/oraios/serena)**（29.7K star） | 语义级代码检索与编辑，给 Agent 装上 IDE 级理解力 |
| **[FastMCP](https://github.com/PrefectHQ/fastmcp)**（27.9K star） | 极速构建 MCP Server 的 Python 框架 |
| **[n8n](https://github.com/n8n-io/n8n)**（205.8K star） | 工作流自动化平台，400+ 集成，原生 MCP 支持 |

> 更多 MCP Server 参见 [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)（95.5K star），收录了社区贡献的大量 MCP 服务器。

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
| **[Devin Desktop](https://devin.ai/desktop)**（原 Windsurf）                   | Cognition 出品 AI IDE（2026-06 更名） |
| **[TraeCode](https://www.trae.cn/)**                                          | 字节 出品 AI IDE（2026 由 TRAE IDE 更名） |
| **[Cherry Studio](https://www.cherry-ai.com/)**                               | 支持多模型并行对话的跨平台AI桌面客户端  |

## 5 分钟快速上手：用 FastMCP 创建你的第一个 MCP Server

```bash
# 1. 安装
pip install fastmcp

# 2. 创建 server.py
cat > server.py << 'EOF'
from fastmcp import FastMCP

mcp = FastMCP("my-first-server")

@mcp.tool()
def hello(name: str) -> str:
    """向用户打招呼"""
    return f"你好，{name}！这是你的第一个 MCP 工具。"

if __name__ == "__main__":
    mcp.run()
EOF

# 3. 运行
fastmcp run server.py
```

在 Claude Code 中配置：在**项目根目录创建 `.mcp.json`**（项目级配置，可提交到 Git 与团队共享）：

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

> 也可以用 CLI 一键添加：`claude mcp add my-server -- python server.py`（默认写入用户级 `~/.claude.json`，加 `-s project` 则写入 `.mcp.json`）。
>
> ⚠️ 注意：MCP 配置**不在** `.claude/settings.json` 中——该文件用于 env / hooks / permissions，不含 `mcpServers` 键。

重启 Claude Code 后，输入"用 hello 工具打个招呼"即可测试。

## 相关文章

- **MCP 官方规范**：[modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP 协议详解**：[腾讯云开发者社区](https://developer.cloud.tencent.com/article/2508227)
- **[MCP Server 市场（mcp.so）](https://mcp.so/zh)**
