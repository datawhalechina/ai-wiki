# 四、CLI 种类

[← 上一章：三、三方模型（API）](../chapter03/03-model-api.md) | [返回总览](../index.md) | [下一章：五、好用的 Skill →](../chapter05/05-skills.md)

CLI（命令行界面）AI 工具是终端中的 AI 编程助手，支持自然语言驱动开发全流程。

**提示**：开源 CLI 工具生态还在快速演进，建议关注各工具的插件体系和 MCP 集成能力。

## 主流 AI CLI 工具

| 工具                                                         | 厂商      | 特点                                                         |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| **[Claude Code](https://code.claude.com/docs/zh-CN/overview)** | Anthropic | 终端级深度编码助手，2026年最受喜爱的 AI 编码工具（46% 偏好），122K+ GitHub 星标 |
| **[Codex CLI](https://openai.com/codex/)**                   | OpenAI    | 根据2026年4月的报道，Codex CLI 已升级至基于 **GPT-5.2-Codex**，甚至有提到在生产环境使用 GPT-5 级别模型以提供极高编码能力。 |
| **[OpenCode](https://opencode.ai/)**                         | 开源      | 158K+ GitHub 星标                                            |
| **[Gemini CLI](https://geminicli.com/)**                     | Google    | 面向开发者的 AI 命令行工具                                   |
| **[Qoder CLI](https://qoder.com)**                           | 阿里      | 200ms 响应，Quest 自主编程模式，CodeReview 能力              |
| **[CodeBuddy](https://codebuddy.cn/)**                       | 腾讯      | 命令行中用自然语言驱动开发全流程                             |

## CLI 工具选型对比

| 工具 | 开源 | 模型灵活度 | MCP 支持 | 社区活跃度 | 学习门槛 | 适用场景 |
|------|------|-----------|---------|-----------|---------|---------|
| Claude Code | 否 | Claude 系列 | 深度集成 | 极高（122K+ star） | 低 | 深度编码、大型项目重构 |
| Codex CLI | 开源 | GPT-5.2 为主 | 支持 | 高 | 低 | OpenAI 生态、多模型切换 |
| OpenCode | 开源 | 多模型自由 | 支持 | 极高（158K+ star） | 中 | 开源优先、社区驱动、自定义工作流 |
| Gemini CLI | 否 | Gemini 系列 | 支持 | 中 | 低 | Google 生态、多模态任务 |
| Qoder CLI | 否 | 通义系列为主 | — | 中 | 低 | 国内生态、快速响应、CodeReview |
| CodeBuddy | 否 | 混元+DeepSeek | 支持 | 中 | 低 | 腾讯生态、全流程开发 |

## 选型建议

- **追求极致编码体验** → **Claude Code**：当前社区偏好度最高（46%），Agent 能力强，适合大型项目
- **开源自由 + 多模型切换** → **OpenCode**：社区最活跃的开源 CLI，可对接任意模型
- **OpenAI 深度用户** → **Codex CLI**：与 GPT-5 模型深度绑定，原生 Computer Use
- **国内生态优先** → **Qoder CLI**（阿里）/ **CodeBuddy**（腾讯）：中文优化好，国产模型集成
- **Google 全家桶用户** → **Gemini CLI**：与 Gemini 3 模型和 Google Cloud 深度集成

## 辅助工具

| 工具 | 特点 |
|------|------|
| **[cc-switch](https://github.com/farion1231/cc-switch)**（66K star） | 跨平台桌面应用，一键切换 Claude Code / Codex / OpenCode / OpenClaw / Gemini CLI，免去终端手动切换的繁琐 |

