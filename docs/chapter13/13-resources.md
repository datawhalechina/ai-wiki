# 十三、资源导航

[← 上一章：十二、Vibe Coding 四种](../chapter12/12-vibe-coding.md) | [返回总览](../index.md) | [下一章：十四、Prompt Engineering →](../chapter14/14-prompt-engineering.md)

## 工具导航站

| 站点 | 核心价值 | 适合谁 | 使用建议 |
|------|---------|--------|---------|
| **[AI 工具导航](https://www.ai-all.info/)** | 工具聚合、分类导航 | 不确定用什么工具时先来逛逛 | 按场景筛选比搜索更高效 |
| **[Product Hunt AI](https://www.producthunt.com/categories/ai)** | 新品发布、热度排行 | 关注前沿趋势、发现新工具 | 每周看一次 Top 5 即可，避免信息过载 |
| **[MCP Server 市场](https://mcp.so/zh)** | MCP 服务器聚合搜索 | 要找特定功能的 MCP Server | 按场景分类浏览，中文友好 |

## 评测与榜单

| 站点 | 核心价值 | 适合谁 | 使用建议 |
|------|---------|--------|---------|
| **[Artificial Analysis](https://artificialanalysis.ai/)** | 模型价格/性能/延迟对比 | 做模型选型决策 | 重点看 Quality vs Price 象限图，找到性价比最优解 |
| **[OpenRouter](https://openrouter.ai/rankings)** | 模型热度榜、调用占比 | 判断哪些模型社区在用 | 排名反映真实使用量，比宣传更有参考价值 |
| **[LMArena](https://arena.ai/)** | LLM 对战榜、Elo 排名 | 对比模型实际对话能力 | 偏主观偏好，适合选对话体验，不适合选推理能力 |
| **[MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)** | Embedding 模型实时排名 | 选 Embedding 模型 | 筛选中文任务（Chinese）列，关注 Retrieval 子榜单 |

### 评测榜单使用建议

- **选推理模型** → Artificial Analysis（客观基准）+ OpenRouter（使用量）
- **选对话模型** → LMArena（人类偏好）+ Artificial Analysis（基准测试）
- **选 Embedding 模型** → MTEB Leaderboard（中文 Retrieval 子榜单）
- **发现新模型** → OpenRouter Rankings（新模型上榜快）+ Product Hunt

## 社区与资源

| 站点 | 核心价值 | 适合谁 | 使用建议 |
|------|---------|--------|---------|
| **[GitHub Trending](https://github.com/trending)** | 开源趋势、热门项目 | 发现新框架/工具 | 关注 AI 相关语言筛选（Python/TypeScript） |
| **[Hugging Face](https://huggingface.co/)** | 模型/数据集/空间 | 模型选型、在线体验 | 直接搜模型名，看 Model Card 和 Benchmark |
| **[ModelScope 魔搭社区](https://modelscope.cn/)** | 国产模型生态 | 国内用户在线体验模型 | 中文模型更全，下载速度更快 |
| **[Datawhale](https://github.com/datawhalechina)** | 教程共建、学习社群 | 系统学习 AI 开发 | 关注开源项目矩阵，参与社区共学 |

## 学习资源

| 类型 | 推荐 | 说明 |
|------|------|------|
| **互动课程** | [Learn Prompting](https://learnprompting.org/) | 开源 Prompt Engineering 课程，从入门到进阶 |
| **官方文档** | [Anthropic 文档](https://docs.anthropic.com/) / [OpenAI 文档](https://platform.openai.com/docs) | 模型使用的一手信息，最权威 |
| **视频教程** | [3Blue1Brown：深度学习](https://www.3blue1brown.com/topics/neural-networks) | 可视化理解 Transformer 等核心概念 |
| **实战项目** | [LangChain Templates](https://github.com/langchain-ai/langchain/tree/master/templates) | 官方模板，直接 clone 改造 |

## 按需求找资源

| 你想做什么 | 先看哪个章节 | 再去哪里找资源 |
|-----------|------------|-------------|
| 选一个编程模型 | 章节三（模型 API） | Artificial Analysis 价格对比 → OpenRouter 热度 |
| 搭建 RAG 系统 | 章节九（RAG 框架） | MTEB 选 Embedding → Hugging Face 体验模型 |
| 写一个 MCP Server | 章节六（MCP） | mcp.so 找参考实现 → FastMCP 文档 |
| 选一个 AI IDE | 章节七（IDE） | Product Hunt 看新品 → GitHub Trending 看热度 |
| 学 Prompt Engineering | 章节十四（Prompt Engineering） | Learn Prompting 课程 → Anthropic 官方文档 |
| 做 Vibe Coding 原型 | 章节十二（Vibe Coding） | Bolt.new 直接上手 → GitHub 找模板项目 |

## 建议持续关注方向

- **龙虾生态**：国内 Claw 产品百花齐放，安全机制和 Skills 市场是关注重点
- **Coding Plan 竞争**：各厂商 Coding Plan 定价和模型覆盖范围快速变化
- **MCP、Skill 生态**：正在快速演进，每周都有新的 MCP Server、Skill 发布
- **Agent 框架融合**：微软推出 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)，统一 AutoGen 与 Semantic Kernel 的多 Agent 模式，行业正从分散走向统一
- **GraphRAG 与 Agentic RAG**：下一代 RAG 架构正在成为企业知识管理新标准
