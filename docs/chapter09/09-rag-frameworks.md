# 九、RAG 框架

[← 上一章：八、Agent 框架](../chapter08/08-agent-frameworks.md) | [返回总览](../index.md) | [下一章：十、向量知识库 →](../chapter10/10-vector-databases.md)

RAG（检索增强生成）框架。2026 年的趋势是向 Agentic RAG 和上下文工程演进。

## 主流 RAG 框架

| 框架                                                         | 特点                        |
| ---------------------------------------------------------- | ------------------------- |
| **[RAGFlow](https://ragflow.io/)**                         | 企业级知识处理引擎，深度文档解析，表格识别能力强  |
| **[LlamaIndex](https://github.com/run-llama/llama_index)** | 数据框架，RAG 核心工具，支持 Agent 集成 |
| **[LangChain](https://www.langchain.com/)**                | RAG 基础组件丰富，生态最大           |
| **[Haystack](https://haystack.deepset.ai/)**               | deepset 出品，模块化 RAG 管线，支持主流向量库和 LLM |
| **[FastGPT](https://fastgpt.cn/)**                         | 高速内容生成专家，轻量易用             |

## RAG 框架选型对比

| 框架 | 文档解析 | 企业级 | 部署 | 学习曲线 | 适用规模 | 典型场景 |
|------|---------|--------|------|---------|---------|---------|
| RAGFlow | 极强（深度文档解析、表格识别） | 是 | 自托管/云 | 中 | 大 | 非结构化文档、表格密集型 |
| LlamaIndex | 强 | 是 | 自托管 | 中 | 大 | 数据框架、Agent 集成 |
| LangChain | 强（组件丰富） | 是 | 自托管 | 中 | 大 | 生态最大，需要灵活组合 |
| Haystack | 强（模块化管线） | 是 | 自托管 | 中 | 中-大 | 模块化 RAG 管线，向量库自由切换 |
| FastGPT | 中 | 否 | 自托管 | 低 | 中小 | 快速搭建知识库问答 |

## 选型路径

- **快速验证** → **FastGPT**：小时级上线知识库问答
- **文档密集型（PDF/表格）** → **RAGFlow**：深度文档解析能力最强
- **需要灵活编排 + Agent 集成** → **LlamaIndex** / **LangChain**
- **模块化切换向量库和 LLM** → **Haystack**
- **企业私有化部署** → **RAGFlow** / **Dify**（低代码，可私有部署）

## RAG 演进方向

- **GraphRAG**：结合知识图谱提升检索精度
- **Agentic RAG**：Agent 驱动的动态检索
- **多模态 RAG**：支持图像、表格等多类型数据
- **上下文工程**：从简单检索到智能上下文编排
