# 十一、Embedding 模型

[← 上一章：十、向量知识库](../chapter10/10-vector-databases.md) | [返回总览](../index.md) | [下一章：十二、Vibe Coding 四种 →](../chapter12/12-vibe-coding.md)

Embedding 模型将文本转换为向量表示，是 RAG 和语义搜索的核心组件。

**[MTEB Leaderboardb：embedding 模型的“标准化能力排行榜”](https://huggingface.co/spaces/mteb/leaderboard)**

## 主流 Embedding 模型

| 模型                                                                                                                    | 特点                                             |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **[Qwen3-Embedding-4B/8B](https://qwen.ai/blog?id=qwen3-embedding)**                                                  | 阿里开源，MTEB 榜单领先，4B 版性价比高，8B 版精度优                |
| **[Gemini Embedding 2](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)** | 跨模态、跨语言、关键词检索综合最强                              |
| **[KaLM-Embedding](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511)**                                   | 腾讯开源百亿参数模型，MTEB 多语言榜单全球第一（72.32 分），覆盖 1038 种语言 |
| **[OpenAI text-embedding-3](https://platform.openai.com/docs/guides/embeddings/)**                                    | RAG 原型最常用，易于集成，但生产 RAG 中可能不够用                  |
| **[Jina Embeddings](https://jina.ai/)**                                                                               | 多语言支持，擅长长文档                                    |
| **[BGE 系列](https://github.com/FlagOpen/FlagEmbedding)**                                                               | BAAI 出品，中英文双语强，开源社区广泛使用                        |
