# 十一、Embedding 模型

[← 上一章：十、向量知识库](../chapter10/10-vector-databases.md) | [返回总览](../index.md) | [下一章：十二、Vibe Coding 四种 →](../chapter12/12-vibe-coding.md)

Embedding 模型将文本转换为向量表示，是 RAG 和语义搜索的核心组件。

## Embedding 模型选型对比

| 模型 | 维度 | 开源 | 中文优化 | 多语言 | MTEB 表现 | 适用场景 |
|------|------|------|---------|--------|----------|---------|
| Qwen3-Embedding-4B/8B | 可变 | 开源 | 优 | 强 | 榜单领先 | 中文 RAG 首选 |
| Gemini Embedding 2 | — | API | 良 | 极强 | 关键词检索最强 | 跨模态、跨语言搜索 |
| KaLM-Embedding (12B) | — | 开源 | 优 | 极强（1038 语言） | 曾登顶多语言榜首 | 多语言 RAG |
| OpenAI text-embedding-3 | 256-3072 | API | 中 | 良 | 中上 | 快速原型，与 OpenAI 生态集成 |
| Jina Embeddings | — | 开源 | 中 | 强 | — | 长文档嵌入 |
| BGE 系列 | — | 开源 | 优 | 强（中英双语） | 高 | 开源社区首选，成熟稳定 |
| Cohere Embed | — | API | 中 | 强 | — | 企业级 RAG |

## 选型建议

- **中文 RAG 首选** → **BGE 系列**（开源成熟）/ **Qwen3-Embedding**（榜单领先）
- **多语言场景** → **KaLM-Embedding**（1038 语言覆盖）/ **Gemini Embedding 2**
- **快速开始** → **OpenAI text-embedding-3**（API 调用，零配置）
- **长文档处理** → **Jina Embeddings**（擅长长文本）
- **企业级** → **Cohere Embed**（企业级 SLA）

> 实时排名请查看 **[MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)**

## 主流 Embedding 模型

| 模型                                                                                                                    | 特点                                             |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **[Qwen3-Embedding-4B/8B](https://qwen.ai/blog?id=qwen3-embedding)**                                                  | 阿里开源，MTEB 榜单领先，4B 版性价比高，8B 版精度优                |
| **[Gemini Embedding 2](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)** | 跨模态、跨语言、关键词检索综合最强                              |
| **[KaLM-Embedding](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511)**                                   | 腾讯开源百亿参数模型，曾登顶 MTEB 多语言榜单（72.32 分），覆盖 1038 种语言 |
| **[OpenAI text-embedding-3](https://platform.openai.com/docs/guides/embeddings/)**                                    | RAG 原型最常用，易于集成，但生产 RAG 中可能不够用                  |
| **[Jina Embeddings](https://jina.ai/)**                                                                               | 多语言支持，擅长长文档                                    |
| **[BGE 系列](https://github.com/FlagOpen/FlagEmbedding)**                                                               | BAAI 出品，中英文双语强，开源社区广泛使用                        |
| **[Cohere Embed](https://cohere.com/embed)**                                                                          | 企业级 Embedding，多语言支持，RAG 场景优化                   |
