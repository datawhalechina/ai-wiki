# 八、Agent 框架

[← 上一章：七、编程工具 IDE](../chapter07/07-ide-tools.md) | [返回总览](../index.md) | [下一章：九、RAG 框架 →](../chapter09/09-rag-frameworks.md)

AI Agent 框架提供构建自主推理、规划和执行任务的智能体系统的基础设施。

## Agent 设计模式

选择框架前，先理解 Agent 的核心设计模式，不同模式适合不同场景：

| 模式 | 核心思想 | 适用场景 | 代表框架 |
|------|---------|---------|---------|
| **ReAct** | 推理(Reason)+行动(Act)交替：先想再干，观察结果后决定下一步 | 需要工具调用的单 Agent | LangChain ReAct Agent |
| **Plan-Execute** | 先规划完整步骤，再逐步执行，可动态调整计划 | 多步骤复杂任务 | LangGraph PlanExecute |
| **Multi-Agent 编排** | 多个 Agent 分工协作，通过对话或消息传递协调 | 需要多角色协作的任务 | CrewAI、AutoGen、LangGraph |
| **反射（Reflection）** | Agent 执行后自我评估，发现问题则修正重做 | 需要高质量输出的场景 | LangGraph Self-Reflective |
| **路由（Router）** | 根据输入意图分发给不同专业 Agent 处理 | 多领域问答/客服 | LangChain Router |

**选择建议**：
- 单 Agent + 工具调用 → **ReAct**
- 任务复杂、步骤多 → **Plan-Execute**
- 需要多角色协作 → **Multi-Agent**
- 质量要求高 → **ReAct + Reflection** 组合

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

## 5 分钟快速上手：用 CrewAI 创建多 Agent 协作

```bash
# 1. 安装
pip install crewai

# 2. 创建 crew_demo.py
cat > crew_demo.py << 'EOF'
from crewai import Agent, Task, Crew

# 定义两个 Agent
researcher = Agent(
    role="研究员",
    goal="研究指定主题的最新进展",
    backstory="你是一位资深 AI 研究员",
)

writer = Agent(
    role="撰稿人",
    goal="将研究结果写成简洁的文章",
    backstory="你是一位擅长科技写作的撰稿人",
)

# 定义任务
research_task = Task(
    description="研究 2026 年 RAG 技术的最新进展",
    agent=researcher,
)

write_task = Task(
    description="基于研究结果，写一篇 500 字的技术摘要",
    agent=writer,
)

# 组建 Crew 并运行
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
print(result)
EOF

# 3. 运行（需要设置 OPENAI_API_KEY 或其他 LLM API Key）
python crew_demo.py
```

**国内用户**：可配置 `openai_api_base` 指向国内模型 API（如 DeepSeek），降低成本。

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

