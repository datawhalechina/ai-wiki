# 七、编程工具 IDE

[← 上一章：六、MCP](../chapter06/06-mcp.md) | [返回总览](../index.md) | [下一章：八、Agent 框架 →](../chapter08/08-agent-frameworks.md)

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

