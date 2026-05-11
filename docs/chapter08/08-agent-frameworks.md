# 八、Agent 框架

[← 上一章：七、编程工具 IDE](../chapter07/07-ide-tools.md) | [返回总览](../index.md) | [下一章：九、RAG 框架 →](../chapter09/09-rag-frameworks.md)

AI Agent 框架提供构建自主推理、规划和执行任务的智能体系统的基础设施。

## 主流 Agent 框架

| 框架                                                         | 特点                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **[LangChain / LangGraph](https://www.langchain.com/)**      | 最成熟的生态，LangGraph 专注状态图多 Agent 编排，生产验证最充分 |
| **[AutoGen](https://microsoft.github.io/autogen/)**          | 微软出品，多 Agent 对话协作                                  |
| **[CrewAI](https://crewai.com/)**                            | 角色化多 Agent 协作                                          |
| **[Claude Code](https://code.claude.com/docs/zh-CN/overview)** | Anthropic 的 Agent 能力封装，122K+ GitHub 星标               |
| **[OpenClaw](https://openclaw.ai/)**                         | 开源本地 AI 智能体，强调"动手执行"，可 7×24 小时自动化       |
| **[Hermes Agent](https://github.com/nousresearch/hermes-agent)** | 开源新星 142K star；Hermes Agent 是由 Nous Research 开发的开源、自托管自主 AI 智能体框架，专注于持久记忆、自我进化和跨平台工具使用，常被称为”会随着使用不断成长的数字员工”。它能持久化记忆，在跨会话中沉淀技能，并支持飞书、Telegram 等多平台接入。 |
| **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** | 微软推出的统一 Agent 框架，融合 AutoGen 和 Semantic Kernel 的多 Agent 模式，支持 Python 和 .NET |

## 低代码智能体平台

- **[Coze](https://www.coze.cn/)**：零代码 AI 工作流，易上手，适合 AI 密集型任务
- **[Dify](https://dify.ai/)**：低代码 AI 应用工厂，支持私有化部署，企业级复杂流程
- **[n8n](https://n8n.io/)**：开源智能流程自动化中枢，擅长系统集成，高度定制化自动化

## Agent 框架选型对比

| 框架 | 成熟度 | 学习曲线 | 多 Agent | 记忆/持久化 | 适用规模 | 典型场景 |
|------|--------|---------|---------|------------|---------|---------|
| LangChain/LangGraph | 极高 | 中 | 原生状态图编排 | 需自行集成 | 生产级 | 复杂多 Agent 工作流 |
| Microsoft Agent Framework | 中 | 中 | 融合 AutoGen+SK 模式 | — | 企业级 | .NET/Python 企业应用 |
| AutoGen | 高 | 中 | 对话式多 Agent | 有限 | 中型+ | 研究探索、对话协作 |
| CrewAI | 高 | 低 | 角色化分工 | 有限 | 中小型 | 快速搭建角色化 Agent |
| Hermes Agent | 中 | 低 | 支持 | 持久记忆+自进化 | 中型 | 个人数字员工，自动化 |
| OpenClaw | 中 | 低 | Skills 驱动 | 会话级 | 中小型 | 本地自动化，IM 操控 |
| Claude Code | 极高 | 低 | Agent 模式内建 | 会话级 | 生产级 | 编码场景，终端 Agent |

## 选型决策树

```
需要编码 Agent？
 ├── 是 → Claude Code（终端编码）/ OpenClaw（本地自动化）
 └── 否 → 需要多 Agent 协作？
           ├── 是 → 生产级？
           │        ├── 是 → LangGraph（最成熟）/ Microsoft Agent Framework（.NET 生态）
           │        └── 否 → CrewAI（快速上手）/ AutoGen（微软生态）
           └── 否 → 需要持久记忆？
                    ├── 是 → Hermes Agent（自进化记忆）
                    └── 否 → 低代码平台（Coze / Dify）
```

## 相关文章

- **Multi-Agent 框架终极对比：LangGraph、CrewAI、AutoGen**：[腾讯云开发者社区](https://cloud.tencent.com/developer/article/2639437)
- **CrewAI vs LangGraph vs AutoGen 深度对比**：[Eimoon Blog](https://blog.eimoon.com/p/crewai-langgraph-autogen-multi-agent-ai-frameworks-comparison/)
- **Agent 框架横向对比**：[知乎](https://zhuanlan.zhihu.com/p/1984725399767376336)
- **[一文讲懂Agent及主流Agent框架介绍 - 知乎](https://zhuanlan.zhihu.com/p/1962475257895052209)**

