# AI实践大百科：AI 开发者的随身工具清单

> ⭐ 如果觉得有用，欢迎 Star！[→ GitHub 仓库](https://github.com/2951121599/ai-practice-wiki)

## 目录

[TOC]



## 一、龙虾 Claw 产品系列

"龙虾"是对开源 AI 智能体 **[OpenClaw](https://openclaw.ai/)**（原名 Clawdbot/Moltbot）的昵称，因其红色机械龙虾图标而得名。它能理解自然语言指令，自主调用电脑工具完成任务，真正实现从"意图"到"执行"的闭环。

### OpenClaw 核心能力

- 对接 ChatGPT、Claude、Gemini、DeepSeek、Kimi 等主流模型，也支持 Ollama 本地模型
- 直接读写文件、运行代码、模拟键鼠、操控浏览器
- 通过微信、飞书、QQ 等 IM 工具用自然语言发号施令

**提示**：持续关注"龙虾"生态的 Skills 市场和安全机制演进，尤其是端云协同方案的发展。

### 国内"龙虾"产品矩阵


| 产品                                                         | 厂商     | 部署方式         | 特点                                                      |
| ------------------------------------------------------------ | -------- | ---------------- | --------------------------------------------------------- |
| **[OpenClaw](https://openclaw.ai/)**                         | 开源社区 | 本地/云端        | 开源框架，对接多模型，"海纳百川"                          |
| **[AutoClaw](https://autoglm.z.ai/autoclaw/)**               | 智谱 AI  | 本地（一键安装） | 预置 50+ Skills，内置专属模型 Pony-Alpha-2，支持飞书等 IM |
| **[KimiClaw](https://kimi-claw.com/)**                       | 月之暗面 | 云端             | 主要调用 Kimi 自有模型                                    |
| **[MaxClaw](https://agent.minimaxi.com/activity/max-claw)**  | MiniMax  | 云端             | 主要调用 MiniMax 自有模型                                 |
| **[ArkClaw](https://console.volcengine.com/ark/region:ark+cn-beijing/experience/claw)** | 字节跳动 | 云端             | 火山引擎旗下，深度集成豆包大模型                          |
| **[QClaw](https://qclaw.qq.com/)**                           | 腾讯     | 本地             | 面向企业办公场景                                          |


### 相关文章

- [OpenClaw 全攻略](https://developer.aliyun.com/article/1719048)
- [中美 OpenClaw 发展对比](https://www.163.com/dy/article/KOBC9MBE05568W0A.html)

## 二、Coding Plan

Coding Plan 是各 AI 平台推出的编程模型订阅套餐，以低价月费提供高质量代码生成能力。

### 主流 Coding Plan


| 套餐                                                                              | 厂商        | 价格               | 特点                                                                                                                  |
| ------------------------------------------------------------------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| **[方舟 Coding Plan](https://www.volcengine.com/activity/codingplan)**            | 字节 火山引擎   | 月费 40 元起         | 模型自由、工具不限；升级可解锁 [ArkClaw](https://console.volcengine.com/ark/region:ark+cn-beijing/experience/claw)，7×24 小时在线专属智能伙伴 |
| **[GLM Coding Plan](https://bigmodel.cn/glm-coding)**                           | 智谱 AI     | 月费 49 元起         | 3x Claude Pro 用量额度起，支持月/季/年订阅                                                                                       |
| **[Kimi Code Plan](https://www.kimi.com/code)**                                 | 月之暗面 Kimi | 月费 49 元起         | 仅限Kimi系列模型（K2、K2.5、K2 Thinking等）                                                                                    |
| **[MiniMax Token Plan](https://platform.minimax.io/subscribe/token-plan)**      | MiniMax   | 月费 10 美元起        | 仅限MiniMax系列模型（M2、M2.1、M2.5、最新M2.7等）                                                                                 |
| **[阿里云 Coding Plan](https://www.alibabacloud.com/zh/campaign/ai-scene-coding)** | 阿里云       | 月费 Pro 高级套餐 200元 | 支持 qwen3.5-plus , kimi-k2.5 , glm-5, MiniMax-M2.5，完美兼容 Cline、Claude Code 及 Qwen Code                                |


### Coding Plan 趋势

- 各家 Coding Plan 正从单一模型走向多模型聚合，用户可自由切换

### 相关文章

- [已知国内 LLM Coding Plan 订阅套餐整理 - 知乎](https://zhuanlan.zhihu.com/p/2006431542428315931)
- [AI Coding Plan 对比 - Coding Plan 对比工具](https://z4crk6mg95.coze.site/)



## 三、三方模型（API）

三方模型指通过 API 调用的第三方大语言模型服务，涵盖国际主流和国产模型。

### 国际主流模型 API


| 模型                                                         | 厂商      | 特点                                                       |
| ------------------------------------------------------------ | --------- | ---------------------------------------------------------- |
| **[Claude API (Sonnet/Opus/Haiku)](https://docs.anthropic.com/zh-CN/docs/claude/claude-api)** | Anthropic | 代码理解能力强，Claude 4.5 Sonnet 在代码生成评测中表现突出 |
| **[GPT-5](https://developers.openai.com/api/docs)**          | OpenAI    | 全能型基准，代码生成能力强，GPT-5.2 在代码质量评测中领先   |
| **[Gemini 系列](https://ai.google.dev/gemini-api)**          | Google    | 多模态能力，Gemini 3 在代码评测中表现优异                  |


### 国产主流模型 API


| 模型                                                | 厂商     | 特点                                   |
| --------------------------------------------------- | -------- | -------------------------------------- |
| **[DeepSeek 系列](https://platform.deepseek.com/)** | 深度求索 | 开源强推理模型，成本低，编码能力强     |
| **[Qwen3 系列](https://qwen.ai/apiplatform)**       | 阿里     | 多尺寸可选（32B/235B等），中文理解精准 |
| **[Kimi-K2](https://platform.moonshot.ai/)**        | 月之暗面 | 长上下文，中文场景优势                 |
| **[GLM-5.x 系列](https://bigmodel.cn/console/)**    | 智谱 AI  | 国内老牌模型，编码场景持续优化         |
| **[MiniMax M2](https://www.minimaxi.com/)**         | MiniMax  | 开源模型，音乐、语音、视频模型         |


### 模型聚合平台

- **[OpenRouter](https://openrouter.ai/)**：统一 API 网关，支持 500+ 模型、60+ 提供商，OpenAI 兼容接口
- **[Hugging Face](https://huggingface.co/)**：提供开源模型托管和推理服务



## 四、CLI 种类

CLI（命令行界面）AI 工具是终端中的 AI 编程助手，支持自然语言驱动开发全流程。

**提示**：开源 CLI 工具生态还在快速演进，建议关注各工具的插件体系和 MCP 集成能力。

### 主流 AI CLI 工具


| 工具                                                         | 厂商      | 特点                                                         |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| **[Claude Code](https://docs.anthropic.com/zh-CN/docs/claude-code/overview)** | Anthropic | 终端级深度编码助手，2026年最受喜爱的 AI 编码工具（46% 偏好） |
| **[Codex CLI](https://openai.com/codex/)**                   | OpenAI    | 开源命令行工具，基于 GPT-4o，面向交互式终端 AI 助手          |
| **[OpenCode](https://opencode.ai/)**                         | 开源      | 141K+ GitHub 星标                                            |
| **[Gemini CLI](https://geminicli.com/)**                     | Google    | 面向开发者的 AI 命令行工具                                   |
| **[Qoder CLI](https://qoder.com)**                           | 阿里      | 200ms 响应，Quest 自主编程模式，CodeReview 能力              |
| **[CodeBuddy](https://codebuddy.cn/)**                       | 腾讯      | 命令行中用自然语言驱动开发全流程                             |



## 五、好用的 Skill

Skills（技能） 是一种为 AI 预定义可复用的专业能力的机制。

通过 Skills，你可以把常用的操作流程、专业知识、行为规范封装成一个"技能包"，让 AI 在特定场景下自动激活和使用。

**提示**：建议关注各 AI IDE（Cursor、Windsurf、Trae）的 Rules/Skills 社区生态，以及 Claude Code 的插件市场。

### 主流 Skill 生态


| 平台                                                         | 特点                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **[Claude 官方 Skills](https://github.com/anthropics/skills)** | Anthropic 为 Claude 实现的技能                               |
| **[Cursor Skills](https://cursor.com/cn/docs/skills)**       | AI IDE 支持 Agent、MCP等                                     |
| **[VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)** | GitHub 开源项目，OpenClaw 技能合集                           |
| **[travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)** | 一份精选的 Claude 技能、资源和工具列表，用于自定义 Claude AI 工作流程 |
| [Skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | 创建新技能、修改和改进现有技能，并衡量技能表现               |
| [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 创建具有独特风格、生产级品质且设计精良的前端界面             |
| [PDF](https://github.com/anthropics/skills/tree/main/skills/pdf) | 对 PDF 文件进行任何操作                                      |

### 值得关注的 Skill 类型

- 代码生成类：REST API 生成、单元测试编写、数据库 Schema 设计
- 办公自动化类：文件整理、邮件处理、Excel 报表生成
- 内容创作类：营销文案生成、短视频脚本、社交媒体排版发布
- 金融投研类：股票行情监控、财报分析、信号触发



## 六、MCP

MCP（模型上下文协议）是 Anthropic 提出的开放协议，为 LLM 应用与外部数据源、工具之间提供标准化集成方式，被形象地称为"AI 应用的 USB-C 接口"。

### **热门 MCP 服务器**

| MCP Server | 功能领域 |
| --- | --- |
| **[GitHub](https://github.com/github/github-mcp-server)** | Issues、PRs、仓库管理 |
| **[Playwright](https://github.com/microsoft/playwright-mcp)** | 微软官方，AI 精确控制网页、自动化数据抓取 |
| **[Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** | 网页抓取、内容提取，AI 必备数据源 |
| **[Context7](https://github.com/upstash/context7)** | 实时获取库最新文档和代码示例，编码神器 |
| **[Jina AI](https://github.com/jina-ai/mcp)** | 语义搜索、图像搜索、跨模态搜索 |
| **[Notion](https://github.com/makenotion/notion-mcp-server)** | 页面创建、编辑、搜索 |
| **[飞书 Lark](https://github.com/larksuite/lark-openapi-mcp)** | 飞书消息、日历、文档 |
| **[Figma](https://github.com/GLips/Figma-Context-MCP)** | MCP 服务器向 Agent 提供 Figma 布局信息 |

### 支持 MCP 的客户端

| MCP Client | 简介 |
| --- | --- |
| **[Claude Desktop](https://claude.ai/)** | Anthropic 官方桌面客户端 |
| **[Claude Code](https://docs.anthropic.com/zh-CN/docs/claude-code/overview)** | Anthropic 终端级 AI 编程助手 |
| **[Cursor](https://www.cursor.com/)** | AI 原生 IDE（基于 VSCode） |
| **[Windsurf](https://www.windsurf.com/)** | Codeium 出品 AI IDE |
| **[Trae](https://www.trae.cn/)** | 字节 出品 AI IDE |
| **[Cherry Studio](https://www.cherry-ai.com/)** | 支持多模型并行对话的跨平台AI桌面客户端 |

### 相关文章

- **MCP 官方规范**：[modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP 协议详解**：[腾讯云开发者社区](https://developer.cloud.tencent.com/article/2508227)
- **[MCP Server 市场（mcp.so）](https://mcp.so/zh)**



## 七、编程工具 IDE

### IDE / 编辑器类


| 工具                                                      | 类型          | 特点                                                   |
| --------------------------------------------------------- | ------------- | ------------------------------------------------------ |
| **[Cursor](https://www.cursor.com/)**                     | AI 原生 IDE   | 基于 VSCode，AI 编程新宠儿，Composer 模式、Agent 模式  |
| **[Windsurf](https://www.windsurf.com/)**                 | AI 原生 IDE   | Codeium 出品，流畅的 AI 协作体验                       |
| **[Trae](https://www.trae.ai/)**                          | 字节 AI IDE   | 基础版免费，中文指令理解精准度高                       |
| **[GitHub Copilot](https://github.com/features/copilot)** | 微软 IDE 插件 | 微软生态的智能编码标配                                 |
| **[CodeBuddy](https://codebuddy.cn/)**                    | 腾讯 全栈 IDE | 混元+DeepSeek 双引擎，Plan-Coding-Deploy 三 Agent 协同 |


### Web / 浏览器类


| 工具                                  | 特点                       |
| ----------------------------------- | ------------------------ |
| **[Bolt.new](https://bolt.new/)**   | 浏览器中构建全栈应用，StackBlitz 出品 |
| **[V0 by Vercel](https://v0.dev/)** | 从文本描述生成 React 组件/UI      |
| **[Replit](https://replit.com/)**   | 浏览器端编码、运行、部署一体化          |



## 八、Agent 框架

AI Agent 框架提供构建自主推理、规划和执行任务的智能体系统的基础设施。

### 主流 Agent 框架


| 框架                                                         | 特点                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **[LangChain / LangGraph](https://www.langchain.com/)**      | 最成熟的生态，LangGraph 专注状态图多 Agent 编排，生产验证最充分 |
| **[AutoGen](https://microsoft.github.io/autogen/)**          | 微软出品，多 Agent 对话协作                                  |
| **[CrewAI](https://crewai.com/)**                            | 角色化多 Agent 协作                                          |
| **[Claude Code](https://docs.anthropic.com/zh-CN/docs/claude-code/overview)** | Anthropic 的 Agent 能力封装                                  |
| **[OpenClaw](https://openclaw.ai/)**                         | 开源本地 AI 智能体，强调"动手执行"，可 7×24 小时自动化       |

### 低代码智能体平台

- **[Coze](https://www.coze.cn/)**：零代码 AI 工作流，易上手，适合 AI 密集型任务
- **[Dify](https://dify.ai/)**：低代码 AI 应用工厂，支持私有化部署，企业级复杂流程
- **[n8n](https://n8n.io/)**：开源智能流程自动化中枢，擅长系统集成，高度定制化自动化

### 相关文章

- **Multi-Agent 框架终极对比：LangGraph、CrewAI、AutoGen**：[腾讯云开发者社区](https://cloud.tencent.com/developer/article/2639437)
- **CrewAI vs LangGraph vs AutoGen 深度对比**：[Eimoon Blog](https://blog.eimoon.com/p/crewai-langgraph-autogen-multi-agent-ai-frameworks-comparison/)
- **Agent 框架横向对比**：[知乎](https://zhuanlan.zhihu.com/p/1984725399767376336)
- **[一文讲懂Agent及主流Agent框架介绍 - 知乎](https://zhuanlan.zhihu.com/p/1962475257895052209)**



## 九、RAG 框架

RAG（检索增强生成）框架。2026 年的趋势是向 Agentic RAG 和上下文工程演进。

### 主流 RAG 框架


| 框架                                                       | 特点                                             |
| ---------------------------------------------------------- | ------------------------------------------------ |
| **[RAGFlow](https://ragflow.io/)**                         | 企业级知识处理引擎，深度文档解析，表格识别能力强 |
| **[LlamaIndex](https://github.com/run-llama/llama_index)** | 数据框架，RAG 核心工具，支持 Agent 集成          |
| **[LangChain](https://www.langchain.com/)**                | RAG 基础组件丰富，生态最大                       |
| **[FastGPT](https://fastgpt.cn/)**                         | 高速内容生成专家，轻量易用                       |


### RAG 演进方向

- **GraphRAG**：结合知识图谱提升检索精度
- **Agentic RAG**：Agent 驱动的动态检索
- **多模态 RAG**：支持图像、表格等多类型数据
- **上下文工程**：从简单检索到智能上下文编排



## 十、向量知识库

### 主流向量数据库


| 数据库                                    | 类型        | 特点                               |
| ----------------------------------------- | ----------- | ---------------------------------- |
| **[Pinecone](https://www.pinecone.io/)**  | 云服务      | 全托管，企业级，易上手             |
| **[Milvus / Zilliz](https://milvus.io/)** | 开源/云服务 | 生产级，大规模向量检索，云原生架构 |
| **[Qdrant](https://qdrant.tech/)**        | 开源/云服务 | Rust 编写，高性能，支持过滤        |
| **[Weaviate](https://weaviate.io/)**      | 开源/云服务 | 内置向量化模块，GraphQL API        |
| **[Chroma](https://trychroma.com/)**      | 开源        | 轻量级，适合原型和中小规模         |


### 相关文章

- **向量数据库全面解析：从原理到选型**：[CSDN](https://blog.csdn.net/u014354882/article/details/159767868)



## 十一、Embedding 模型

Embedding 模型将文本转换为向量表示，是 RAG 和语义搜索的核心组件。

**[MTEB Leaderboardb：embedding 模型的“标准化能力排行榜”](https://huggingface.co/spaces/mteb/leaderboard)**

### 主流 Embedding 模型


| 模型                                                         | 特点                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **[Qwen3-Embedding-4B/8B](https://qwen.ai/blog?id=qwen3-embedding)** | 阿里开源，MTEB 榜单领先，4B 版性价比高，8B 版精度优          |
| **[Gemini Embedding 2](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)** | 跨模态、跨语言、关键词检索综合最强                           |
| **[KaLM-Embedding](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511)** | 腾讯开源百亿参数模型，MTEB 多语言榜单全球第一（72.32 分），覆盖 1038 种语言 |
| **[OpenAI text-embedding-3](https://platform.openai.com/docs/guides/embeddings/)** | RAG 原型最常用，易于集成，但生产 RAG 中可能不够用            |
| **[Jina Embeddings](https://jina.ai/)**                      | 多语言支持，擅长长文档                                       |
| **[BGE 系列](https://github.com/FlagOpen/FlagEmbedding)**    | BAAI 出品，中英文双语强，开源社区广泛使用                    |



## 十二、Vibe Coding 四种

Vibe Coding 由 AI 研究员 Andrej Karpathy 于 2025 年 2 月提出，指通过自然语言描述需求让 AI 生成代码，而非手动编写。

### 四种开发者原型（按技术知识与 AI 依赖度分类）


| 原型        | 技术知识 | AI 依赖度 | 核心特征                                     |
| --------- | ---- | ------ | ---------------------------------------- |
| **传统工程师** | 高    | 低      | 全面理解代码库，谨慎使用 AI，聚焦系统完整性，未来将转向架构/安全/系统设计  |
| **增强工程师** | 高    | 高      | 深度依赖 AI 同时保持技术理解，评估和优化 AI 生成方案，将成为主导开发范式 |
| **新兴开发者** | 低    | 低      | 传统方式学习基础，使用基础辅助工具，群体正在缩小                 |
| **领域创造者** | 低    | 高      | 专注问题描述而非实现细节，快速原型，将分化为纯非技术创作者与技术学习者      |

### 四种 AI 编程范式

| 范式                    | 核心思想           | 前置工作       | 适用场景           | 核心优势              |
| ----------------------- | ------------------ | -------------- | ------------------ | --------------------- |
| **Vibe Coding**         | 灵感驱动，边做边改 | 很少，快速启动 | 创意探索、原型验证 | 最快出结果，抓住灵感  |
| **Spec Coding**         | 先定义，再开发     | 完整规格说明   | 需求明确、模块交付 | AI 容易执行，结果可控 |
| **Glue Coding**         | 复用整合，拼装交付 | 梳理已有模块   | MVP 开发、应用整合 | 最快交付，效率最高    |
| **Harness Engineering** | 质检门禁，返工迭代 | 定义质检标准   | 生产环境、大型项目 | 质量可控，可维护性好  |

### 相关文章

- **[Vibe Coding 是什么？AI 时代 Vibe Coding 深度解析与工具推荐](https://qubittool.com/zh/blog/vibe-coding-complete-guide)**
- **[Vibe Coding 完全指南：从"氛围编程"到 Agentic Engineering](https://zhuanlan.zhihu.com/p/2010879714030540578)**
- **[easy-vibe：Datawhale Vibe Coding 教程](https://datawhalechina.github.io/easy-vibe)**



## 十三、资源导航

### 工具导航站

- **[AI 工具导航](https://www.ai-all.info/)**
- **[Product Hunt AI](https://www.producthunt.com/categories/ai)**

### 评测与榜单

- **[Artificial Analysis](https://artificialanalysis.ai/)**
- **[OpenRouter 模型排行](https://openrouter.ai/rankings)**

### 社区与资源

- **[GitHub Trending](https://github.com/trending)**
- **[Hugging Face](https://huggingface.co/)**
- **[ModelScope 魔搭社区](https://modelscope.cn/)**
- **[Datawhale 专注于AI领域的开源组织](https://github.com/datawhalechina)**

### 建议持续关注方向

- **龙虾生态**：国内 Claw 产品百花齐放，安全机制和 Skills 市场是关注重点
- **Coding Plan 竞争**：各厂商 Coding Plan 定价和模型覆盖范围快速变化
- **MCP、Skill 生态**：正在快速演进，每周都有新的 MCP Server、Skill 发布
- **Agent 框架融合**：AutoGen 与 Semantic Kernel 合并为 Microsoft Agent Framework，行业正从分散走向统一
- **GraphRAG 与 Agentic RAG**：下一代 RAG 架构正在成为企业知识管理新标准

