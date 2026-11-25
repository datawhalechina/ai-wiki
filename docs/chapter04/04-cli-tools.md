# 四、CLI 种类

[← 上一章：三、三方模型（API）](../chapter03/03-model-api.md) | [返回总览](../index.md) | [下一章：五、好用的 Skill →](../chapter05/05-skills.md)

CLI（命令行界面）AI 工具是终端中的 AI 编程助手，支持自然语言驱动开发全流程。

**提示**：开源 CLI 工具生态还在快速演进，建议关注各工具的插件体系和 MCP 集成能力。

## 主流 AI CLI 工具

| 工具                                                         | 厂商      | 特点                                                         |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| **[Claude Code](https://code.claude.com/docs/zh-CN/overview)** | Anthropic | 终端级深度编码助手，最新 **2.1.332**（2026-11-25）：① **MCP 服务器可以带技能了（beta）**——装完在 `/` 菜单里显示为 `server:skill`，与其他来源的技能区分开；② 新增 **`PreSkillShellCommand` 钩子**，能在技能或命令加载时**拒掉其中的内联 shell 命令**（旧版遇到该配置只会在启动时弹个对话框）；③ 多会话场景补了「**Always deliver**」（其他会话压着待投递的消息可强制送达）与一行**常驻页脚**：当会话被标记跑在另一个模型上时提示，直到你用 `/model` 选定为止；④ 观测面上 OpenTelemetry 新增 `assistant_response` 事件，覆盖 `SendUserMessage` / Cowork 消息工具发出的文本；⑤ 启动头开始显示 **Cyber Verification Program 的访问层级**（在用 claude.ai 账号登录且该档适用于当前模型时，跟在模型名旁边）。这一版主要在收稳定性窟窿：**命名管道无人写入时**（如被锁的密钥管理器挂载的 `.env`）Read / `@` 提及 / 压缩会**挂死**，现在 20 秒后失败；**hook 无休止输出**会造成卡死与内存失控，hook 阻断或失败时日志过大还会撑爆上下文（超约 5 万字符改为截断）；**本地 MCP 服务器刷屏 stdout** 会冻住终端且吃掉 Ctrl+C；权限规则或 hook 条件里带多个通配符时对长命令求值会卡住；SSE MCP 的事件流被切断后换端点回来，此前必须手动重连否则所有工具调用都挂。另修三处会误导人的判断：`claude auth login` 在 claude.ai 登录**没能落盘**时仍报「Login successful」（现在退 1 并说明查什么）、反复自动压缩失败后不该结束的回合被「Prompt is too long」掐断、以及把「You've used…」开头的正文字误判成用量超限报错。云侧模型名解析也修了一批：`sonnet` 别名在 Bedrock Mantle 上曾**错解析到 Haiku 4.5**、`opus` 在拒答的网关后面不会顺次降档、`--fallback-model` 里写家族名在 `availableModels` 只放旧版时会被丢掉。前一版 **2.1.331**（11-23）：**Code Mode 扩到四家托管云**（Amazon Bedrock、Google Cloud 的 Agent Platform、Microsoft Foundry 与 AWS 上的 Claude Platform），`claude doctor` 新增 **API 连通性检查段**、插件清单支持 **`optionalDependencies`**；修本地 / WebSocket MCP 返回格式异常时工具调用**卡住最长 30 分钟**、中断的插件更新留半截目录。另预告 **2026-11-30 起**托管 `extraKnownMarketplaces` 里的插件市场默认自动更新，要关需在该条目上设 `"autoUpdate": false`。再前一版 **2.1.330**（11-20）：内置画图 mod **easel**、接上 **Enterprise Admin Console** 组织、`/loop` 最长运行期 **7 天放宽到 30 天**、自托管 runner 增 `--start-dir`，并**把 2.1.329 撤掉的 `max_tokens` 超限自动重试加回来**。Stack Overflow 2026 开发者调查中采用率 **65.5%**，为同类最高（Codex CLI 29.5%），156.6K GitHub 星标 |
| **[Codex CLI](https://openai.com/codex/)**                   | OpenAI    | 最新 **0.172.0**（2026-11-24）：**Tab 补全斜杠命令参数**（`/mcp lo` 补成 `/mcp login`）；搜索结果与转录里的 **thread 链接可直接打开**，跳到已存对话或嵌套 agent；agent 指挥中心用 **`Shift+Up` / `Shift+Down`** 在任务组之间跳；带缓存工具清单的 **stdio MCP 服务器改为首次工具调用时才启动**（此前启动即拉起，启动更快）；`config.toml` 可为单个 connected app 工具指定**审批复核人**；app-server 客户端在安装 / 登录时可选 **Amazon Bedrock Runtime**。修了 `codex exec resume` 不还原沙箱权限 / 工作目录 / workspace roots、客户端与服务端跨操作系统时远端会话丢可写路径、provider 报错要等流结束才显示（现在还点明撞的是哪条 API 额度上限）、打断父轮会丢掉子 agent 已排队的回复。**捆绑的 `openai-docs` skill 已补 GPT-6.2 Astra / Sol 的迁移指引**（端点选择与工具调用要求）；工程上 **Code Mode 的宿主连接全部改走 gRPC**，`code_mode_host_grpc` 设置废弃。前一版 **0.171.0**（11-20）：**模型目录正式纳入 `gpt-6.2-sol` / `gpt-6.2-astra`，且 Sol 是目录里的默认项**——这是 6.2 发布后官方第一次把默认值写进 release note；**TUI 工作区默认开启**（侧边可搜的文档预览、图片预览、subagent 转录与主对话并排）；非 Vim 输入模式支持自定义 **undo / redo 快捷键**，附件与大段粘贴一起回滚；新增 `codex exec --remote <ADDR>`（在已有 app server 上起或续非交互会话）、`/rc` 与 `/remote`（管本地 remote control、显示设备配对码）、`/statusline`（自选或自写 MCP 状态行）。修了切会话时草稿 / 排队追问 / 中断输入没跟回原线程、改工作目录会丢权限配置、上一轮迟到的完成事件取消新一轮审批，以及 IdP 不发 refresh token 时的企业 MCP 登录。前一版 **0.170.0**（11-18）：TUI 里的实时语音通话改走 **WebRTC 协商**、OpenTelemetry 导出器支持自动刷新的鉴权头、实验性支持「不同环境下的同名 MCP 服务器共存」；修 MCP OAuth 在取消/登录/登出时的凭证竞态、Cloud 会话断流后的自动重连、Windows 沙箱的文件替换与权限保留。默认模型自 0.153.4 起是 **`gpt-6-astra`**，11-17 起 **`gpt-6.2-astra` / `gpt-6.2-sol` 已可通过 `/model` 选用**，**0.171 起模型目录的默认项换成 `gpt-6.2-sol`**（官方原话 default catalog selection）——但「目录默认」不等于已存的配置会被改写，升级后仍建议用 `/model` 确认自己挂在哪一代。客户端默认挂在 **Low 推理档**防额度超支；**0.165 起接入 GCP Vertex AI 作为内置 provider**（`model_provider = "gcp"`），模型目录加入 **`gpt-6.1-terra`**；**GPT-5.5 已于 2026-10-14 从 ChatGPT 登录会话退役**（API 与 API-key 会话不受影响），官方建议把保存的设置与脚本指向 `gpt-6.1-sol`。0.167 新增 agent 指挥中心（`codex agents --no-daemon`）、跨后端切换保留草稿、10 个 `/presets` 槽位；**0.168 把 provider 选择搬进 TUI**（Sessions → Model providers 选默认）、侧栏会话可拖拽缩放（`leader z`）、支持音频附件与动图；**0.169 扩成多标签侧栏、可按名称 / 提示预览 / 工作目录搜索历史任务、终端内增改自定义 provider（SSH 可走 device code）**，并让 `codex exec` 在不可信目录默认关闭项目配置与 MCP（需显式 `--trust`） |
| **[OpenCode](https://opencode.ai/)**                         | 开源      | 228.5K GitHub 星标                                            |
| **[DSH](https://github.com/deepseek-ai/deepseek-harness)**   | DeepSeek  | 285.4K GitHub 星标。开源 Agent 运行时，主打「一切皆插件」——模型、工具、循环、UI 均可替换重组；**当前 `0.2.2-rc`（npm `latest` 与 `next` 均已指向 `0.2.2-rc.5`），仍属开发者预览，官方明示会出现破坏兼容性的变更、不可用于生产**；插件怎么装、索引源加哪个见下文「DSH 插件推荐小结」 |
| **[Pi](https://github.com/earendil-works/pi)**               | Earendil Works | 123.3K GitHub 星标。极简底座——只保留读/写/改文件与跑命令四个工具；支持单会话内跨供应商接力（Claude 做到一半转给 DeepSeek 继续） |
| **[Antigravity CLI](https://antigravity.google/)**           | Google    | 命令名 `agy`，Gemini CLI 的继任者，已全面开放（第三方多标注为 preview，**官方未使用 GA 字样**）。**Gemini CLI 已于 2026-06-18 对免费 / Google AI Pro / Google AI Ultra 用户停止服务**，企业版（Code Assist）不受影响。个人档 **$0/月**，无需信用卡 |
| **[Qoder CLI](https://qoder.com)**                           | Qoder-AI | Agentic Coding Platform，支持 CLI 和 IDE，自主编程模式，CodeReview 能力 |
| **[CodeBuddy](https://codebuddy.cn/)**                       | 腾讯      | 命令行中用自然语言驱动开发全流程                             |

## CLI 模型支持矩阵

CLI 工具最关键的分化点是**能不能换模型**——这直接决定你会不会被单一厂商绑定，以及能否用国内 Coding Plan 降低调用成本：

| 工具 | 默认模型 | 可切换范围 | 自由度 |
|------|---------|-----------|--------|
| **Claude Code** | Anthropic Claude（现役 Opus 5.5） | 原生仅 Anthropic；**可通过 Base URL 指向第三方端点**（阿里云、腾讯云 Coding Plan 均支持此用法） | 中 |
| **Codex CLI** | **`gpt-6.2-sol`**（0.171 起目录默认） | `gpt-6.2-astra`（旗舰，$8/$40）、`gpt-6.1-sol`（复杂编码与 agentic 流程）、`gpt-6.1-terra`（视觉推理 / computer use / 写作）、`gpt-6-sol` / `gpt-6-luna`（存量档位）；另有 GCP Vertex AI 与 Amazon Bedrock 渠道 | 低（仅 OpenAI） |
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
| Claude Code | 否 | Claude 系列 | 深度集成 | 极高（156.6K star） | 低 | 深度编码、大型项目重构 |
| Codex CLI | 开源 | **`gpt-6.2-sol` 默认，可切 6.2 Astra / 6.1 Sol / 6.1 Terra / Luna** | 支持 | 高 | 低 | OpenAI 生态、多模型切换 |
| OpenCode | 开源 | 多模型自由 | 支持 | 极高（228.5K star） | 中 | 开源优先、社区驱动、自定义工作流 |
| Antigravity CLI | 否 | Gemini + Claude + gpt-oss | 支持 | 中 | 低 | Google 生态、多模态任务、免费档 $0（2026-06 起取代 Gemini CLI） |
| Qoder CLI | 否 | 多模型支持 | 支持 | 中 | 低 | 自主编程、CodeReview、IDE+CLI 双模式 |
| CodeBuddy | 否 | 混元+DeepSeek | 支持 | 中 | 低 | 腾讯生态、全流程开发 |
| DSH | 开源（MIT） | 近 40 家提供方 | 支持 | 高（285.4K star） | 中 | 插件化改造、自定义 agent 运行时（预览版） |
| Pi | 开源（MIT） | 多供应商（20+） | 支持 | 高（123.3K star） | 中 | 极简底座、自建工作流、跨模型接力 |

## 选型建议

- **追求极致编码体验** → **Claude Code**：Stack Overflow 调查中采用率 65.5%，Agent 能力强，适合大型项目
- **开源自由 + 多模型切换** → **OpenCode**：社区最活跃的开源 CLI，可对接任意模型
- **OpenAI 深度用户** → **Codex CLI**：0.171 起目录默认 **`gpt-6.2-sol`**（$2/$10），最难的任务切 `gpt-6.2-astra`（$8/$40），视觉与电脑操作用 `gpt-6.1-terra`（$1/$5）
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
| [dsh-market](https://github.com/dsh-market/dsh-market) | 13.2K star | 可视化插件市场：浏览 / 搜索 / 一键装，同一份目录兼作索引源，另有主题一键切换 | `dsh plugin --profile web add dshmarket`；或把索引 `https://cdn.jsdelivr.net/npm/dsh-plugin-catalog/index.json` 添加进「发现」 |
| [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 25.4K star | 人工精选清单，按用途分类，适合上手前先扫一遍 | 索引源 `https://awesome-dsh-plugin.com/index.json` |
| [DSH Desktop](https://github.com/anywhere-labs/dsh-desktop) | 36.6K star | 把桌面端本身也做成插件，补 GUI 与常驻体验 | 见仓库 README（非插件索引，属宿主外壳） |

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
| **[cc-switch](https://github.com/farion1231/cc-switch)**（156.3K star） | 跨平台桌面应用，一键切换 Claude Code / Codex / OpenCode / OpenClaw / Antigravity CLI，免去终端手动切换的繁琐 |

