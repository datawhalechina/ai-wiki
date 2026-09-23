# 四、CLI 种类

[← 上一章：三、三方模型（API）](../chapter03/03-model-api.md) | [返回总览](../index.md) | [下一章：五、好用的 Skill →](../chapter05/05-skills.md)

CLI（命令行界面）AI 工具是终端中的 AI 编程助手，支持自然语言驱动开发全流程。

**提示**：开源 CLI 工具生态还在快速演进，建议关注各工具的插件体系和 MCP 集成能力。

## 主流 AI CLI 工具

| 工具                                                         | 厂商      | 特点                                                         |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| **[Claude Code](https://code.claude.com/docs/zh-CN/overview)** | Anthropic | 终端级深度编码助手，2026年最受喜爱的 AI 编码工具（46% 偏好），147.8K GitHub 星标 |
| **[Codex CLI](https://openai.com/codex/)**                   | OpenAI    | 最新 **0.156.1**（2026-09）。出厂默认模型为 **`gpt-6-astra`**（自 0.153.4 起），客户端默认挂在 **Low 推理档**防额度超支（官方建议日常切 medium）；`gpt-6-sol` / `gpt-6-luna` 自 0.156.1 起可在模型选择器中切换，**但都不是默认** |
| **[OpenCode](https://opencode.ai/)**                         | 开源      | 209.6K GitHub 星标                                            |
| **[DSH](https://github.com/deepseek-ai/deepseek-harness)**   | DeepSeek  | 234.1K GitHub 星标。开源 Agent 运行时，主打「一切皆插件」——模型、工具、循环、UI 均可替换重组；**v0.1 开发者预览版，官方明示不可用于生产** |
| **[Pi](https://github.com/earendil-works/pi)**               | Earendil Works | 108.8K GitHub 星标。极简底座——只保留读/写/改文件与跑命令四个工具；支持单会话内跨供应商接力（Claude 做到一半转给 DeepSeek 继续） |
| **[Antigravity CLI](https://antigravity.google/)**           | Google    | 命令名 `agy`，Gemini CLI 的继任者，已全面开放（第三方多标注为 preview，**官方未使用 GA 字样**）。**Gemini CLI 已于 2026-06-18 对免费 / Google AI Pro / Google AI Ultra 用户停止服务**，企业版（Code Assist）不受影响。个人档 **$0/月**，无需信用卡 |
| **[Qoder CLI](https://qoder.com)**                           | Qoder-AI | Agentic Coding Platform，支持 CLI 和 IDE，自主编程模式，CodeReview 能力 |
| **[CodeBuddy](https://codebuddy.cn/)**                       | 腾讯      | 命令行中用自然语言驱动开发全流程                             |

## CLI 模型支持矩阵

CLI 工具最关键的分化点是**能不能换模型**——这直接决定你会不会被单一厂商绑定，以及能否用国内 Coding Plan 降低调用成本：

| 工具 | 默认模型 | 可切换范围 | 自由度 |
|------|---------|-----------|--------|
| **Claude Code** | Anthropic Claude（现役 Opus 5.5） | 原生仅 Anthropic；**可通过 Base URL 指向第三方端点**（阿里云、腾讯云 Coding Plan 均支持此用法） | 中 |
| **Codex CLI** | **`gpt-6-astra`** | `gpt-6-sol`（复杂编码与 agentic 流程）、`gpt-6-luna`（高频轻量任务）；Bedrock 渠道的默认是 Sol | 低（仅 OpenAI） |
| **Antigravity CLI** | Gemini 3.x | Gemini 3.8 / 3.7 / 3.6 Flash、3.1 Pro，以及 **Claude Sonnet 4.6、Claude Opus 4.6、gpt-oss-120b** | 中（**不支持 BYOK**） |
| **OpenCode** | 内置免费模型 | **Go 订阅打包 30 款**：GLM-5.3、Kimi K3、DeepSeek V4.1、MiMo、Qwen3.8、MiniMax M3、Grok 4.7 等 | 极高 |
| **DSH** | 可切换 | 支持**近 40 家**模型提供方，模型/工具/循环/UI 均可替换 | 极高 |
| **Pi** | 可切换 | 多供应商（20+），支持**单会话内跨供应商接力** | 极高 |
| **Qoder CLI** | 多模型 | 多模型支持 | 中 |
| **CodeBuddy** | 混元系 | 混元 + DeepSeek | 低 |

> 💡 **换模型的两种方式**：① 工具内置模型选择器（如 Codex 的 `codex --model gpt-6-sol`）；② 通过 Base URL + API Key 指向第三方端点——这是国内用户把 Claude Code、Cursor 接到 Coding Plan 上的通用做法。

## CLI 工具选型对比

| 工具 | 开源 | 模型灵活度 | MCP 支持 | 社区活跃度 | 学习门槛 | 适用场景 |
|------|------|-----------|---------|-----------|---------|---------|
| Claude Code | 否 | Claude 系列 | 深度集成 | 极高（147.8K star） | 低 | 深度编码、大型项目重构 |
| Codex CLI | 开源 | **`gpt-6-astra` 默认，可切 Sol / Luna** | 支持 | 高 | 低 | OpenAI 生态、多模型切换 |
| OpenCode | 开源 | 多模型自由 | 支持 | 极高（209.6K star） | 中 | 开源优先、社区驱动、自定义工作流 |
| Antigravity CLI | 否 | Gemini + Claude + gpt-oss | 支持 | 中 | 低 | Google 生态、多模态任务、免费档 $0（2026-06 起取代 Gemini CLI） |
| Qoder CLI | 否 | 多模型支持 | 支持 | 中 | 低 | 自主编程、CodeReview、IDE+CLI 双模式 |
| CodeBuddy | 否 | 混元+DeepSeek | 支持 | 中 | 低 | 腾讯生态、全流程开发 |
| DSH | 开源（MIT） | 近 40 家提供方 | 支持 | 高（234.1K star） | 中 | 插件化改造、自定义 agent 运行时（预览版） |
| Pi | 开源（MIT） | 多供应商（20+） | 支持 | 高（108.8K star） | 中 | 极简底座、自建工作流、跨模型接力 |

## 选型建议

- **追求极致编码体验** → **Claude Code**：当前社区偏好度最高（46%），Agent 能力强，适合大型项目
- **开源自由 + 多模型切换** → **OpenCode**：社区最活跃的开源 CLI，可对接任意模型
- **OpenAI 深度用户** → **Codex CLI**：默认 `gpt-6-astra`，需要更强 agentic 能力时切 `gpt-6-sol`，高频轻量任务切 `gpt-6-luna`
- **国内生态优先** → **Qoder CLI**（Agentic Coding）/ **CodeBuddy**（腾讯）：中文优化好，自主编程模式
- **Google 全家桶用户** → **Antigravity CLI（`agy`）**：Gemini CLI 已于 2026-06-18 对个人用户停服，由其继任；个人档 **$0** 且可选 Claude / gpt-oss 模型，与企业版 Code Assist 和 Google Cloud 深度集成
- **想自己拼装 agent 底座** → **DSH**（一切皆插件，模型/工具/循环都可换，但仍是预览版）/ **Pi**（极简四工具底座，适合把 agent 嵌进自己的工作流）

## 5 分钟快速上手：Claude Code

```bash
# 1. 安装
npm install -g @anthropic-ai/claude-code

# 2. 启动（首次运行需登录 Anthropic 账号）
claude

# 3. 第一个命令：让 AI 帮你创建项目
> 帮我创建一个 Python FastAPI 项目，包含健康检查接口

# 4. 常用操作
> 读取 main.py 并解释它的功能       # 理解代码
> 给这个项目加一个用户登录接口       # 增加功能
> 运行测试并修复所有失败的用例       # 调试修复
> 帮我做一次 CodeReview              # 代码审查
```

**国内用户**：可通过 Coding Plan（章节二）使用阿里云/腾讯云 Token Plan 接入，降低成本。

## 辅助工具

| 工具 | 特点 |
|------|------|
| **[cc-switch](https://github.com/farion1231/cc-switch)**（135.5K star） | 跨平台桌面应用，一键切换 Claude Code / Codex / OpenCode / OpenClaw / Antigravity CLI，免去终端手动切换的繁琐 |

