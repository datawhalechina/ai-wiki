# 一、龙虾 Claw 产品系列

[← 返回总览](../index.md) | [下一章：二、Coding Plan →](../chapter02/02-coding-plan.md)

"龙虾"是对开源 AI 智能体 **[OpenClaw](https://openclaw.ai/)**（原名 Clawdbot/Moltbot）的昵称，因其红色机械龙虾图标而得名。它能理解自然语言指令，自主调用电脑工具完成任务，真正实现从"意图"到"执行"的闭环。

**[openclaw/openclaw](https://github.com/openclaw/openclaw)**：390.3K star · 76K fork · TypeScript · MIT 协议 · 每日发版

## OpenClaw 核心能力

- **模型自由**：对接 Claude、GPT、Gemini、DeepSeek、Kimi、Qwen、GLM 等主流模型，也支持 Ollama 本地模型
- **系统操控**：读写文件、运行代码/脚本（可沙盒）、模拟键鼠、操控浏览器
- **多 IM 接入**：WhatsApp、Telegram、Discord、Slack、Signal、iMessage、微信、飞书、QQ
- **持久记忆**：记住用户偏好和上下文，跨会话形成个性化 AI
- **技能系统**：[ClawHub](https://openclaw.ai/) 技能市场（已拆为 **Skills + Plugins** 双结构，并设有[中国官方镜像 mirror-cn.clawhub.com](https://mirror-cn.clawhub.com/)，2026-04 由火山引擎共建）+ 社区 [5400+ Skills](https://github.com/VoltAgent/awesome-openclaw-skills)（52.7K star）
- **多智能体**：可同时运行多个实例协同工作
- **后台自动化**：cron 任务、定时提醒、后台常驻
- **语音能力**：集成 ElevenLabs TTS，支持语音通话
- **伴侣应用（Beta）**：macOS 15+ 菜单栏应用

## 最新动态

| 时间 | 事件 |
|------|------|
| 2026-09-19 | 发版 **v2026.9.5**（最新正式版）；另有 extended-stable 渠道 v2026.7.35（09-21），面向求稳的生产用户 |
| 2026-08-31 | 发布 **OpenClaw 2.0**（v2026.8.1）：官方口径 **987 位贡献者、16,977 个 PR**，约合项目历史 PR 总量的一半 |
| 2026-07-08 | 项目转入 **[OpenClaw Foundation](https://openclaw.ai/blog/introducing-openclaw-foundation)**，成为美国 501(c)(3) 非营利组织，**协议保持 MIT**；OpenAI 为主要捐赠方 |
| 2026-05-10 | 发版 v2026.5.10-beta.2，保持每日发版节奏 |
| 2026-03-07 | **ClawCon** 线下聚会在纽约举办，社区展示开放生态 |
| 2026-02-15 | 创始人 **Peter Steinberger 加入 OpenAI**，项目仍以开源形式继续 |
| 2026-01-30 | TechCrunch 报道：OpenClaw AI 助手开始构建社交网络 **Moltbook** |
| 2025-11-24 | 项目创建，仅 6 个月达到 370K star |

## 国内"龙虾"产品矩阵

2026 年 3 月起，国内厂商密集推出 Claw 类产品，从最初的 6 款扩至 12 款以上。纳入本表的**必须是能给出厂商官方入口的产品**：

| 产品 | 厂商 | 端形态 | 模型 | 定位 |
|------|------|--------|------|------|
| **[OpenClaw](https://openclaw.ai/)** | 开源社区 | 本地/云端 | 任意模型 | 开源旗舰，390.3K star，"海纳百川" |
| **[AutoClaw（澳龙）](https://autoglm.z.ai/autoclaw/)** | 智谱 AI | **本地**（Win/macOS 一键安装，约 1 分钟） | **完全开放**（推荐 DeepSeek/Kimi/MiniMax/GLM） | 2026-03-10 上线，国内首个真·一键安装本地版；预置 50+ Skills；内置 Pony-Alpha-2（内测代号）；一键接入飞书 |
| **[KimiClaw](https://www.kimi.com/bot)** | 月之暗面 | 云端（另有桌面版 / 安卓托管） | Kimi 系（默认 K2.6，可切 K3） | 一键云部署，40GB 云存储；一键部署需 **Allegretto 及以上**会员 |
| **[MaxClaw](https://agent.minimaxi.com/activity/max-claw)** | MiniMax | 云端 | MiniMax 系（M3 / M2.7） | 10 秒部署、50GB 云存储；语音/音乐能力强 |
| **[ArkClaw](https://console.volcengine.com/ark/region:ark+cn-beijing/experience/claw)** | 火山引擎（字节） | 云端 SaaS | 豆包系 + 多家第三方 | 已推出**企业版**（席位制，单次 ≥5 席、最多 1000 席） |
| **[QClaw](https://qclaw.qq.com/)** | 腾讯（电脑管家团队） | **本地**（PC） | 混元系 | **V2 已支持最多 3 个 Agent 并行** + 智能连接器（腾讯文档/腾讯会议/金山文档/Notion/邮箱）+ 龙虾管家安全沙箱 |
| **[小艺Claw](https://xiaoyi.huawei.com/)** | 华为 | **手机 / 平板 / PC** | openPangu-2.0-Pro、DeepSeek V4、MiniMax M3 可切换 | 2026-06-25 起对 **HarmonyOS 5.0+ 全机型开放**；500+ Skills；套餐 49 元（1000 点）/ 199 元（6000 点） |
| **[JVSClaw](https://jvs.wuying.aliyun.com/)** | 阿里云（无影团队） | 云端（Web / iOS） | 多模型 | 2026-03 品牌独立，运行在 **ClawSpace 沙箱**；另有 JVS Computer / JVS Mobile 两条 B 端线 |
| **[DuMate（搭子）](https://dumate.baidu.com/)** | 百度智能云 | **PC + 移动端** | 文心系 | 2026-03-17 AI DAY 发布、03-22 全量上线；已发布 15 个行业套件；本地沙箱 + 权限分级 |
| **Xiaomi miclaw** | 小米 | **手机**（另有手表版） | MiMo | 2026-03 起**邀请制封测**，仅小米 17 系列等机型，走 OTA 推送，**无公开下载页**（入口在小米社区 miclaw 圈子）；官方自述为国内首个手机端类 OpenClaw 应用 |
| **[LobsterAI（有道龙虾）](https://lobsterai.youdao.com/)** | 网易有道 | **PC 桌面**（可 NAS 部署） | 模型自由 | 国内首个 **100% 开源**桌面级办公 Agent；2026-09-16 发布 **2.0**，兼容 OpenClaw 2.0，新增 Sites / Teams |
| **[AstronClaw](https://agent.xfyun.cn/astron-claw)** | 科大讯飞 | 云端 SaaS | 星火 X2 + MiniMax / Kimi / GLM 可切换 | 2026-03-12 上线；10000+ skills；沙箱隔离；支持企微/钉钉/飞书 |

**同样值得关注但未列入主表**：

| 产品 | 厂商 | 说明 |
|------|------|------|
| **HiClaw** | 阿里云（Higress 团队） | **Apache 2.0 开源的团队版**，Manager–Worker 架构 + Matrix 通信，与 JVSClaw **分属不同团队** |
| **纳米Work**（原 360 安全龙虾） | 360 | 2026-07-28 由「360 安全龙虾」整体升级而来，PC 客户端 + 硬件 Box，主打安全与多智能体 |
| **UniClaw** | 中国联通 | 2026-04-28 发布，含 UniClaw Box / U 盘随身版；**注意是联通，不是腾讯** |
| **Mavis** | MiniMax | **不是 MaxClaw 改名**——它是 MiniMax Agent 于 2026-05 升级并更名而来，主打 Agent Teams（Leader/Worker/Verifier 三角色协作），与 MaxClaw 并列存在 |

> ⚠️ **厂商标注易错点**（社区文章常见错误，引用前请核对）
> 1. **AutoClaw = 智谱 AI**（不是字节跳动），中文名「澳龙」。
> 2. **UniClaw = 中国联通**（不是腾讯）。
> 3. **JVSClaw / HiClaw / CoPaw 同属阿里云但分属不同团队**（无影 / Higress / 通义），不要笼统写成「阿里云 JVSClaw」。
> 4. **MaxClaw ≠ Mavis**：前者是云端 Claw 托管服务，后者是 MiniMax Agent 更名后的多智能体平台，同名混淆极常见。
> 5. **AutoClaw 的模型是完全开放的**，支持接入任意模型的 Coding Plan 或 API，并非只能跑 GLM（早期资料常见此误）。
> 6. **KimiClaw 的官方入口是 `kimi.com/bot`**，而非各种第三方「kimi-claw.com」类站点。

## 按端形态选型

| 端形态 | 代表产品 | 适合谁 |
|--------|---------|--------|
| **本地（PC）** | OpenClaw、AutoClaw、QClaw、LobsterAI | 在意数据不出本机、要操控本地文件与软件 |
| **云端** | KimiClaw、MaxClaw、ArkClaw、JVSClaw、AstronClaw | 想零部署开箱即用、要 7×24 常驻 |
| **手机 / 平板** | 小艺Claw、Xiaomi miclaw | 随时随地下派任务，受机型限制较多 |
| **跨端** | DuMate（PC + 移动）、小艺Claw（三端） | 桌面与移动都要覆盖 |

## 重点产品能力对照

| 维度 | OpenClaw | AutoClaw | KimiClaw | MaxClaw | ArkClaw | QClaw |
|------|---------|---------|---------|---------|---------|------|
| 开源 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 模型自由度 | 任意模型 | **任意模型的 Coding Plan / API** | Kimi 系列 | MiniMax 系列 | 豆包系 | 混元系列 |
| Skills 市场 | ClawHub + 5400+ | 50+ 预置 | ClawHub 可用 | — | — | — |
| 本地部署 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| 多 IM 支持 | 10+ | 飞书等 | 多通道 | — | — | 企业 IM |
| 语音 | ElevenLabs | — | — | 原生语音 | — | — |
| 企业版 | — | — | — | — | ✅ 席位制 | — |
| 社区规模 | 390.3K star | — | — | — | — | — |
| 发版节奏 | 每日 | — | — | — | — | — |

## OpenClaw 周边生态

除上述厂商产品外，社区还涌现了丰富的周边工具：

| 项目 | 领域 | 亮点 |
|------|------|------|
| **[claw-code](https://github.com/ultraworkers/claw-code)**（195.3K star） | Rust 重写 | "史上最快突破 100K star"，Rust 高性能版本 |
| **[NVIDIA NemoClaw](https://github.com/NVIDIA/NemoClaw)**（22.5K star） | 安全沙盒 | NVIDIA OpenShell 安全容器运行 OpenClaw |
| **[ClawX](https://github.com/ValueCell-ai/ClawX)**（7.6K star） | 桌面 GUI | 图形界面版，[中文站 clawx.com.cn](https://clawx.com.cn) |
| **[AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)**（14.5K star） | 科研自动化 | 从想法到论文全自动 |
| **[ClawWork](https://github.com/HKUDS/ClawWork)**（8.6K star） | 自动化工作 | "11 小时赚 $15K" |
| **[ClawTeam](https://github.com/HKUDS/ClawTeam)**（5.5K star） | 群体智能 | 多 Agent 集群全自动协作 |
| **[clawpanel](https://github.com/qingchencloud/clawpanel)**（2.9K star） | 管理面板 | 多引擎管理，Tauri 桌面应用，11 种语言 |
| **[汉化版](https://github.com/1186258278/OpenClawChineseTranslation)**（3.8K star） | 中文本地化 | CLI + Dashboard 全中文，含搭建教程 |

## 选型建议

- **追求最大自由度 + 社区生态** → **OpenClaw**：开源、390.3K star、每日迭代、任意模型、5400+ Skills
- **想低门槛在本地跑起来** → **AutoClaw（澳龙）**：一键安装、预置 50+ Skills、**模型完全开放**（可接任意模型的 Coding Plan，不绑定 GLM）
- **数据不出本机、要开源可控** → **LobsterAI（有道龙虾）**：100% 开源桌面 Agent，可 NAS 部署
- **不想装东西，开箱即用** → **KimiClaw**（`kimi.com/bot`）/ **MaxClaw** / **JVSClaw**：云端一键部署
- **手机上下派任务** → **小艺Claw**（HarmonyOS 全机型）/ **Xiaomi miclaw**（小米机型且为邀请制）
- **企业采购、要席位管理** → **ArkClaw 企业版**（火山引擎）/ **HiClaw**（阿里云开源团队版）
- **模型绑定但集成度高** → 对应厂商的 Claw 产品：KimiClaw / MaxClaw / ArkClaw / QClaw / AstronClaw
- **需要高性能** → **claw-code**（Rust 版）
- **需要桌面体验** → **ClawX** / **clawpanel**

## 相关文章

- [OpenClaw 全攻略](https://developer.aliyun.com/article/1719048)
- [中美 OpenClaw 发展对比](https://www.163.com/dy/article/KOBC9MBE05568W0A.html)
