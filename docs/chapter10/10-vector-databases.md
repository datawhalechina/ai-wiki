# 十、向量知识库

[← 上一章：九、RAG 框架](../chapter09/09-rag-frameworks.md) | [返回总览](../index.md) | [下一章：十一、Embedding 模型 →](../chapter11/11-embedding-models.md)

## 主流向量数据库

2026 年选型的第一层判断不再是"谁的 benchmark 更高"，而是**架构路线**——它基本决定了成本量级和运维方式：

| 路线 | 代表 | 一句话 |
| --- | --- | --- |
| 全托管专用库 | Pinecone、Zilliz Cloud | 不管运维，按量付费，成本最高 |
| 开源自托管 | Milvus、Qdrant、Weaviate | 可控、可私有化，运维自己扛 |
| 寄生于既有数据库 | pgvector / pgvectorscale、LanceDB | 不新增一套数据库系统，2026 年的务实默认 |
| 对象存储原生 | Turbopuffer | 索引放对象存储，闲置数据近乎零成本，代价是冷查询延迟 |

| 数据库 | 类型 | 特点 |
| --- | --- | --- |
| **[Pinecone](https://www.pinecone.io/)** | 云服务 | 全托管（闭源），企业级，易上手；老牌路线，存储成本偏高 |
| **[Turbopuffer](https://turbopuffer.com/)** | 云服务 | **对象存储（S3 / GCS / Azure）原生**，索引不常驻内存；Cursor / Notion / Anthropic 生产使用；无免费档，$16/月起 |
| **[Milvus / Zilliz](https://milvus.io/)** | 开源 / 云服务 | 生产级，大规模向量检索，云原生架构（**46.2K star**） |
| **[Qdrant](https://qdrant.tech/)** | 开源 / 云服务 | Rust 编写，高性能，高级过滤（**34.8K star**） |
| **[Weaviate](https://weaviate.io/)** | 开源 / 云服务 | 内置向量化模块，GraphQL API（**16.8K star**） |
| **[Chroma](https://trychroma.com/)** | 开源（嵌入式） | 轻量、零配置起步，适合原型与中小规模；2025 年以 Rust 重写（**29.4K star**） |
| **[LanceDB](https://lancedb.com/)** | 开源（嵌入式）/ 云 | 进程内运行，**Lance 列存格式（基于 Apache Arrow）**，同一张表存向量与多模态数据，自带版本管理与回滚（**11.5K star**） |
| **[pgvector](https://github.com/pgvector/pgvector)** | Postgres 扩展 | 在既有 PostgreSQL 里做向量检索，与业务数据同事务查询；Supabase / Neon / RDS 等默认自带（**23.1K star**） |
| **[pgvectorscale](https://github.com/timescale/pgvectorscale)** | Postgres 扩展 | Timescale 出品，在 pgvector 之上叠加 **StreamingDiskANN** 磁盘索引与量化压缩，突破内存上限（**3.1K star**） |

## 向量数据库选型对比

| 数据库 | 部署 | 性能 | 规模 | 过滤能力 | 上手难度 | 成本 |
| --- | --- | --- | --- | --- | --- | --- |
| Pinecone | 全托管云 | 高 | 十亿级 | 强（元数据过滤） | 低 | 偏高 |
| Turbopuffer | 全托管云（对象存储） | 高（热缓存 p50 < 10ms；冷查询需从对象存储回载） | 千亿级（官方口径实测 1T+ 文档） | 强（元数据 + BM25 全文 + 混合） | 低 | 用量计费，$16/月起；官方称约为传统方案 1/10 |
| Milvus / Zilliz | 自托管 / 云 | 极高 | 百亿级 | 强（标量 + 向量混合） | 中 | 自托管免费，云付费 |
| Qdrant | 自托管 / 云 | 极高（Rust） | 十亿级 | 强（高级过滤） | 中 | 自托管免费，云付费 |
| Weaviate | 自托管 / 云 | 高 | 亿级 | 强（GraphQL） | 中 | 自托管免费，云付费 |
| Chroma | 嵌入式 | 中 | 百万级 | 基础 | 极低 | 免费 |
| LanceDB | 嵌入式 / 云 | 高（磁盘访问接近内存） | 亿级（单节点 1 亿+） | 中（SQL 风格过滤 + 全文） | 极低 | 自托管免费；云 Pro $39/月 |
| pgvector | Postgres 扩展 | 中（索引需常驻内存） | 千万级 | 强（标准 SQL WHERE） | 极低 | 免费（复用现有 PG） |
| pgvectorscale | Postgres 扩展 | 高（磁盘索引） | 亿级 | 强（标签过滤） | 低 | 免费（开源扩展） |

> **一句话取舍**：把速度和运维交给专用库（Milvus / Qdrant / Pinecone），把成本和"少一套系统"交给 pgvector / LanceDB / Turbopuffer。没有全面最优解，只有约束不同的解。

## 选型建议

- **原型验证（< 100 万向量）** → **Chroma**：零配置，Python 一行启动
- **已在用 Postgres** → **pgvector**（内存吃紧时加 **pgvectorscale**）：不新增一套数据库系统，向量与业务数据同事务查询，备份、权限、连接池全部复用。**2026 年最务实的默认选择**
- **生产环境（千万-亿级）** → **Milvus** / **Qdrant**：性能最强，社区大
- **不想管运维** → **Pinecone** / **Zilliz Cloud**：全托管，开箱即用
- **海量冷数据 + 成本敏感** → **Turbopuffer**：索引放对象存储，闲置命名空间几乎零成本，适合"用户多、单个用户的数据平时没人查"的多租户场景
- **多模态 / 数据工程栈** → **LanceDB**：向量、文本、图像、音频同表存储，本地磁盘与对象存储都能跑，与 Pandas / DuckDB / Polars 衔接顺畅
- **GraphQL 技术栈** → **Weaviate**：原生 GraphQL API
- **Rust 技术栈 + 极致性能** → **Qdrant**：Rust 编写，高并发

## 选型路径

```
你的情况？
 ├── 已在用 Postgres，数据量在千万级以内 → pgvector（内存不够时再加 pgvectorscale）
 ├── 数据在本地 / 边缘，想"一个库文件搞定" → LanceDB；只做原型 → Chroma
 ├── 海量冷数据、成本是第一约束 → Turbopuffer（对象存储原生）
 ├── 已有 ES / OpenSearch 集群 → 先评估集群自带的向量能力，不急着上新库
 └── 要极致性能 / 强多租户隔离 → Milvus、Qdrant、Weaviate

自托管还是托管？
 ├── 有运维能力、要私有化 → 开源自托管（Milvus / Qdrant / Weaviate）
 └── 不想管运维 → 全托管（Pinecone / Zilliz Cloud / Turbopuffer）
```

## 核心概念

### 向量索引类型

| 索引类型 | 原理 | 查询速度 | 召回率 | 内存占用 | 适用场景 |
| --- | --- | --- | --- | --- | --- |
| **HNSW** | 基于图的近似最近邻，多层跳表导航 | 极快 | 高 | 较高 | 生产环境首选，延迟敏感 |
| **IVF** | 先聚类再搜索，只查相关聚类 | 快 | 中 | 低 | 大规模数据，可接受精度换速度 |
| **Flat（暴力）** | 逐个比较，精确搜索 | 慢 | 100% | 低 | 小数据集（< 10 万），需要精确结果 |
| **DiskANN** | 图索引与向量存盘，查询时按需流式读取 | 快 | 高 | 低（内存只留压缩副本） | 数据量超出内存、成本敏感 |

**选择建议**：< 100 万向量用 Flat（精确）；100 万 - 1 亿用 HNSW（又快又准）；> 1 亿用 IVF + HNSW 组合；**内存装不下时改用 DiskANN 磁盘索引**（如 pgvectorscale 的 StreamingDiskANN）。

### 混合检索

纯向量检索可能遗漏关键词精确匹配，混合检索同时使用向量 + 关键词，兼顾语义和精确匹配：

```
用户查询："Python 3.12 新特性"
  ├── 向量检索 → 找到语义相关的文档
  ├── 关键词检索（BM25）→ 精确匹配"Python 3.12"
  └── 融合排序（RRF）→ 综合两路结果，重排输出
```

Milvus、Qdrant、Weaviate、Turbopuffer、LanceDB 都原生支持混合检索；Postgres 侧可配合 BM25 扩展（如 ParadeDB）补齐关键词一路。

### 过滤策略

在向量检索前/后加上元数据过滤（如时间、类别、权限），缩小检索范围：

- **预过滤**：先过滤元数据，再在子集中做向量搜索。适合过滤后数据量仍较大的场景
- **后过滤**：先做向量搜索，再过滤不满足条件的结果。可能丢失结果，需增大 top-k

## 相关文章

- **向量数据库全面解析：从原理到选型**：[CSDN](https://blog.csdn.net/u014354882/article/details/159767868)
