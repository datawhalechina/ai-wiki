# 七、编程工具 IDE

[← 上一章：六、MCP](../chapter06/06-mcp.md) | [返回总览](../index.md) | [下一章：八、Agent 框架 →](../chapter08/08-agent-frameworks.md)]

## IDE / 编辑器类

| 工具                                                      | 类型          | 特点                                                   | 最新情况                                                     |
| --------------------------------------------------------- | ------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **[Cursor](https://www.cursor.com/)**                     | AI 原生 IDE   | 基于 VSCode，AI 编程新宠儿，Composer 模式、Agent 模式  | **Cursor已更新至3.1.x版本**，持续强化 Agent 模式和 MCP 集成能力 |
| **[Windsurf](https://www.windsurf.com/)**                 | AI 原生 IDE   | Codeium 出品，流畅的 AI 协作体验                       |                                                              |
| **[Antigravity](https://antigravity.google/)**            | AI 原生 IDE   | Google出品                                             | 基于 VS Code 构建，Agent-first 设计，使用 Gemini 3 模型；已有社区 Skills 生态（[antigravity-skills](https://github.com/rmyndharis/antigravity-skills)）和配额监控插件（[vscode-antigravity-cockpit](https://github.com/jlcodes99/vscode-antigravity-cockpit)） |
| **[Trae](https://www.trae.ai/)**                          | 字节 AI IDE   | 基础版免费，中文指令理解精准度高                       | 已升级为 **TRAE SOLO**，定位从 AI IDE 扩展为"More Than Coding"跨平台 AI 协作平台（Desktop + App + Web） |
| **[GitHub Copilot](https://github.com/features/copilot)** | 微软 IDE 插件 | 微软生态的智能编码标配                                 |                                                              |
| **[CodeBuddy](https://codebuddy.cn/)**                    | 腾讯 全栈 IDE | 混元+DeepSeek 双引擎，Plan-Coding-Deploy 三 Agent 协同 |                                                              |

## Web / 浏览器类

| 工具                                  | 特点                       |
| ----------------------------------- | ------------------------ |
| **[Bolt.new](https://bolt.new/)**   | 浏览器中构建全栈应用，StackBlitz 出品 |
| **[V0 by Vercel](https://v0.dev/)** | 从文本描述生成 React 组件/UI      |
| **[Replit](https://replit.com/)**   | 浏览器端编码、运行、部署一体化          |

## 各 IDE 核心体验

### Cursor

**核心模式**：
- **Tab 补全**：编辑时自动建议，按 Tab 接受，与 Copilot 类似但更激进
- **Composer**：多文件同时编辑，AI 理解项目上下文后跨文件生成代码
- **Agent 模式**：自主执行多步操作——读写文件、运行命令、调用 MCP 工具

**适合**：中大型项目的主力开发，需要 AI 深度理解代码库的场景

**注意事项**：付费工具，Pro 版 20 美元/月；首次打开项目需建立索引，大型代码库等待较久

### Windsurf

**核心模式**：
- **Cascade**：流畅的 AI 对话流，可在对话中逐步修改代码
- **内联编辑**：选中代码后直接用自然语言修改

**适合**：偏好流畅对话体验的开发者，对 AI 编程的"手感"有要求

### Trae (SOLO)

**核心模式**：
- **SOLO 模式**：跨平台 AI 协作（Desktop + App + Web），不限于编码
- **Builder 模式**：从自然语言描述生成完整项目

**适合**：零成本入门 AI 编程，中文场景优先，想用 AI 做更多事（不只是写代码）

**注意事项**：基础版免费，深度绑定豆包大模型；相比 Cursor 功能成熟度略低

### GitHub Copilot

**核心模式**：
- **内联建议**：编码时实时补全
- **Copilot Chat**：侧栏对话，支持 @workspace 引用项目上下文
- **Agent 模式**：VS Code 内自主执行多步操作

**适合**：已有 VS Code / JetBrains 工作流，不想换 IDE 的开发者

**注意事项**：需要 GitHub 订阅；作为插件，深度项目理解能力不如 AI 原生 IDE

### CodeBuddy

**核心模式**：
- **Plan Agent**：分析需求，生成开发计划
- **Coding Agent**：按计划逐步实现
- **Deploy Agent**：一键部署

**适合**：腾讯生态用户，想从规划到部署一站式完成的开发者

## Web 工具适用场景

| 场景 | 推荐工具 | 理由 |
|------|---------|------|
| 快速出原型/演示 | Bolt.new | 零配置，浏览器直接出全栈应用 |
| UI/前端组件生成 | V0 | 文本描述 → React 组件，设计感强 |
| 线上学习/轻量开发 | Replit | 编码+运行+部署一体化，无需本地环境 |
| 非技术人员做产品 | Bolt.new + Vercel | 自然语言出应用，一键上线 |

> **提示**：Web 工具适合快速验证想法，项目变大后建议导出代码到 Cursor/Claude Code 继续迭代（参考章节十二 Vibe Coding → Spec Coding 切换）。

## IDE 选型对比

| 工具 | 类型 | 免费 | 核心模型 | Agent 能力 | MCP 支持 | 中文体验 | 适用场景 |
|------|------|------|---------|-----------|---------|---------|---------|
| Cursor | AI IDE | 付费 | 多模型可选 | Composer+Agent | 支持 | 良 | 专业开发，大型项目 |
| Windsurf | AI IDE | 付费 | 多模型可选 | Cascade 模式 | 支持 | 良 | 流畅协作体验 |
| Antigravity | AI IDE | — | Gemini 3 | Agent-first | 社区支持 | — | Google 生态，社区 Skills |
| Trae (SOLO) | AI IDE | 基础版免费 | 豆包大模型 | SOLO 模式 | 支持 | 优 | 中文优先，零成本入门，跨平台 |
| Copilot | IDE 插件 | 付费 | GPT-5/Claude | Agent 模式 | 支持 | 良 | VS Code/JetBrains 用户 |
| CodeBuddy | 全栈 IDE | — | 混元+DeepSeek | Plan-Code-Deploy | 支持 | 优 | 腾讯生态，全流程 |

## 选型建议

- **主力开发工具** → **Cursor** 或 **Windsurf**：成熟 AI IDE，Agent 能力强，适合日常开发
- **零成本入门** → **Trae**（基础免费）+ **CodeBuddy**：中文体验好，适合学习和小项目
- **已有 IDE 不想换** → **GitHub Copilot**：插件形式，无缝集成现有工作流
- **Web 快速原型** → **Bolt.new** / **V0**：浏览器端零配置，秒出原型
- **全栈部署** → **Replit**：编码+运行+部署一体化
- **中文优先 + 跨平台** → **Trae SOLO**：桌面端 + 移动端 + Web 端，中文理解精准

## 从零开始选 IDE 的路径

```
你的情况？
 ├── 已有 VS Code 工作流，不想换 → Copilot 插件
 ├── 愿意尝试新 IDE，追求最强 AI 能力 → Cursor
 ├── 预算有限 / 先体验 → Trae（免费）
 └── 只做原型验证，不想装软件 → Bolt.new（浏览器）

项目变大后？
 └── Web 工具 → 导出代码 → Cursor / Claude Code 迭代
```

## 相关文章

- **[2026 年 AI IDE 终极对比：Cursor vs Windsurf vs Trae](https://zhuanlan.zhihu.com/p/2020879714030540578)**
- **[Cursor 从入门到精通](https://cursor.directory/)**
- **[AI IDE 对比评测](https://www.bilibili.com/video/BV1xx411c7mD/)**
