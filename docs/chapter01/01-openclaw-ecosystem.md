# 一、龙虾 Claw 产品系列

[← 返回总览](../index.md) | [下一章：二、Coding Plan →](../chapter02/02-coding-plan.md)

"龙虾"是对开源 AI 智能体 **[OpenClaw](https://openclaw.ai/)**（原名 Clawdbot/Moltbot）的昵称，因其红色机械龙虾图标而得名。它能理解自然语言指令，自主调用电脑工具完成任务，真正实现从"意图"到"执行"的闭环。

**[openclaw/openclaw](https://github.com/openclaw/openclaw)**：370K star · 76K fork · TypeScript · MIT 协议 · 每日发版

## OpenClaw 核心能力

- **模型自由**：对接 Claude、GPT、Gemini、DeepSeek、Kimi、Qwen、GLM 等主流模型，也支持 Ollama 本地模型
- **系统操控**：读写文件、运行代码/脚本（可沙盒）、模拟键鼠、操控浏览器
- **多 IM 接入**：WhatsApp、Telegram、Discord、Slack、Signal、iMessage、微信、飞书、QQ
- **持久记忆**：记住用户偏好和上下文，跨会话形成个性化 AI
- **技能系统**：[ClawHub](https://openclaw.ai/) 技能市场 + 社区 [5400+ Skills](https://github.com/VoltAgent/awesome-openclaw-skills)（48K star）
- **多智能体**：可同时运行多个实例协同工作
- **后台自动化**：cron 任务、定时提醒、后台常驻
- **语音能力**：集成 ElevenLabs TTS，支持语音通话
- **伴侣应用（Beta）**：macOS 15+ 菜单栏应用

## 最新动态

| 时间 | 事件 |
|------|------|
| 2026-05-10 | 发版 v2026.5.10-beta.2，保持每日发版节奏 |
| 2026-03-07 | **ClawCon** 线下聚会在纽约举办，社区展示开放生态 |
| 2026-02-15 | 创始人 **Peter Steinberger 加入 OpenAI**，项目仍以开源形式继续 |
| 2026-01-30 | TechCrunch 报道：OpenClaw AI 助手开始构建社交网络 **Moltbook** |
| 2025-11-24 | 项目创建，仅 6 个月达到 370K star |

## 国内"龙虾"产品矩阵

| 产品 | 厂商 | 部署 | 生态绑定 | 定位 |
|------|------|------|---------|------|
| **[OpenClaw](https://openclaw.ai/)** | 开源社区 | 本地/云端 | 模型自由 | 开源旗舰，370K star，"海纳百川" |
| **[AutoClaw](https://autoglm.z.ai/autoclaw/)** | 智谱 AI | 本地（一键安装） | GLM 系列 | 预置 50+ Skills，内置 Pony-Alpha-2，支持飞书 |
| **[KimiClaw](https://kimi-claw.com/)** | 月之暗面 | 云端 | Kimi 系列 | 调用 Kimi 自有模型（K2.6） |
| **[MaxClaw](https://agent.minimaxi.com/activity/max-claw)** | MiniMax | 云端 | MiniMax 系列 | 调用 MiniMax 自有模型，语音/音乐能力强 |
| **[ArkClaw](https://console.volcengine.com/ark/region:ark+cn-beijing/experience/claw)** | 字节跳动 | 云端 | 豆包系列 | 火山引擎旗下，深度集成豆包大模型 |
| **[QClaw](https://qclaw.qq.com/)** | 腾讯 | 本地 | 混元系列 | 面向企业办公场景 |

## 六款 Claw 产品对比

| 维度 | OpenClaw | AutoClaw | KimiClaw | MaxClaw | ArkClaw | QClaw |
|------|---------|---------|---------|---------|---------|------|
| 开源 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 模型自由度 | 任意模型 | GLM 系列 | Kimi 系列 | MiniMax 系列 | 豆包系列 | 混元系列 |
| Skills 市场 | ClawHub + 5400+ | 50+ 预置 | — | — | — | — |
| 本地部署 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| 多 IM 支持 | 10+ | 飞书等 | — | — | — | 企业 IM |
| 语音 | ElevenLabs | — | — | 原生语音 | — | — |
| 社区规模 | 370K star | — | — | — | — | — |
| 发版节奏 | 每日 | — | — | — | — | — |

## 选型建议

- **追求最大自由度 + 社区生态** → **OpenClaw**：开源、370K star、每日迭代、任意模型、5400+ Skills
- **智谱生态用户** → **AutoClaw**：与 GLM 模型深度绑定，一键安装，预置技能
- **Kimi/MiniMax/豆包/混元深度用户** → 对应厂商的 Claw 产品，模型绑定但集成度高
- **企业办公场景** → **QClaw**：腾讯生态，面向企业内部协作

## 相关文章

- [OpenClaw 全攻略](https://developer.aliyun.com/article/1719048)
- [中美 OpenClaw 发展对比](https://www.163.com/dy/article/KOBC9MBE05568W0A.html)
