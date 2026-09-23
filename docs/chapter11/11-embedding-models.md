# 十一、Embedding 模型

[← 上一章：十、向量知识库](../chapter10/10-vector-databases.md) | [返回总览](../index.md) | [下一章：十二、Vibe Coding 四种 →](../chapter12/12-vibe-coding.md)

Embedding 模型将文本转换为向量表示，是 RAG 和语义搜索的核心组件。

## Embedding 模型选型对比

| 模型 | 维度 | 开源 | 中文优化 | 多语言 | MTEB 表现 | 适用场景 |
|------|------|------|---------|--------|----------|---------|
| Qwen3-Embedding-4B/8B | 可变 | 开源 | 优 | 强 | MTEB(eng,v1) **第 2**（8B） | 中文 RAG 首选 |
| Conan-embedding-v2 | — | 开源 | 良 | 强 | MTEB(eng,v1) **第 1**（74.22） | 英文检索、榜单基线 |
| Harrier-OSS-v1-27B | — | 开源（MIT） | 中 | 极强 | **MTEB 多语言 v2 第 1**（74.27） | 多语言检索（当前最强档） |
| KaLM-Embedding (12B) | — | 开源 | 优 | 极强（1038 语言） | 多语言 v2 **第 2**（72.32） | 多语言 RAG |
| Gemini Embedding 2 | — | API | 良 | 极强 | 关键词检索最强 | 跨模态、跨语言搜索 |
| OpenAI text-embedding-3 | 256-3072 | API | 中 | 良 | 中上 | 快速原型，与 OpenAI 生态集成 |
| Jina Embeddings | — | 开源 | 中 | 强 | — | 长文档嵌入 |
| BGE 系列 | — | 开源 | 优 | 强（中英双语） | 高 | 开源社区首选，成熟稳定 |
| Cohere Embed | — | API | 中 | 强 | — | 企业级 RAG |

> ⚠️ **别直接横比 MTEB 分数**：MTEB 已拆分为 **v1 / v2** 两套榜单，任务集与计分方式都改过，**两边的分数不可直接比较**；同一模型在「英文榜」与「多语言榜」上的名次也常常不一致。所以表中同时标注了**榜单名**——选型时请认准与你场景匹配的那一张（英文检索看 MTEB(eng)，跨语言看 Multilingual），并到最新榜单页确认。榜单变动很快，本表的排名随时可能过时。

## 选型建议

- **中文 RAG 首选** → **BGE 系列**（开源成熟）/ **Qwen3-Embedding**（MTEB(eng,v1) 第 2）
- **多语言场景** → **Harrier-OSS-v1-27B**（当前多语言榜首）/ **KaLM-Embedding**（1038 语言覆盖）
- **英文检索基线** → **Conan-embedding-v2**（MTEB(eng,v1) 第 1）
- **快速开始** → **OpenAI text-embedding-3**（API 调用，零配置）
- **长文档处理** → **Jina Embeddings**（擅长长文本）
- **企业级** → **Cohere Embed**（企业级 SLA）

> 实时排名请查看 **[MTEB 官方榜单](https://leaderboard.mteb.org/)**（注意先确认是 v1 还是 v2）

## 核心概念

### 维度选择

| 维度 | 特点 | 适用场景 |
|------|------|---------|
| 低（256-384） | 存储省、检索快，精度略低 | 大规模初筛、对延迟敏感 |
| 中（768-1024） | 精度与性能平衡 | 大多数 RAG 场景 |
| 高（1536-3072） | 精度最高，存储和检索成本大 | 高精度要求、小数据集 |

**选择建议**：优先用模型默认维度；如果存储/检索是瓶颈，OpenAI text-embedding-3 支持通过 `dimensions` 参数降维，BGE 可选 small 版本。

### Chunk 策略

文档送入 Embedding 前需要切分（chunk），切分策略直接影响检索质量：

| 策略 | 说明 | 适用场景 |
|------|------|---------|
| **固定长度** | 按字符/token 数切分，加 overlap | 通用场景，简单可靠 |
| **语义切分** | 按段落/章节/句子边界切分 | 文档结构清晰 |
| **递归切分** | 优先按分隔符切，超出则递归 | LangChain 默认策略，适用面广 |
| **文档解析切分** | 基于 PDF/HTML 结构切分 | 表格密集型文档 |

**关键参数**：chunk_size 建议 256-512 token（中文偏短），overlap 建议 10%-20%，避免语义断裂。

### 多向量 vs 单向量

| 方案 | 说明 | 适用场景 |
|------|------|---------|
| **单向量** | 整个文档/段落生成一个向量 | 短文本、段落级检索 |
| **多向量（ColBERT）** | 每个 token 生成一个向量，检索时逐 token 匹配 | 需要细粒度匹配（如法律条文） |
| **多向量（摘要+详情）** | 文档的摘要和详情分别生成向量 | 长文档，先粗筛后精排 |

## 主流 Embedding 模型

| 模型                                                                                                                    | 特点                                             |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **[Qwen3-Embedding-4B/8B](https://qwen.ai/blog?id=qwen3-embedding)**                                                  | 阿里开源，MTEB(eng,v1) 第 2（8B 版），4B 版性价比高，8B 版精度优      |
| **[Conan-embedding-v2](https://huggingface.co/TencentBAC/Conan-embedding-v2)**                                        | 腾讯开源，MTEB(eng,v1) 第 1（74.22），英文检索当前最强档           |
| **[Harrier-OSS-v1](https://huggingface.co/microsoft/harrier-oss-v1-27b)**                                             | 微软开源（MIT），**MTEB 多语言 v2 第 1**（27B 版 74.27）；提供 270M / 0.6B / 27B 三档 |
| **[KaLM-Embedding](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511)**                                   | 腾讯开源百亿参数模型，多语言 v2 第 2（72.32 分），覆盖 1038 种语言      |
| **[Gemini Embedding 2](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)** | 跨模态、跨语言、关键词检索综合最强                              |
| **[OpenAI text-embedding-3](https://platform.openai.com/docs/guides/embeddings/)**                                    | RAG 原型最常用，易于集成，但生产 RAG 中可能不够用                  |
| **[Jina Embeddings](https://jina.ai/)**                                                                               | 多语言支持，擅长长文档                                    |
| **[BGE 系列](https://github.com/FlagOpen/FlagEmbedding)**                                                               | BAAI 出品，中英文双语强，开源社区广泛使用                        |
| **[Cohere Embed](https://cohere.com/embed)**                                                                          | 企业级 Embedding，多语言支持，RAG 场景优化                   |
