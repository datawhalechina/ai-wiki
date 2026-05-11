# 十、向量知识库

[← 上一章：九、RAG 框架](../chapter09/09-rag-frameworks.md) | [返回总览](../index.md) | [下一章：十一、Embedding 模型 →](../chapter11/11-embedding-models.md)

## 主流向量数据库

| 数据库                                       | 类型     | 特点                  |
| ----------------------------------------- | ------ | ------------------- |
| **[Pinecone](https://www.pinecone.io/)**  | 云服务    | 全托管，企业级，易上手         |
| **[Milvus / Zilliz](https://milvus.io/)** | 开源/云服务 | 生产级，大规模向量检索，云原生架构   |
| **[Qdrant](https://qdrant.tech/)**        | 开源/云服务 | Rust 编写，高性能，支持过滤    |
| **[Weaviate](https://weaviate.io/)**      | 开源/云服务 | 内置向量化模块，GraphQL API |
| **[Chroma](https://trychroma.com/)**      | 开源     | 轻量级，适合原型和中小规模       |

## 向量数据库选型对比

| 数据库 | 部署 | 性能 | 规模 | 过滤能力 | 上手难度 | 成本 |
|--------|------|------|------|---------|---------|------|
| Pinecone | 全托管云 | 高 | 十亿级 | 强（元数据过滤） | 低 | 偏高 |
| Milvus/Zilliz | 自托管/云 | 极高 | 百亿级 | 强（标量+向量混合） | 中 | 自托管免费，云付费 |
| Qdrant | 自托管/云 | 极高（Rust） | 十亿级 | 强（高级过滤） | 中 | 自托管免费，云付费 |
| Weaviate | 自托管/云 | 高 | 亿级 | 强（GraphQL） | 中 | 自托管免费，云付费 |
| Chroma | 自托管 | 中 | 百万级 | 基础 | 极低 | 免费 |

## 选型建议

- **原型验证（<1M 向量）** → **Chroma**：零配置，Python 一行启动
- **生产环境（千万-亿级）** → **Milvus** / **Qdrant**：性能最强，社区大
- **不想管运维** → **Pinecone** / **Zilliz Cloud**：全托管，开箱即用
- **GraphQL 技术栈** → **Weaviate**：原生 GraphQL API
- **Rust 技术栈 + 极致性能** → **Qdrant**：Rust 编写，高并发

## 相关文章

- **向量数据库全面解析：从原理到选型**：[CSDN](https://blog.csdn.net/u014354882/article/details/159767868)
