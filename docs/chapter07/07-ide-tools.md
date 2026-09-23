# 七、编程工具 IDE

[← 上一章：六、MCP](../chapter06/06-mcp.md) | [返回总览](../index.md) | [下一章：八、Agent 框架 →](../chapter08/08-agent-frameworks.md)

## 先搞清楚：IDE、Agent CLI、ADE 是三件事

2025 年之前，"AI 编程工具"基本等于"编辑器插件"——你打字，它补全。这个前提在 2026 年已经不再成立：**入口从"编辑器"换成了"agent"**。同一件事因此分化出三种形态，按「你把多少控制权交出去」从少到多排列：

| 形态 | 中心是什么 | 你是怎么用的 | 代表工具 | 在哪一章 |
| --- | --- | --- | --- | --- |
| **AI IDE** | 编辑器 | 你逐步操纵，agent 在编辑会话里当加速器 | Cursor、TraeCode、Antigravity | 本章 |
| **Agent CLI** | 终端 | 你委派一个任务，它自己读码、改码、跑测试并自验 | Claude Code、Codex CLI、OpenCode | [章节四](../chapter04/04-cli-tools.md) |
| **ADE** | agent | 你甩出一个目标，调度 N 个 agent 并行推进 | ZCode、JetBrains Air、Warp | 本章 |

**ADE**（Agentic Development Environment，智能体开发环境）是 2026 年的新品类词。它与 AI IDE 最本质的区别是**没有传统编辑器**：文件树、终端、Git 面板、浏览器预览都降级成 agent 调用的工具，你的主界面变成一个任务（Goal）和它的执行过程。JetBrains 在发布 Air 时把这层意思讲得很直白——"整个软件开发系统能集中在一个窗口里的时代即将结束"。

> ⚠️ **一个容易混淆的点**：ADE 这个词在 2026 年有两个含义。Letta 最早用它指"用来开发和调试 agent 本身的平台"，而现在开发工具圈普遍用来指"用 agent 造软件的工作台"。本章及绝大多数语境说的都是后者。

## IDE / 编辑器类

| 工具                                                      | 形态          | 特点                                                   | 最新情况                                                     |
| --------------------------------------------------------- | ------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **[Cursor](https://www.cursor.com/)**                     | AI 原生 IDE   | 基于 VSCode，AI 编程新宠儿，Composer 模式、Agent 模式  | 归属 **Anysphere**（**2026-08-14 起为 SpaceX 全资子公司**）；版本约 **3.21.x**（2026-09），持续强化 Agent 模式和 MCP 集成能力 |
| **[Devin Desktop](https://devin.ai/desktop)**（原 Windsurf） | AI 原生 IDE   | **Cognition** 出品（Devin 母公司），流畅的 AI 协作体验 | **2026-06-02 由 Windsurf 更名**，原域名 `windsurf.com` 已 301 跳转至 `devin.ai/desktop`；本地 Agent 由 Cascade 改为 **Devin Local**（Rust 重写） |
| **[Antigravity](https://antigravity.google/)**            | Google AI IDE | 基于 VS Code 构建，Agent-first 设计                     | 已 **GA（正式可用）**。个人档 **$0/月**：不限量 Tab 补全与命令请求 + 每周基础 agent 额度，可选模型含 Gemini 3 系列 Flash、Gemini 3.1 Pro，另可调 Claude Sonnet/Opus 4.6 与 gpt-oss-120b；付费走 Google AI Pro（$19.99/月）与 Ultra（$99.99 / $199.99）。**Antigravity 2.0 已从 IDE 转为「命令中心」**，专门并行管理多个本地 agent，另有 CLI 与 SDK 入口；企业版经 Gemini Enterprise 提供。社区生态：[antigravity-skills](https://github.com/rmyndharis/antigravity-skills)、[配额监控插件](https://github.com/jlcodes99/vscode-antigravity-cockpit) |
| **[TraeCode](https://www.trae.ai/)**（原 TRAE IDE）        | 字节 AI IDE   | 基础版免费，中文指令理解精准度高                       | **已更名为 TraeCode**，IDE 模式与 **SOLO 模式**（AI 主导规划与执行）并存；原先的办公能力已拆分为独立产品 **TraeWork**（AI 原生工作台，网页 / 桌面 / 移动三端，Work / Code / Design 三模式） |
| **[GitHub Copilot](https://github.com/features/copilot)** | 微软 IDE 插件 | 微软生态的智能编码标配                                 |                                                              |
| **[Visual Studio 2026](https://visualstudio.microsoft.com/)** | 微软 IDE      | .NET / C++ 主力 IDE，Fluent UI 重做，性能大幅提升      | **2025-11-11 正式发布**（与 .NET 10 LTS 同期）；**GitHub Copilot 免费内置**（Copilot Free 每月 2,000 次补全 + 50 次高级请求，超出后回落到 IntelliCode）；内置 Profiler Agent、Debugger Agent（自动分析失败单测并给出修复）与 C#/C++ 专用 agent，可装 VS 2022 扩展 |
| **[CodeBuddy](https://codebuddy.cn/)**                    | 腾讯 全栈 IDE | 混元+DeepSeek 双引擎，Plan-Coding-Deploy 三 Agent 协同 |                                                              |

## ADE（Agent-first 开发环境）

这一类是 2026 年新出现的，共同特征是**没有传统编辑器**、以任务（Goal）为单位、原生支持多个 agent 并行。

| 工具 | 厂商 | 特点 | 最新情况 |
| --- | --- | --- | --- |
| **[ZCode](https://z.ai/)** | 智谱 Z.ai | Agent-first 的 ADE，由 GLM 系列驱动 | 国内名 **Z Code**，2025-12-26 首发；**2026-07-02 Z.ai 发布 ADE 版并登顶 Hacker News**；内核已适配 **GLM-5.3-Flash**；支持 BYOK 接入 GPT / Claude / Gemini 等。⚠️ **2026-09-18 就"代码库数据上传"公开致歉并宣布将开源代码库**，企业采用建议等开源后再评估 |
| **[JetBrains Air](https://www.jetbrains.com/air/)** | JetBrains | 把 JetBrains 六个月来围绕 agentic 开发的工作整合成一套产品体系 | **2026-09-22 发布**。含 Air in IDEs（IDE 内插件）、Air Teams（团队云端协作）、Air Governance（原 JetBrains Central，治理与成本）、Air Context（语义索引）、Air Gateway（把终端 agent 接进来）。坚持**多供应商**：可接 Claude Agent、Codex、Copilot、OpenCode、Junie，以及任何实现 **ACP**（Agent Client Protocol，JetBrains 与 Zed 共同制定）的 agent |
| **[Warp](https://www.warp.dev/)** | Warp | 从终端起家的 ADE，配云端编排平台 **Oz** | **2026-04-28 开源**核心产品（65K star），并提出"Open Agentic Development"模式：非技术用户提需求，agent 在公开仓库里实现并提交 PR。Oz 可把 **Claude Code、Codex、Warp Agent 并排跑在同一控制面**（2026-05-19），带跨 harness 持久记忆、自动多 agent 编排、企业级权限与成本上限 |
| **[Emdash](https://github.com/generalaction/emdash)** | 开源（YC W26，MIT） | 桌面端多 agent 编排，用 **git worktree** 给每个 agent 隔离工作目录 | 可接入 **31+ 种 CLI agent**（Claude Code、Codex、Gemini CLI、OpenCode、Cline、Droid 等），支持 SSH 远程跑长任务（5.8K star） |

> **为什么必须用 git worktree 隔离**：多个 agent 同时改同一份代码会互相覆盖。给每个 agent 一个独立 worktree（各自一个目录、共享同一份 `.git`），跑完再用 diff 视图挑最优结果合并——这是 2026 年"多 agent 并行"能真正落地的前提，也是 ADE 这个品类成立的技术基础。

> **延伸：ADE 是"编程向的 agent 工作台"**。同一思路用在办公场景，就是 AI 原生工作台——字节 **TraeWork**、腾讯 **WorkBuddy**、月之暗面 **Kimi Work**，形态与 ADE 高度相似，区别只是产物从代码换成了文档、表格与自动化流程。

## Web / 浏览器类

| 工具                                  | 特点                       |
| ----------------------------------- | ------------------------ |
| **[Bolt.new](https://bolt.new/)**   | 浏览器中构建全栈应用，StackBlitz 出品 |
| **[V0 by Vercel](https://v0.dev/)** | 从文本描述生成 React 组件/UI      |
| **[Replit](https://replit.com/)**   | 浏览器端编码、运行、部署一体化          |

## 各工具核心体验

### Cursor

**核心模式**：
- **Tab 补全**：编辑时自动建议，按 Tab 接受，与 Copilot 类似但更激进
- **Composer**：多文件同时编辑，AI 理解项目上下文后跨文件生成代码
- **Agent 模式**：自主执行多步操作——读写文件、运行命令、调用 MCP 工具

**适合**：中大型项目的主力开发，需要 AI 深度理解代码库的场景

**注意事项**：付费工具，Pro 版 20 美元/月（Pro+ 60 / Ultra 200 / Teams 40 美元每席）；首次打开项目需建立索引，大型代码库等待较久

### Devin Desktop（原 Windsurf）

**核心模式**：
- **Devin Local**：本地 Agent（Rust 重写），流畅的 AI 对话流，可在对话中逐步修改代码
- **内联编辑**：选中代码后直接用自然语言修改

**适合**：偏好流畅对话体验的开发者，对 AI 编程的"手感"有要求

### TraeCode（原 TRAE IDE）

**核心模式**：
- **IDE 模式**：保留编辑器、终端、调试、Git 传统工作流，你精细掌控每一步
- **SOLO 模式**：AI 主导任务的规划与执行，你只描述需求

**适合**：零成本入门 AI 编程，中文场景优先，需要从需求到预览完整跑通的开发者

**注意事项**：基础版免费，深度绑定豆包大模型；相比 Cursor 功能成熟度略低。

> 如果你的目标**不是写代码**（写方案、做分析、推协作），该用的是同门的 **TraeWork**，而不是 TraeCode 的 SOLO 模式——字节已经把这两条线拆开了。

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

### ZCode（ADE）

**核心模式**：
- **Goal（目标）**：一次设定多步开发目标，agent 自行规划、改码、跑测试、迭代验证，中途不必逐步确认
- **远程触发**：可从微信、飞书、Telegram 下发任务，高危操作（写敏感目录、提交 Git）仍需桌面端确认
- **BYOK**：界面用 ZCode 的，模型可换成 GPT、Claude、Gemini 或任意 OpenAI 兼容端点

**适合**：愿意放弃传统编辑器、把整个开发流程交给 agent 的开发者和团队

**注意事项**：2026-09-18 就"代码库数据上传"问题公开致歉并承诺开源，**企业采用建议等代码库真正开源后再评估**

### JetBrains Air（ADE）

**核心模式**：
- **多 agent 编排**：在 JetBrains IDE 内指导并验证 agent 的工作，同时跟踪多个项目的会话、改动文件与待推送提交
- **一键接入**：自动发现本机已装的 agent，也可从 agent registry 添加新的
- **多供应商**：不强制使用 JetBrains 自家 Junie，Claude Agent / Codex / Copilot / OpenCode 均可接

**适合**：已在用 IntelliJ IDEA / PyCharm 等 JetBrains IDE，又想上多 agent 协作的开发者与团队

**注意事项**：2026-09-22 才发布，Air Teams 仍处早期访问，云端运行正在分批开放

### Warp（ADE）

**核心模式**：
- **任意 agent 混用**：同一界面里跑 Claude Code、Codex、Warp Agent，可用垂直标签与通知并行管理多个会话
- **本地到云端无缝交接**：终端里起任务，需要长时间跑就交给 Oz 云端继续
- **可配置界面**：从纯终端，到极简 agent 视图（diff + 文件树），再到完整 ADE，同一产品三种形态

**适合**：习惯终端、同时用多个 agent、且需要企业级可观测性的团队

## Web 工具适用场景

| 场景 | 推荐工具 | 理由 |
|------|---------|------|
| 快速出原型/演示 | Bolt.new | 零配置，浏览器直接出全栈应用 |
| UI/前端组件生成 | V0 | 文本描述 → React 组件，设计感强 |
| 线上学习/轻量开发 | Replit | 编码+运行+部署一体化，无需本地环境 |
| 非技术人员做产品 | Bolt.new + Vercel | 自然语言出应用，一键上线 |

> **提示**：Web 工具适合快速验证想法，项目变大后建议导出代码到 Cursor/Claude Code 继续迭代（参考章节十二 Vibe Coding → Spec Coding 切换）。

## IDE 选型对比

| 工具 | 形态 | 免费 | 核心模型 | Agent 能力 | MCP 支持 | 中文体验 | 适用场景 |
|------|------|------|---------|-----------|---------|---------|---------|
| Cursor | AI IDE | 付费 | 多模型可选 | Composer+Agent | 支持 | 良 | 专业开发，大型项目 |
| Devin Desktop | AI IDE | 付费 | 多模型可选 | Devin Local | 支持 | 良 | 流畅协作体验 |
| Antigravity | AI IDE | **$0 个人档** | Gemini 3 系列 + Claude | Agent-first；2.0 并行多 agent | 支持 | 良 | Google 生态，零成本起步 |
| TraeCode | AI IDE | 基础版免费 | 豆包大模型 | IDE + SOLO 双模式 | 支持 | 优 | 中文优先，零成本入门 |
| Visual Studio 2026 | 传统 IDE | 内置 Copilot Free | GPT-5 / Claude | Profiler / Debugger Agent | 支持 | 优 | .NET / C++ 团队 |
| Copilot | IDE 插件 | 付费 | GPT-5/Claude | Agent 模式 | 支持 | 良 | VS Code/JetBrains 用户 |
| CodeBuddy | 全栈 IDE | — | 混元+DeepSeek | Plan-Code-Deploy | 支持 | 优 | 腾讯生态，全流程 |
| **ZCode** | **ADE** | 免费下载 | GLM-5.3 | Goal 驱动，全流程自主 | 支持 | 优 | 放弃编辑器，把流程交给 agent |
| **JetBrains Air** | **ADE** | 自带订阅可用 | 多供应商 | 多 agent 编排 + 治理 | 支持 | 中 | JetBrains 用户，团队协作 |
| **Warp** | **ADE** | 免费下载 | 多模型可选 | Oz 云端编排，多 harness 并行 | 支持 | 良 | 终端党，多 agent 混用 |

## 选型建议

- **主力开发工具** → **Cursor** 或 **Devin Desktop（原 Windsurf）**：成熟 AI IDE，Agent 能力强，适合日常开发
- **零成本入门** → **TraeCode**（基础免费）+ **Antigravity**（个人档 $0）+ **CodeBuddy**：中文体验好，且都有免费档
- **已有 IDE 不想换** → **GitHub Copilot** / **Visual Studio 2026**：插件或内置形式，无缝集成现有工作流
- **Web 快速原型** → **Bolt.new** / **V0**：浏览器端零配置，秒出原型
- **全栈部署** → **Replit**：编码+运行+部署一体化
- **中文优先 + 国产模型** → **TraeCode** / **CodeBuddy**：中文理解精准，豆包 / 混元深度适配
- **不想逐步操作，只想给一个目标** → **ZCode** / **Warp**：ADE 形态，你出 Goal，agent 跑完整个流程
- **团队要多 agent 并行 + 治理** → **JetBrains Air** / **Warp Oz**：多 agent 编排 + 权限与成本控制
- **办公自动化（不写代码）** → **TraeWork** / **WorkBuddy** / **Kimi Work**：AI 原生工作台，产物是文档、数据与自动化流程

## 从零开始选工具

```
你的情况？
 ├── 已有 VS Code 工作流，不想换 → Copilot 插件
 ├── 愿意尝试新 IDE，追求最强 AI 能力 → Cursor
 ├── 预算有限 / 先体验 → TraeCode（基础免费）/ Antigravity（个人档 $0）
 ├── 只做原型验证，不想装软件 → Bolt.new（浏览器）
 ├── 不想逐步操作，只想给一个目标 → ZCode / Warp（ADE）
 └── 目标不是写代码，而是产出文档 / 数据 → TraeWork / Kimi Work（AI 工作台）

项目变大后？
 ├── Web 工具 → 导出代码 → Cursor / Claude Code 迭代
 └── 单个 agent 不够用 → 上 ADE（JetBrains Air / Warp Oz）做多 agent 编排

代码必须自托管 / 有合规要求？
 └── 优先开源 ADE（Warp、Emdash）+ 开源权重模型（GLM、Kimi、Qwen）
```

## 相关文章

- **[2026 年 AI IDE 终极对比：Cursor vs Windsurf vs Trae](https://zhuanlan.zhihu.com/p/2020879714030540578)**（原文标题；Windsurf 现名 **Devin Desktop**，TRAE IDE 现名 **TraeCode**）
- **[Cursor 从入门到精通](https://cursor.directory/)**
- **[AI IDE 对比评测](https://www.bilibili.com/video/BV1xx411c7mD/)**
- **[JetBrains Air 官方产品页](https://www.jetbrains.com/air/)**（2026-09-22 发布的 ADE 产品体系）
- **[Warp 官方站](https://www.warp.dev/)**（开源 ADE + Oz 云端 agent 编排）
- **[Emdash](https://github.com/generalaction/emdash)**（开源多 agent 编排，31+ 种 CLI agent）
