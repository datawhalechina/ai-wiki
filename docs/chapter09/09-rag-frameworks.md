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

### GraphRAG

GraphRAG 在传统向量检索之上叠加知识图谱层，通过实体-关系抽取构建结构化语义网络，解决"片段式检索看不到全局关联"的问题。

**核心流程：**
```
文档 → 实体/关系抽取（LLM） → 知识图谱构建 → 图遍历 + 向量混合检索 → 生成
```

**代表项目：**
- **[Microsoft GraphRAG](https://github.com/microsoft/graphrag)**（23K+ star）：微软开源，自动构建实体知识图谱，支持全局摘要（Global Search）和局部检索（Local Search）两种模式
- **[Neo4j + LLM](https://neo4j.com/)**：图数据库原生集成，适合已有 Neo4j 基础设施的企业
- **[LightRAG](https://github.com/HKUDS/LightRAG)**：港大出品，轻量级 GraphRAG，成本更低

**典型实践案例：**

| 场景 | 为什么用 GraphRAG | 效果 |
|------|-------------------|------|
| 法律判例检索 | 法条之间相互引用，向量检索容易遗漏关联先例 | 图遍历可沿引用链追溯，召回率提升 30%+ |
| 医药文献分析 | 药物-靶点-疾病三者构成天然图结构 | 发现跨文献的间接关联，辅助药物重定位 |
| 企业制度问答 | 制度文件之间互相引用、存在层级关系 | 理解"上级制度→下级细则"的层级链 |
| 科研文献综述 | 论文引用网络是天然的知识图谱 | 沿引用链追踪研究脉络，生成结构化综述 |

### Agentic RAG

Agentic RAG 用 Agent 替代固定的检索流水线——Agent 自主判断"该不该查、去哪里查、怎么查、查完够不够"，实现动态多步检索。

**区别于传统 RAG：**

| | 传统 RAG | Agentic RAG |
|------|---------|------------|
| 检索次数 | 一次 | 多轮，直到满足需求 |
| 检索源 | 固定向量库 | 向量库 + Web 搜索 + API + 数据库 |
| 决策主体 | 预设管线 | Agent 自主决策 |
| 失败处理 | 静默返回不完整结果 | 重写查询、换源、自我纠错 |

**典型架构：**
```
用户提问 → Agent 分析意图
              ├── 需要检索？→ 选择检索源（向量库/Web/API）
              │                   → 评估结果质量
              │                   → 不满足？→ 重写查询重试
              └── 信息充足？→ 综合生成回答（含引用来源）
```

**典型实践案例：**

| 场景 | Agent 行为 | 技术栈 |
|------|-----------|--------|
| 竞品分析报告 | 先搜 Web 获最新动态 → 查内部文档补细节 → 交叉验证 → 生成报告 | LangGraph + Tavily + 向量库 |
| 客服工单排查 | 查知识库 → 不够？查历史工单 DB → 还不够？查操作日志 → 给出根因 | LangChain + SQL + 向量库 |
| 学术研究助手 | 检索论文摘要 → 筛选高相关 → 深度阅读全文 → 交叉引用追踪 → 综述 | LlamaIndex + Semantic Scholar API |
| 合规审查 | 检索法规条文 → 比对企业制度 → 标记冲突点 → 生成整改清单 | RAGFlow + 规则引擎 |

**落地建议：**
- 从简单场景起步：先用传统 RAG 跑通，发现"一次检索不够"时再加入 Agent 循环
- 控制检索步数：建议上限 3-5 步，避免 Agent 无限循环消耗 token
- 记录检索链路：每次检索的 query、来源、结果都应可追溯，便于调试和优化

### 多模态 RAG

支持图像、表格、音视频等非文本数据的检索增强生成。

**代表项目：**
- **[ColPali](https://github.com/illuin-tech/colpali)**：视觉语言模型驱动的 PDF 检索，无需 OCR 即可理解文档布局
- **[LlamaIndex 多模态](https://docs.llamaindex.ai/)**：内置多模态索引和检索
- **[RAGFlow 深度文档解析](https://ragflow.io/)**：原生支持表格、图表、扫描件

### 上下文工程

从"丢一段检索结果给 LLM"升级为系统性编排上下文：去噪、排序、压缩、多文档融合，确保每一 token 上下文都有信息量。相关工具：[LangChain Context](https://www.langchain.com/)、[LlamaIndex Ingestion Pipeline](https://docs.llamaindex.ai/)。
