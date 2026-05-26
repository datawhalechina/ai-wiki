# 十二、Vibe Coding 四种

[← 上一章：十一、Embedding 模型](../chapter11/11-embedding-models.md) | [返回总览](../index.md) | [下一章：十三、资源导航 →](../chapter13/13-resources.md)

Vibe Coding 由 AI 研究员 Andrej Karpathy 于 2025 年 2 月提出，指通过自然语言描述需求让 AI 生成代码，而非手动编写。

## 四种开发者原型（按技术知识与 AI 依赖度分类）

| 原型        | 技术知识 | AI 依赖度 | 核心特征                                     |
| --------- | ---- | ------ | ---------------------------------------- |
| **传统工程师** | 高    | 低      | 全面理解代码库，谨慎使用 AI，聚焦系统完整性，未来将转向架构/安全/系统设计  |
| **增强工程师** | 高    | 高      | 深度依赖 AI 同时保持技术理解，评估和优化 AI 生成方案，将成为主导开发范式 |
| **新兴开发者** | 低    | 低      | 传统方式学习基础，使用基础辅助工具，群体正在缩小                 |
| **领域创造者** | 低    | 高      | 专注问题描述而非实现细节，快速原型，将分化为纯非技术创作者与技术学习者      |

## 四种 AI 编程范式

| 范式                      | 核心思想      | 前置工作    | 适用场景        | 核心优势         |
| ----------------------- | --------- | ------- | ----------- | ------------ |
| **Vibe Coding**         | 灵感驱动，边做边改 | 很少，快速启动 | 创意探索、原型验证   | 最快出结果，抓住灵感   |
| **Spec Coding**         | 先定义，再开发   | 完整规格说明  | 需求明确、模块交付   | AI 容易执行，结果可控 |
| **Glue Coding**         | 复用整合，拼装交付 | 梳理已有模块  | MVP 开发、应用整合 | 最快交付，效率最高    |
| **Harness Engineering** | 质检门禁，返工迭代 | 定义质检标准  | 生产环境、大型项目   | 质量可控，可维护性好  |

## 每种范式的实操案例

### Vibe Coding：灵感驱动

**场景**：周末突然想到一个好点子，想快速验证是否可行

```
你：在 Cursor Agent 模式中输入
"做一个极简的 Markdown 笔记应用，支持实时预览、标签分类、localStorage 存储"

结果：5 分钟内得到一个可运行的单页应用

不满意？继续对话：
"加一个暗色主题切换"
"预览区加上代码高亮"

每次对话都是一次探索，不需要想清楚再动手
```

**关键**：不纠结代码质量，先跑通再说。灵感转瞬即逝，速度优先。

### Spec Coding：先定义再开发

**场景**：需求已明确，要交付一个功能模块

```
第一步：写规格文档（PRD.md）

## 用户登录模块
- 输入：手机号 + 验证码
- 验证：手机号格式校验、验证码 6 位数字、60 秒过期
- 输出：JWT token（有效期 7 天）
- 异常：手机号格式错误 → 400，验证码过期 → 401

第二步：让 AI 按规格实现

你：claude "按照 PRD.md 实现用户登录模块"

AI 输出可预测、可验证，因为规格已经限定了边界
```

**关键**：写规格的时间是值得投入的——规格越清晰，AI 输出越准确，返工越少。

### Glue Coding：复用整合

**场景**：已有多个组件，需要快速拼装一个 MVP

```
你：claude "用以下组件搭建一个知识库问答 MVP：
1. LlamaIndex 做 RAG 检索（见 rag_service.py）
2. FastMCP 暴露为 MCP 工具（见 mcp_server.py）
3. Streamlit 做前端界面

请把它们串起来，确保用户可以在网页端提问，后端调用 RAG 检索并返回答案"

AI 的核心工作不是写新代码，而是理解已有代码并写好"胶水"
```

**关键**：AI 最擅长写连接代码，把现有模块串起来。你提供组件，AI 负责拼装。

### Harness Engineering：质检门禁

**场景**：代码要上线，必须有质量保障

```
第一步：定义质检标准

你：claude "给这个项目加 Harness：
1. 所有 API 端点必须有单元测试，覆盖率 > 80%
2. 运行 npm run lint 无报错
3. 所有用户输入必须校验
4. 无硬编码密钥或凭证
5. 错误处理必须有用户友好提示"

第二步：AI 执行质检并修复

AI 发现问题后自动修复，循环执行直到所有门禁通过
```

**关键**：Harness 不是一次性加的，而是在项目从原型走向生产时逐步建立。

## 何时切换范式

| 信号 | 当前范式 | 应切换到 | 原因 |
|------|---------|---------|------|
| AI 生成代码越来越难维护 | Vibe Coding | Spec Coding | 代码量超出 AI 上下文理解能力 |
| 多次对话修改同一功能仍不满意 | Vibe Coding | Spec Coding | 需求已明确但缺少规格约束 |
| 需要集成 3+ 个已有模块 | 任意 | Glue Coding | 拼装比重写更高效 |
| 项目要上线/多人协作 | Spec/Vibe/Glue | Harness | 生产环境必须有质检门禁 |
| 修复同一个 bug 超过 2 次 | 任意 | Harness | 缺少测试保护导致回归 |
| 需求一句话说不清 | Glue/Harness | Spec | 先理清需求再动手 |

**核心原则**：项目早期用 Vibe，中期切 Spec，上线前加 Harness。同一项目中不同模块可以混合使用。

## 范式与工具映射

不同范式适合不同的工具组合：

| 范式 | 推荐 CLI | 推荐 IDE | 推荐 Skill/工作流 |
|------|---------|---------|----------------|
| Vibe Coding | Claude Code / OpenClaw | Cursor Agent 模式 / Bolt.new | 前端设计、创意生成类 Skill |
| Spec Coding | Claude Code（Plan 模式）| Cursor / Windsurf | skill-creator（生成规格）、doc-coauthoring（文档协作） |
| Glue Coding | OpenClaw（Skills 驱动）| Trae / Replit | mcp-builder（集成外部工具）、API 对接 Skill |
| Harness Engineering | Claude Code（TDD 模式）| Cursor + Copilot | webapp-testing（E2E 测试）、CodeReview Skill |

## 实操建议

- **从 Vibe Coding 入门**：先用 Bolt.new 或 Cursor Agent 模式快速出原型，感受 AI 编程的效率
- **项目变大时切换 Spec Coding**：当 Vibe Coding 产出难以维护时，用 PRD 或规格文档约束 AI 输出
- **生产环境必须上 Harness**：无论哪种范式，上线前都需要测试门禁和 CodeReview
- **混合使用**：同一项目中，核心模块用 Spec/Harness，探索性功能用 Vibe，不必拘泥于单一范式

## 常见问题

**Q：Vibe Coding 写出来的代码质量差怎么办？**
A：这是正常的——Vibe Coding 的目标是"快速验证想法"而非"写出生产级代码"。验证可行后，用 Spec Coding 重写关键模块，再加 Harness 保障质量。

**Q：我该从哪种范式开始？**
A：如果你是新手，从 Vibe Coding 开始——最快出成果，建立信心。如果你已有编程经验，直接从 Spec Coding 开始更高效。

**Q：Glue Coding 和 Vibe Coding 有什么区别？**
A：Vibe Coding 是从零生成代码，Glue Coding 是用已有组件拼装。当你有现成组件时，Glue Coding 远比 Vibe Coding 高效。

## 相关文章

- **[Vibe Coding 是什么？AI 时代 Vibe Coding 深度解析与工具推荐](https://qubittool.com/zh/blog/vibe-coding-complete-guide)**
- **[Vibe Coding 完全指南：从"氛围编程"到 Agentic Engineering](https://zhuanlan.zhihu.com/p/2010879714030540578)**
- **[easy-vibe：Datawhale Vibe Coding 教程](https://datawhalechina.github.io/easy-vibe)**
