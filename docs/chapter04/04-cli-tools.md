# 四、CLI 种类

[← 上一章：三、三方模型（API）](../chapter03/03-model-api.md) | [返回总览](../index.md) | [下一章：五、好用的 Skill →](../chapter05/05-skills.md)

CLI（命令行界面）AI 工具是终端中的 AI 编程助手，支持自然语言驱动开发全流程。

**提示**：开源 CLI 工具生态还在快速演进，建议关注各工具的插件体系和 MCP 集成能力。

## 主流 AI CLI 工具

| 工具                                                         | 厂商      | 特点                                                         |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| **[Claude Code](https://code.claude.com/docs/zh-CN/overview)** | Anthropic | 终端级深度编码助手，最新 **2.1.329**（2026-11-19，仍是修复为主的大补丁，但先看三处新增：**`/tasks` 升级为会话级总览**——一次看清本次对话里的定时任务、`/loop` 唤醒、目标与对话分叉，按 `x` 会在询问后停掉其中一个；**`/mcp` 的服务器页新增 Server message 行**，把远程 HTTP MCP 被拒时返回的 JSON-RPC 错误原文摆出来，不用再翻日志；**`/status` 增 Marketplace auto-update 行**，列出没有自动更新的托管市场及原因。另外 **OpenTelemetry 与 Code Mode 可以同时开**了——脚本里每次工具调用都会发事件（追踪类特性仍要求代价：开着它就关 Code Mode）。最该关注的是修掉一处**会丢配置**的 bug：网络卡顿或文件锁让 `~/.claude.json` 读不到时，保存会把文件清空、有时直接重置成默认值；同批还修了 macOS 上能读不能写 Keychain 导致的反复登出、`/teleport` 选云会话会顶掉当前打开的对话、后台 MCP 任务在慢重连后停滞、以 `application/octet-stream` 发来的 PDF / 图片 / Office 文件被存成 `.bin`，并**撤掉了 2.1.326 在 `max_tokens` 报错处的自动重试**。前一版 **2.1.328**（11-18，144 条修复的补丁：**auto 模式的自动判断扩到 Bedrock / Google Cloud Agent Platform / Microsoft Foundry 与 Claude apps gateway**，交互式会话只要没指定权限模式就直接落在 auto；MCP 工具 schema 以 `anyOf / oneOf / allOf` 开头时不再整段消失，单个坏 schema 只让该工具被跳过、不再拖垮整个会话；自动压缩不再复用旧的系统提示词；修好 zsh 里 `=cmd` 被误当命令路径展开（`echo ====` 报 not found）这类静默失败；`mcp_tool` hook 新增 `"onFailure": "block"`；自托管 runner 增 `--repository-folder` / `--hook-label` / `--metadata` 与两个编排器指标）。前一版 **2.1.327**（11-17）侧重凭证与体检：`claude mcp add-json <name> -` 支持从 **stdin** 读服务器 JSON，令牌不必再落到命令行历史；`/status` 新增一段**体检清单**——列出损坏的 agent / skill / command / output-style 文件、键位冲突、不可用的沙箱、被忽略的权限设置，以及「永远匹配不上」的 hook matcher；`/config` 会标出被其他设置覆盖的行；`/tui classic` 成为非全屏渲染器的正式名，并修了一批会话恢复与 `/export`、`/rewind`、`/plugin` 的静默失败。Stack Overflow 2026 开发者调查中采用率 **65.5%**，为同类最高（Codex CLI 29.5%），155.7K GitHub 星标 |
| **[Codex CLI](https://openai.com/codex/)**                   | OpenAI    | 最新 **0.171.0**（2026-11-20）：**模型目录正式纳入 `gpt-6.2-sol` / `gpt-6.2-astra`，且 Sol 是目录里的默认项**——这是 6.2 发布后官方第一次把默认值写进 release note；**TUI 工作区默认开启**（侧边可搜的文档预览、图片预览、subagent 转录与主对话并排）；非 Vim 输入模式支持自定义 **undo / redo 快捷键**，附件与大段粘贴一起回滚；新增 `codex exec --remote <ADDR>`（在已有 app server 上起或续非交互会话）、`/rc` 与 `/remote`（管本地 remote control、显示设备配对码）、`/statusline`（自选或自写 MCP 状态行）。修了切会话时草稿 / 排队追问 / 中断输入没跟回原线程、改工作目录会丢权限配置、上一轮迟到的完成事件取消新一轮审批，以及 IdP 不发 refresh token 时的企业 MCP 登录。前一版 **0.170.0**（11-18）：TUI 里的实时语音通话改走 **WebRTC 协商**、OpenTelemetry 导出器支持自动刷新的鉴权头、实验性支持「不同环境下的同名 MCP 服务器共存」；修 MCP OAuth 在取消/登录/登出时的凭证竞态、Cloud 会话断流后的自动重连、Windows 沙箱的文件替换与权限保留。默认模型自 0.153.4 起是 **`gpt-6-astra`**，11-17 起 **`gpt-6.2-astra` / `gpt-6.2-sol` 已可通过 `/model` 选用**，**0.171 起模型目录的默认项换成 `gpt-6.2-sol`**（官方原话 default catalog selection）——但「目录默认」不等于已存的配置会被改写，升级后仍建议用 `/model` 确认自己挂在哪一代。客户端默认挂在 **Low 推理档**防额度超支；**0.165 起接入 GCP Vertex AI 作为内置 provider**（`model_provider = "gcp"`），模型目录加入 **`gpt-6.1-terra`**；**GPT-5.5 已于 2026-10-14 从 ChatGPT 登录会话退役**（API 与 API-key 会话不受影响），官方建议把保存的设置与脚本指向 `gpt-6.1-sol`。0.167 新增 agent 指挥中心（`codex agents --no-daemon`）、跨后端切换保留草稿、10 个 `/presets` 槽位；**0.168 把 provider 选择搬进 TUI**（Sessions → Model providers 选默认）、侧栏会话可拖拽缩放（`leader z`）、支持音频附件与动图；**0.169 扩成多标签侧栏、可按名称 / 提示预览 / 工作目录搜索历史任务、终端内增改自定义 provider（SSH 可走 device code）**，并让 `codex exec` 在不可信目录默认关闭项目配置与 MCP（需显式 `--trust`） |
| **[OpenCode](https://opencode.ai/)**                         | 开源      | 227.0K GitHub 星标                                            |
| **[DSH](https://github.com/deepseek-ai/deepseek-harness)**   | DeepSeek  | 281.4K GitHub 星标。开源 Agent 运行时，主打「一切皆插件」——模型、工具、循环、UI 均可替换重组；**当前 `0.2.2-rc`（npm `latest` 为 `0.2.2-rc.1`），仍属开发者预览，官方明示会出现破坏兼容性的变更、不可用于生产**；插件怎么装、索引源加哪个见下文「DSH 插件推荐小结」 |
| **[Pi](https://github.com/earendil-works/pi)**               | Earendil Works | 122.1K GitHub 星标。极简底座——只保留读/写/改文件与跑命令四个工具；支持单会话内跨供应商接力（Claude 做到一半转给 DeepSeek 继续） |
| **[Antigravity CLI](https://antigravity.google/)**           | Google    | 命令名 `agy`，Gemini CLI 的继任者，已全面开放（第三方多标注为 preview，**官方未使用 GA 字样**）。**Gemini CLI 已于 2026-06-18 对免费 / Google AI Pro / Google AI Ultra 用户停止服务**，企业版（Code Assist）不受影响。个人档 **$0/月**，无需信用卡 |
| **[Qoder CLI](https://qoder.com)**                           | Qoder-AI | Agentic Coding Platform，支持 CLI 和 IDE，自主编程模式，CodeReview 能力 |
| **[CodeBuddy](https://codebuddy.cn/)**                       | 腾讯      | 命令行中用自然语言驱动开发全流程                             |

## CLI 模型支持矩阵

CLI 工具最关键的分化点是**能不能换模型**——这直接决定你会不会被单一厂商绑定，以及能否用国内 Coding Plan 降低调用成本：

| 工具 | 默认模型 | 可切换范围 | 自由度 |
|------|---------|-----------|--------|
| **Claude Code** | Anthropic Claude（现役 Opus 5.5） | 原生仅 Anthropic；**可通过 Base URL 指向第三方端点**（阿里云、腾讯云 Coding Plan 均支持此用法） | 中 |
| **Codex CLI** | **`gpt-6-astra`** | `gpt-6.1-sol`（复杂编码与 agentic 流程）、`gpt-6.1-terra`（视觉推理 / computer use / 写作）、`gpt-6-sol` / `gpt-6-luna`（存量档位）；另有 GCP Vertex AI 与 Amazon Bedrock 渠道 | 低（仅 OpenAI） |
| **Antigravity CLI** | Gemini 4 系 | Gemini 4 Neon / Argon / Carbon / Hydrogen、3.1 Pro，以及 **Claude Sonnet 4.6、Claude Opus 4.6、gpt-oss-120b**；**1.5.12（11-19）起配 `GEMINI_API_KEY` 也能用 Neon**；1.5.1 起所有 ACP 客户端可用账户全部模型 | 中（**不支持 BYOK**） |
| **OpenCode** | 内置免费模型 | **Go 订阅打包 30 款**：GLM-5.3、Kimi K3、DeepSeek V4.1、MiMo、Qwen3.8、MiniMax M3、Grok 4.7 等 | 极高 |
| **DSH** | 可切换 | 支持**近 40 家**模型提供方，模型/工具/循环/UI 均可替换 | 极高 |
| **Pi** | 可切换 | 多供应商（20+），支持**单会话内跨供应商接力** | 极高 |
| **Qoder CLI** | 多模型 | 多模型支持 | 中 |
| **CodeBuddy** | 混元系 | 混元 + DeepSeek | 低 |

> 💡 **换模型的两种方式**：① 工具内置模型选择器（如 Codex 的 `codex --model gpt-6-sol`）；② 通过 Base URL + API Key 指向第三方端点——这是国内用户把 Claude Code、Cursor 接到 Coding Plan 上的通用做法。

## CLI 工具选型对比

| 工具 | 开源 | 模型灵活度 | MCP 支持 | 社区活跃度 | 学习门槛 | 适用场景 |
|------|------|-----------|---------|-----------|---------|---------|
| Claude Code | 否 | Claude 系列 | 深度集成 | 极高（155.7K star） | 低 | 深度编码、大型项目重构 |
| Codex CLI | 开源 | **`gpt-6-astra` 默认，可切 6.1 Sol / 6.1 Terra / Luna** | 支持 | 高 | 低 | OpenAI 生态、多模型切换 |
| OpenCode | 开源 | 多模型自由 | 支持 | 极高（227.0K star） | 中 | 开源优先、社区驱动、自定义工作流 |
| Antigravity CLI | 否 | Gemini + Claude + gpt-oss | 支持 | 中 | 低 | Google 生态、多模态任务、免费档 $0（2026-06 起取代 Gemini CLI） |
| Qoder CLI | 否 | 多模型支持 | 支持 | 中 | 低 | 自主编程、CodeReview、IDE+CLI 双模式 |
| CodeBuddy | 否 | 混元+DeepSeek | 支持 | 中 | 低 | 腾讯生态、全流程开发 |
| DSH | 开源（MIT） | 近 40 家提供方 | 支持 | 高（281.4K star） | 中 | 插件化改造、自定义 agent 运行时（预览版） |
| Pi | 开源（MIT） | 多供应商（20+） | 支持 | 高（122.1K star） | 中 | 极简底座、自建工作流、跨模型接力 |

## 选型建议

- **追求极致编码体验** → **Claude Code**：Stack Overflow 调查中采用率 65.5%，Agent 能力强，适合大型项目
- **开源自由 + 多模型切换** → **OpenCode**：社区最活跃的开源 CLI，可对接任意模型
- **OpenAI 深度用户** → **Codex CLI**：默认 `gpt-6-astra`，日常主力建议切 `gpt-6.1-sol`（$2/$10），视觉与电脑操作用 `gpt-6.1-terra`（$1/$5）
- **国内生态优先** → **Qoder CLI**（Agentic Coding）/ **CodeBuddy**（腾讯）：中文优化好，自主编程模式
- **Google 全家桶用户** → **Antigravity CLI（`agy`）**：Gemini CLI 已于 2026-06-18 对个人用户停服，由其继任；个人档 **$0** 且可选 Claude / gpt-oss 模型，与企业版 Code Assist 和 Google Cloud 深度集成
- **想自己拼装 agent 底座** → **DSH**（一切皆插件，模型/工具/循环都可换，但仍是预览版）/ **Pi**（极简四工具底座，适合把 agent 嵌进自己的工作流）

## DSH 插件推荐小结

DSH 的「一切皆插件」不是修辞。官方 CLI 帮助里把 `dsh` 的启动过程描述为「**按序叠放的插件包补丁层（plugin-bundle patch layers），你的覆盖在最上面**」——所以模型、工具、循环、UI 都能换，而换的方式就是装卸插件包。

当前版本为 **`0.2.2-rc`**（npm 上 `latest` 与 `next` 两个 dist-tag 现已同时指向 **`0.2.2-rc.5`**（2026-11-18）——即 `npm i -g @deepseek-ai/dsh` 拿到的就是 rc.5，不再是此前的 `0.2.2-rc.1`），**全部是预发布**，官方仍标注「未来将出现破坏兼容性的变更」，不要用在生产。

**装插件**：`dsh plugin` 只是把参数转发给该 profile 目录下的 pnpm，因此语法就是 pnpm 的语法，改完要重启 `dsh web` 才生效：

```sh
dsh plugin --profile web add dshmarket     # profile 名按你的宿主填（如 web / tui）
```

**找插件**比装插件麻烦，这是 DSH 与其他工具最大的差别：插件页的**发现**标签默认不出现，得先在「实验性插件」里打开**自定义插件索引**组合包；而且 ⚠️ **官方不内置任何索引源**，必须自己添加一个 format-1 的 JSON 索引 URL 才有东西可浏览。所以下面这些「索引源」比单个插件更值得先配好：

| 项目 | 实测 star | 作用 | 怎么用 |
|------|-----------|------|--------|
| [dsh-market](https://github.com/dsh-market/dsh-market) | 12.5K star | 可视化插件市场：浏览 / 搜索 / 一键装，同一份目录兼作索引源，另有主题一键切换 | `dsh plugin --profile web add dshmarket`；或把索引 `https://cdn.jsdelivr.net/npm/dsh-plugin-catalog/index.json` 添加进「发现」 |
| [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 24.7K star | 人工精选清单，按用途分类，适合上手前先扫一遍 | 索引源 `https://awesome-dsh-plugin.com/index.json` |
| [DSH Desktop](https://github.com/anywhere-labs/dsh-desktop) | 36.1K star | 把桌面端本身也做成插件，补 GUI 与常驻体验 | 见仓库 README（非插件索引，属宿主外壳） |

三点实践经验：

- **索引源优先用 npm / CDN 地址**：dsh-market 作者说明 dsh 对每个索引源有 15 秒超时，其 GitHub Pages 副本在部分网络下会超时，因此同目录的 jsDelivr 版本更稳
- **只加你信任的索引源**：官方文档原话是「索引是第三方内容……DSH 检查文件格式，但不验证这些声明」。安装前在确认框里核对来源是 npm 包还是某个 Git commit；`http:` 索引中途可被篡改，只走 `https:`
- **警惕「不填 Key 就能免费用前沿模型」这类插件**（如 `dsh-our-free-model`，74.3K star）：不用登录、不限量的说法通常意味着背后是共享或转售的上游凭证——违反模型厂商条款、随时可能失效，且你的对话内容会进入他人的池子。真要用前沿模型，走章节三的官方 API 或章节二的 Coding Plan 更稳

> 插件与宿主版本绑得很紧：包内声明 `engines.dsh` 兼容范围，**DSH 安装时会再检查一遍**（没有该字段则退回检查 `@deepseek-ai/dsh*` 的 peer 依赖）。所以在 rc 阶段装插件前，先确认它支持的版本区间覆盖你当前的 0.2.x。

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
| **[cc-switch](https://github.com/farion1231/cc-switch)**（154.5K star） | 跨平台桌面应用，一键切换 Claude Code / Codex / OpenCode / OpenClaw / Antigravity CLI，免去终端手动切换的繁琐 |

