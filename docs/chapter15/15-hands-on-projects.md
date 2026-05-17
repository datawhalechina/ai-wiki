# 十五、端到端实战项目

[← 上一章：十四、Prompt Engineering](../chapter14/14-prompt-engineering.md) | [返回总览](../index.md)]

学完各章节的工具和概念后，最重要的是把它们串起来。以下三个实战项目覆盖最常见的 AI 开发场景，每个项目都标注了前置章节、所需工具和关键步骤。

## 实战一：30 分钟搭建 RAG 知识库问答

**目标**：上传一份 PDF 文档，实现基于文档内容的精准问答。

**前置章节**：模型 API(3) → Embedding(11) → 向量库(10) → RAG 框架(9)

**所需工具**：
- LLM API：DeepSeek / Qwen3（成本低，中文好）
- Embedding：BGE 系列（开源，中文优）
- 向量库：Chroma（零配置，适合原型）
- RAG 框架：RAGFlow（深度文档解析）或 LlamaIndex（灵活编排）

**步骤**：

```
1. 准备文档
   └── 将 PDF/Markdown 放入 data/ 目录

2. 文档切分 + Embedding
   └── 加载文档 → 按段落/512 token 切分 → 调用 BGE 生成向量
   └── 关键：chunk 大小影响检索精度，建议 256-512 token，overlap 50 token

3. 存入向量库
   └── Chroma 一行代码写入：collection.add(documents, embeddings, ids)

4. 检索 + 生成
   └── 用户提问 → Embedding → 向量检索 top-5 → 拼接 prompt → LLM 生成回答

5. 验证效果
   └── 准备 10 个测试问题，检查：回答是否基于文档？是否遗漏关键信息？
   └── 常见问题：chunk 太大导致噪声多、Embedding 模型不匹配中文、检索 top-k 太少
```

**最小可运行代码（LlamaIndex + Chroma + BGE）**：

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

# 1. 设置 Embedding 模型
Settings.embed_model = HuggingFaceEmbedding("BAAI/bge-small-zh-v1.5")

# 2. 加载文档
documents = SimpleDirectoryReader("data/").load_data()

# 3. 创建向量库并索引
db = chromadb.PersistentClient(path="./chroma_db")
chroma_store = ChromaVectorStore(chroma_collection=db.get_or_create_collection("docs"))
index = VectorStoreIndex.from_documents(documents, vector_store=chroma_store)

# 4. 查询
query_engine = index.as_query_engine(similarity_top_k=5)
response = query_engine.query("文档中关于XXX的关键结论是什么？")
print(response)
```

**进阶方向**：
- 换用 RAGFlow 获得更好的 PDF 表格解析
- 加入 reranker（如 bge-reranker）对检索结果重排序
- 尝试 Agentic RAG（章节九），让 Agent 自主判断检索次数

---

## 实战二：5 分钟写一个 MCP Server + Agent 调用

**目标**：用 FastMCP 创建一个自定义 MCP Server，让 Claude Code / OpenClaw 调用它。

**前置章节**：MCP(6) → Agent 框架(8) → Skill(5)

**所需工具**：
- MCP 框架：FastMCP（Python 一行装饰器）
- MCP Client：Claude Code / OpenClaw / 任意支持 MCP 的客户端

**步骤**：

```
1. 安装 FastMCP
   └── pip install fastmcp

2. 编写 MCP Server（weather_server.py）
   └── 定义工具：get_weather(city) → 返回天气信息
   └── 关键：@mcp.tool() 装饰器即可把函数变成 MCP 工具

3. 启动 MCP Server
   └── fastmcp run weather_server.py

4. 在客户端配置
   └── Claude Code: 在 .claude/settings.json 的 mcpServers 中添加
   └── OpenClaw: 在 .mcp.json 中添加

5. 测试调用
   └── 在 Claude Code 中输入"查一下北京天气"
   └── Agent 会自动调用你的 MCP Server 获取数据
```

**最小可运行代码（FastMCP）**：

```python
from fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    # 实际项目中替换为真实 API 调用
    weather_data = {
        "北京": "晴，25°C，北风3级",
        "上海": "多云，22°C，东风2级",
        "深圳": "阵雨，28°C，南风4级",
    }
    return weather_data.get(city, f"未找到{city}的天气数据")

if __name__ == "__main__":
    mcp.run()
```

**客户端配置示例（Claude Code）**：

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["weather_server.py"],
      "cwd": "/path/to/server"
    }
  }
}
```

**进阶方向**：
- 接入真实 API（和风天气、OpenWeatherMap）
- 添加资源（@mcp.resource）和提示（@mcp.prompt）
- 用 Streamable HTTP 部署为远程 MCP Server

---

## 实战三：Vibe Coding 一小时做出 MVP

**目标**：从零用 AI 生成一个可运行的 Web 应用。

**前置章节**：Vibe Coding(12) → CLI(4) → IDE(7)

**所需工具**：
- 方案 A：Bolt.new（零配置，浏览器直接出）+ Vercel 部署
- 方案 B：Cursor Agent 模式 + Claude Code 辅助

**步骤（方案 A：Bolt.new）**：

```
1. 打开 bolt.new，用自然语言描述需求
   └── 示例："做一个待办事项应用，支持添加、删除、标记完成，数据存 localStorage"

2. AI 生成代码，浏览器中预览
   └── 不满意？直接对话修改："把颜色改成蓝色主题"、"加一个筛选已完成的功能"

3. 满意后点 Deploy，一键上线
   └── 获得一个可分享的 URL

4. 导出代码到本地，用 Cursor 继续迭代
   └── 从 Vibe Coding 切换到 Spec Coding
```

**步骤（方案 B：Claude Code + Cursor）**：

```
1. 初始化项目
   └── claude "创建一个 Next.js 项目，包含首页和 API 路由"

2. Vibe Coding 阶段
   └── claude "加一个用户登录页面，用 Tailwind 样式"
   └── claude "API 接口加 JWT 认证"
   └── 边做边改，快速出原型

3. 项目变大后切换 Spec Coding
   └── 先写 PRD.md："本应用包含 X 个模块，每个模块的输入输出是..."
   └── claude "按照 PRD.md 实现用户模块"

4. 上线前加 Harness
   └── claude "给登录和 API 写单元测试"
   └── claude "做一次 CodeReview，检查安全问题"
```

**关键原则**：
- **先跑通，再优化**：Vibe Coding 阶段不要纠结代码质量
- **及时切换范式**：原型验证后，立即用 Spec 或 Harness 约束 AI 输出
- **小步提交**：每完成一个功能就 git commit，避免 AI 生成大量不可控代码

---

## 实战项目与章节对照

| 实战项目 | 核心章节 | 关键概念 | 预计耗时 |
|---------|---------|---------|---------|
| RAG 知识库问答 | 3+9+10+11 | Embedding、向量检索、RAG 管线 | 30-60 分钟 |
| MCP Server + Agent | 6+8+5 | MCP 协议、工具调用、Skill | 5-15 分钟 |
| Vibe Coding MVP | 12+4+7 | AI 编程范式、工具选择 | 1-2 小时 |
