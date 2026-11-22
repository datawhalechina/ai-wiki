# 一、龙虾 Claw 产品系列

[← 返回总览](../index.md) | [下一章：二、Coding Plan →](../chapter02/02-coding-plan.md)

"龙虾"是对开源 AI 智能体 **[OpenClaw](https://openclaw.ai/)**（原名 Clawdbot/Moltbot）的昵称，因其红色机械龙虾图标而得名。它能理解自然语言指令，自主调用电脑工具完成任务，真正实现从"意图"到"执行"的闭环。

**[openclaw/openclaw](https://github.com/openclaw/openclaw)**：395.0K star · 76K fork · TypeScript · MIT 协议 · 每日发版

## OpenClaw 核心能力

- **模型自由**：对接 Claude、GPT、Gemini、DeepSeek、Kimi、Qwen、GLM 等主流模型，也支持 Ollama 本地模型
- **系统操控**：读写文件、运行代码/脚本（可沙盒）、模拟键鼠、操控浏览器
- **多 IM 接入**：WhatsApp、Telegram、Discord、Slack、Signal、iMessage、微信、飞书、QQ
- **持久记忆**：记住用户偏好和上下文，跨会话形成个性化 AI
- **技能系统**：[ClawHub](https://openclaw.ai/) 技能市场（已拆为 **Skills + Plugins** 双结构，并设有[中国官方镜像 mirror-cn.clawhub.com](https://mirror-cn.clawhub.com/)，2026-04 由火山引擎共建）+ 社区 [5400+ Skills](https://github.com/VoltAgent/awesome-openclaw-skills)（53.9K star）
- **多智能体**：可同时运行多个实例协同工作
- **可观测面板**（2026-11 起）：Chat Details 侧栏汇总会话信息、任务进度、PR 与自动化任务，Subagents 面板可只读查看每个 worker 的 transcript
- **Advisor 自查**（实验性，默认关闭）：Agent 干活途中复检进展，发现「重复失败的路径」或「偏离请求」时给出纠正建议。**只建议、不执行工具、不代批**，且每次复查多花一轮模型调用
- **MCP Relay**（可选插件，默认关闭）：让 ChatGPT / Claude 直连 OpenClaw 会话，**不用开公网端口、不必交出 Gateway 密码**；代价是 relay 能读到流经它的内容
- **后台自动化**：cron 任务、定时提醒、后台常驻；2026-11 起支持 **MCP 事件触发**（MCP 服务器上报事件即启任务，需公网 HTTPS 回调）
- **语音能力**：集成 ElevenLabs TTS，支持语音通话
- **伴侣应用（Beta）**：macOS 15+ 菜单栏应用

## 最新动态

| 时间 | 事件 |
|------|------|
| 2026-11-19 | 发版 **v2026.11.6**（当前 stable / npm `latest`，**386 个 PR / 157 位贡献者**、48 个直接提交的补丁版）：从安装、Web UI、消息、记忆、技能、原生应用到模型提供商全链修复，**没有新功能**。三条会改变行为的要留意：① **shell 审批口径收紧**——macOS / Linux 上原本自动执行的一部分命令，现在按现有策略弹审批或被直接拒（安全修复）；② **默认日志迁到所选状态目录**，用独立状态目录的 Gateway，外部日志收集器要改路径或改用 `openclaw logs`（已存在的日志文件不迁移，显式配置的路径不变）；③ **Git 更新默认不再构建 TypeScript 声明**，要 `.d.ts` 得设 `OPENCLAW_RUN_NODE_SKIP_DTS_BUILD=0` 恢复。修复里值得记的两条：**直接更新技能时会把 API Key 引用静默替换成明文**（现在拒绝该请求）、**Doctor 与更新迁移把 API 路由和 Claude / Gemini CLI 路由错误合并**（影响计费与兜底）。另修 macOS / Linux 全新安装请求 beta 却静默装成 stable、清理误删被指定保留的工作区、Discord 附件下载继承私有网络权限、浏览器快照暴露已填密码与一次性卡号安全码等。捆绑 Codex 升到 **0.169.0**、Grok OAuth 代理升到 **1.0.13**；同期 `beta` 标签已是 **2026.11.10-beta.1** |
| 2026-11-18 | 发版 **extended-stable 2026.10.33**（LTS 渠道，**接替 2026.9.37**；当天 stable 仍是 11.5，次日由 11.6 接替）：官方定位「10 月底的产品 + 关键安全更新 + 可靠性/性能修复」，兼容性基线锁在 **11.4**。七条 Highlight 里值得记的是四条——① **长会话与大库的内存上限**：聊天、内存导出、Doctor 修复与 Gateway 启动的导出/恢复都改成有界工作量，减少 OOM；② **中断更新可自愈**（执行器挂掉后 Gateway 不再永久离线）；③ **回复跨重启存活**（保留原始提示、补回 Telegram / WhatsApp / Signal 的丢失回复）；④ **共享会话隐私收紧**（Side chat 只对查看者可见、内部模型提示不进展示输出、压缩摘要里的凭证会被脱敏）。另有自动化可响应轮询条件与 MCP 事件、技能改为按需检索而不再全量进 prompt、可导入 Claude Code / Codex 的既有 transcript。分发范围只含核心 npm 包、官方 npm 插件与 Gateway Docker 镜像，**不含原生应用** |
| 2026-11-17 | 发版 **v2026.11.5**（11-17 起为 stable / npm `latest`，已被 11.6 接替；距 11.4 仅 1 天）：官方口径 **351 个 PR**。七条 Highlight 里六条仍是可靠性（跨 Gateway 重启保留排队消息与最终落库、Doctor / Gateway 启动失败**自动回滚**已激活的更新、Telegram 消息内渲染交互组件、大库内存索引重建与 embedding 批次错误恢复、主账号不再阻断 Claude CLI 兜底、设备文件夹在默认运行时可选、二进制附件不再串成乱码提示词），但**夹了一条破坏性变更**——第三方 harness 必须在宿主 `runAttempt` 回调内注册按会话键管理的活跃运行并保留清理函数，插件 RPC 处理器要把 `chatAbortControllers` / `chatQueuedTurns` 换成经授权的 Gateway 方法派发，start-owner 观察改用 `startDeadlineAtMs`（原 `expiresAtMs`）。自研 harness / 插件的用户升级前先读这条 |
| 2026-11-16 | 发版 **v2026.11.4**（11-17 前为 stable，已被 11.5 接替；距 11.3 仅 6 天）：**纯稳定性版，Highlight 无一条新功能**。六组问题各归一处——① **大会话内存**：大 transcript 裁剪、分页内存导出与 Doctor 修复不再打爆 worker 内存；② **大库启动**：插件及其服务提前到 orphan 扫描之前拉起，扫描活跃恢复候选时不再连带加载无关的历史会话摘要；③ **回复可靠性**：跨 Gateway 重启保留未答提示、WhatsApp 最终回复不被无关重载吃掉、Signal 重连不再跳过缓冲消息；④ **会话隐私**：Side chat 只对通过认证的查看者可见，配对节点的照片与截图恢复默认私密，内部模型提示投影不再混入展示输出；⑤ **升级安全**：新版 CLI 不会把共享数据库迁移到超出旧 Gateway 守护进程支持的版本，同时允许互不相关的安装库各自独立；⑥ **Safe Files**：工作区被替换后拒绝旧编辑器的过期保存，不再覆盖新工作区里的文件。另修 PostgreSQL 不再强制关闭 `synchronous_commit`、委托式管理变更需显式授权并在每次落地前复核 |
| 2026-11-10 | 发版 **v2026.11.3**（11-16 前为 stable，现已被 11.4 / 11.5 接替）：**安全修复版**，官方口径 **56 个 PR / 36 位贡献者**，明确「无新配置项或新功能」。主修凭证外泄——缓存与复用的插件结果按连接凭证隔离、其他插件的传输钩子锁回该 provider 源站、Firecrawl/Exa/Tavily 的 Key 不再跨凭据混用、Signal 守护进程与内置语言服务器不再继承 Gateway 密钥；另修工作区传输证书校验（空指纹时保留已存证书）、必需沙箱下图片预览只留在允许目录、更新中断后 Gateway 停在停止状态、慢存储上的备份超时。同渠道另有 extended-stable **2026.9.37** |
| 2026-11-08 | 发版 **v2026.11.2**：纯修复版，115 个 PR、64 位贡献者，主攻隐私与信任边界（配置密钥不再写入本地审计历史、LSP 输出不再进日志、沙箱搜索只认可信 provider）、账号安全的投递重试、Gateway 可用性与更新自愈。**无新功能**，但修复了从 2026.10.10 升级时卡在「database is locked」的问题 |
| 2026-11-03 | 发版 **v2026.10.10**（功能版，结束 5 个 beta）：官方口径 **3,028 个 PR / 454 位贡献者**。新增 Chat Details 侧栏、实验性 **Advisor**、Browser Talk 分离语音、跨机文件夹、可选 **MCP Relay** 插件、MCP 事件触发自动化 |
| 2026-09-19 | 发版 v2026.9.5；另有 extended-stable 渠道 v2026.7.35（09-21），面向求稳的生产用户（现 extended-stable 为 **2026.10.33**，11-18 接替 2026.9.37） |
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
| **[OpenClaw](https://openclaw.ai/)** | 开源社区 | 本地/云端 | 任意模型 | 开源旗舰，395.0K star，"海纳百川" |
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
| 社区规模 | 395.0K star | — | — | — | — | — |
| 发版节奏 | 每日 | — | — | — | — | — |

## OpenClaw 周边生态

除上述厂商产品外，社区还涌现了丰富的周边工具：

| 项目 | 领域 | 亮点 |
|------|------|------|
| **[claw-code](https://github.com/ultraworkers/claw-code)**（194.7K star） | Rust 重写 | "史上最快突破 100K star"，Rust 高性能版本 |
| **[NVIDIA NemoClaw](https://github.com/NVIDIA/NemoClaw)**（23.1K star） | 安全沙盒 | NVIDIA OpenShell 安全容器运行 OpenClaw |
| **[ClawX](https://github.com/ValueCell-ai/ClawX)**（7.6K star） | 桌面 GUI | 图形界面版，[中文站 clawx.com.cn](https://clawx.com.cn) |
| **[AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)**（14.9K star） | 科研自动化 | 从想法到论文全自动 |
| **[ClawWork](https://github.com/HKUDS/ClawWork)**（8.6K star） | 自动化工作 | "11 小时赚 $15K" |
| **[ClawTeam](https://github.com/HKUDS/ClawTeam)**（5.6K star） | 群体智能 | 多 Agent 集群全自动协作 |
| **[clawpanel](https://github.com/qingchencloud/clawpanel)**（2.9K star） | 管理面板 | 多引擎管理，Tauri 桌面应用，11 种语言 |
| **[汉化版](https://github.com/1186258278/OpenClawChineseTranslation)**（3.8K star） | 中文本地化 | CLI + Dashboard 全中文，含搭建教程 |

## 选型建议

- **追求最大自由度 + 社区生态** → **OpenClaw**：开源、395.0K star、每日迭代、任意模型、5400+ Skills
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
