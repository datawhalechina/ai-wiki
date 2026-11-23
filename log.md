# 更新日志 (Changelog)

> 本项目所有值得关注的变化都会记录在此文件中。

---

## 2026-11-23 23:00 · 每日时效更新

> 例行日增量：核对 11-22 之后的官方口径。今日有两处实质变化——**智谱在晚间静默放出 GLM-5.4**（首个 Loop Transformer 旗舰，但 API 未开放），**OpenClaw 发 v2026.11.7**（纯可靠性版）。其余全线静止。另把连续四天 404 的 `microsoft/agent-framework` 链接改指官方文档。

### 新增

- **章节一 / 最新动态**：新增 **2026-11-23 v2026.11.7** 一行——官方口径 **390 个 PR**，六条 Highlight 全是可靠性（Gateway 重启后接回被中断的回复与子任务结果、自动化失败可由所属会话修复并区分「已恢复 / 主动跳过」、Git 与 npm 更新可穿过 schema 变更与数据库繁忙、慢文件系统期间 Gateway 保持响应、浏览器短码配对、ChatGPT 订阅模型目录直连不必等发版）。Changes 段**再列 #175837 那三条破坏性 SDK 变更**（与 11.5 同一 PR），从 11.5 以下升级者仍需先读；捆绑 Codex runtime **0.169.0 → 0.170.0**（ACP 仍 2.2.2）。依据：`gh api repos/openclaw/openclaw/releases/tags/v2026.11.7`（11-23 01:33Z，"390 in-range PRs"）+ `npm view openclaw dist-tags`（latest 2026.11.7、extended-stable 2026.10.33、beta 2026.11.10-beta.2）
- **章节三 / 智谱行**：新增 **GLM-5.4**（2026-11-23，首个 Loop Transformer 旗舰：GLM-5 基座里 **28 层循环跑两轮**，门控渐进写回 + 跨轮共享 KV Cache + 复用稀疏注意力索引，约 **750B** 基座拿到「2T–3T 级」智能；1M 上下文 / 128K 输出；GLM-5.x 首个能吃图；非高峰 200 token/s、高峰 70–80 token/s）。**明确标注 API 未开放、无公开 per-token 价格**，目前仅 Coding Plan 与 ZCode / Trae / WorkBuddy / Qoder 等平台可用。依据：智谱官方博客 `zhipuai.cn/zh/research/164`（11-23）+ `docs.z.ai/guides/llm/glm-5.4.md`（Context 1M / Max output 128K / 输入含 Video·Image）+ `z.ai/subscribe` 页面标题已改为 "Powered by GLM-5.4 & GLM-5.3-Flash"

### 变更

- **章节二 / GLM Coding Plan 行**：模型列 **`GLM-5.3` → `GLM-5.4`（11-23 起全量开放）+ GLM-5.3 + GLM-5.3-Flash**，并补「周额度档 V2 / V3 / 团队版的 GLM-5.4 额度提到 5.3 的 **1.5 倍**」。价格列（118 / 538 / 1078 元）未动——官方未宣布调价
- **章节三 / 选型建议「预算敏感的中文任务」**：补一句说明——GLM-5.4 虽是旗舰但只有 Coding Plan 能用，按 token 计价的场景仍走 GLM-5.3；同页价格对比表内仍留 GLM-5.3（$1.40/$4.40），因 5.4 无 API 无价
- **章节七 / ZCode**：适配模型 **GLM-5.3-Flash → 补 GLM-5.4 当日同步上线**（官方首发伙伴之一）；工具对比表模型列 **GLM-5.3 → GLM-5.4**

### 修复

- **章节八 / 章节十三**：`Microsoft Agent Framework` 链接由 `github.com/microsoft/agent-framework` 改指官方 Learn 概览页。**与 11-20 ~ 11-22 三天「判临时不可达、不改」的判断有出入**——原因：今天 `git ls-remote` 直接返回 `Repository not found`，GitHub API 也 404（改名会 301 跳转，故不是改名），且 `microsoft/agent-framework-go`、`microsoft/Agent-Framework-Samples` 两个周边仓库同日 200 → 判主仓已不再公开，属真实死链而非限流。官方 Learn 页面仍正常（200）且正文仍在引用该 GitHub 路径，属微软侧文档滞后，故改指文档并在 ch08 行内注明

### 工程

- 外链体检 **186 条**：19 条非 200 中，401（`api.deepseek.com` 三个端点，无 Key）、403（arena.ai、claude.ai、producthunt、知乎 ×5）、521（CSDN 反爬）、429（cursor.directory）均属已知反爬；4 条 `000` 经单条复检全部 200（并发超时，非死链）
- 核对无变化：Claude Code 2.1.330、Codex 0.171.0（alpha 0.173.0-alpha.4 未转正）、OpenCode 1.19.6、DSH `latest`/`next` 均 0.2.2-rc.5（alpha 0.2.3-alpha.2）、Antigravity CLI 1.5.12 + App 2.34.0、Cursor changelog 停 11-06、OpenClaw extended-stable 2026.10.33
- 核对无变化（模型侧）：OpenAI changelog 顶部仍是 11-19 的 GPT-Live-1.1、弃用表 6.0 / 6.1 未进名单；Google changelog 顶部仍是 11-19 的 Genie 4 GA；Anthropic release notes 顶部 11-17（linked billing）、四档模型未变；DeepSeek changelog 停 11-13；Kimi 仍 K3.1 Pro；MiniMax 模型发布页停 11-10；Mistral 仍 Large 4
- `npm run build` 通过（VitePress 1.6.4，2.54s）

---

## 2026-11-22 23:00 · 每日时效更新

> 例行日增量：核对 11-21 之后的官方口径。**模型与工具版本今日全线静止**——Claude Code 仍 2.1.330、Codex 0.171.0（alpha 0.173 未转正）、OpenClaw 11.6、Antigravity CLI 1.5.12 / App 2.34.0、OpenCode 1.19.6、Pi 0.70.6、DSH 全预发布；OpenAI / Anthropic / Google / DeepSeek 的模型表与弃用表均无新增条目。实质变化在**接口行为**：OpenAI 为 GPT-6.2 补发的迁移指南把几条会静默抬高成本的改动写成了硬要求，此前正文只讲了价格与档位，没讲这些。

### 新增

- **章节三 / 国际表格之后**：新增小节「**OpenAI：迁到 GPT-6.2 的四个硬变化**」，记四条官方要求——① 从 6.2 起，Responses API 在**前缀编辑**（改动较早的 developer 消息或 tool call）、跨模型切换（含降级）、终端用户或组织变更后**丢弃 reasoning items**，质量下滑且重复劳动多烧 token，保持前缀不变才能同时保住推理与 prompt 缓存；② 顶层 `instructions` 改为在 input **之后**追加，可复用指令须写成 input 里的第一条 developer message 才进缓存；③ `temperature` / `top_p` / `logprobs` / `top_logprobs` **不再支持**，Responses 侧还要从 `include` 去掉 `message.output_text.logprobs`；④ effort 推荐起点为新接入 `medium`、原用 `none` / `minimal` 者改 `low`。并补 Astra / Sol 对审核组织支持**零数据留存（ZDR）**、开启后 `store` 视为 `false`、多轮须按序回传含加密 reasoning 的 output items。依据：官方《Using GPT-6.2》迁移指南原文（`developers.openai.com/api/docs/guides/latest-model`）三节 "Prefix edits" / "Changes to the instructions field" / "Unsupported parameters"

### 修复

- **章节四 / DSH 行**：`latest` 口径 **`0.2.2-rc.1` → `0.2.2-rc.5`**，并改为「`latest` 与 `next` 均已指向 rc.5」。原因：同页「DSH 插件」小节 11-18 已写「两个 dist-tag 同时指向 rc.5」，与首表自相矛盾——是上次只改了正文没回扫表格的老毛病。依据：`npm view @deepseek-ai/dsh dist-tags` 实测 `latest: 0.2.2-rc.5`、`next: 0.2.2-rc.5`（另有 `alpha: 0.2.3-alpha.2`，预发布不写）

### 工程

- 外链体检 **186 条**：4xx/5xx 全部为已知反爬或平台侧限流（知乎 403、claude.ai 403、producthunt 403、cursor.directory 429、arena.ai 403），非死链
- `microsoft/agent-framework` **连续第三日返 404**，同日 Microsoft Learn「Agent Framework」文档页与 Samples 仓库 homepage 仍指向该地址 → 维持「不改链接、继续复查」判断
- `awesome-dsh-plugin.com/index.json` 与 `cdn.jsdelivr.net/npm/dsh-plugin-catalog/index.json` 今日 404，但 `dsh-market` 仓库 README 仍把这两条列为官方索引源 → 判上游暂不可达，不改
- `npm run build` 通过（VitePress 1.6.4，3.88s）

---

## 2026-11-22 20:30 · 每周 star 专项刷新

> 例行周增量，只刷 star 数字，不动版本号 / 价格 / 模型清单。

### 工程

- `scripts/update_stars.sh --apply` 刷新 **39 处 / 7 个文件**（ch01、ch04、ch05、ch06、ch08、ch09、ch10），清单 51 条 / 41 个仓库，`--check` 全绿（51 条已是最新，退出码 0）
- 涨幅最大三家：**`deepseek-ai/deepseek-harness` 281.4K → 285.4K**、**`anthropics/skills` 194.9K → 198.7K**、**`ChromeDevTools/chrome-devtools-mcp` 56.6K → 58.8K**；旗舰 `openclaw/openclaw` 394.5K → 395.0K（破 395K）
- `microsoft/agent-framework` 本周仍返 404（`gh api` 获取失败，跳过该条）。官方文档与 `Agent-Framework-Samples` 仓库 homepage 仍指向该地址，`microsoft/autogen` 同日正常，维持「不改链接、待复查」判断；页面上的 `14.7K star` 未动
- 清单无新增：本周（11-16 ~ 11-21）没有再出现带 star 的新工具条目，11-21 已把 4 条 DSH 插件纳入
- `npm run build` 通过（VitePress 1.6.4，2.63s）

---

## 2026-11-21 23:00 · 每日时效更新

> 例行日增量：核对 11-20 之后的官方口径。模型侧继续静止——OpenAI、Anthropic、Google、DeepSeek 四家的 changelog 最新条目分别停在 11-19、11-17、11-19、11-13，没有新旗舰、没有新弃用。实质变化在工具朝：Claude Code 又出一版（这次有功能不是纯修复）、Antigravity App 支持 MCP Apps。另把昨天「有发布无官价、所以没写」的 GPT-Live-1.1 补上——官方定价页今天已有按分钟单价。

### 新增

- **章节三 / OpenAI 行尾部**：新增语音线 **GPT-Live** 口径——**GPT-Live-1.1（2026-11-19）** 改进多语种下的发音、口音一致性与转写，**按秒计费**，活跃档 **$0.05 / 分钟**、待机档 **$0.02 / 分钟**（与 GPT-Live-1 同价）。依据：OpenAI changelog 11-19 条目（`gpt-live-1.1`，`v1/live/sessions`）+ 官方定价页 GPT-Live 小节（"Active rate / Standby rate: $0.05 / $0.02 per minute"，"bills voice sessions per second"）。**与上次判断的出入**：11-20 记「只有二手来源的价格，不写」——当时定价页尚未列出该模型；今天定价页已给出官方三值，故按一手来源补写

### 变更

- **章节四 / Claude Code 行**：`2.1.329` → **`2.1.330`（2026-11-20）**，前置四件事：① 新增内置画图 mod **easel**——被要求画图、或 MCP 返回指标结果时自动出图（Pro / Max，Team / Enterprise 视地区，macOS 与 Linux），可在 `/config` 关掉自动图表；② **可登录 Anthropic Enterprise Admin Console 管理的组织**，`claude auth login` 后套用组织设置与云厂商 / 网关；③ **定时任务与 `/loop` 最长运行期 7 天 → 30 天**（旧任务仍按 7 天）；④ 自托管 runner 新增 `--start-dir` / `SELF_HOSTED_RUNNER_START_DIR`。修掉压缩超长对话后卡死数分钟、WebFetch 在某些页面卡住或返空、`ExitWorktree` 删掉另一会话正在用的 worktree、多进程同时保存用户设置互相覆盖、`/stats` 按 UTC 而非本地时区统计日活。依据：官方 `CHANGELOG.md` 2.1.330 条目 + `gh api repos/anthropics/claude-code/releases`（v2.1.330，2026-11-20T22:32Z，`prerelease=false`）+ `npm view @anthropic-ai/claude-code version`（2.1.330）
- **章节四 / Claude Code 2.1.329 段**：补一句 **`max_tokens` 自动重试在 2.1.330 又被加回来了**——2.1.329 撤掉的那条重试只活了一天。依据：2.1.330 条目 "Reverted 2.1.329's removal of the automatic retry when `max_tokens` exceeds a model's or gateway's limit"
- **章节七 / Antigravity 行**：补 App 版本口径——**2.34.0（2026-11-20）支持 MCP Apps**（MCP 服务器可把可直接渲染的界面带回对话），同版把 **Gemini 4 Neon 与 Orchestrator 开放给符合条件的付费消费档**，15 项改进 + 24 项修复。依据：`antigravity.google/docs/changelog`「Antigravity App v2.34.0 · November 20, 2026」条目原文

### 修复

- **章节四 / Codex 默认模型三处下游表述**：11-20 只改了正文（`0.171 起目录默认 gpt-6.2-sol`），漏了同一文件里三处仍写旧默认值——**模型支持矩阵**「默认模型 `gpt-6-astra`」→ **`gpt-6.2-sol`（0.171 起目录默认）**，可切换范围补 `gpt-6.2-astra`（旗舰 $8/$40）；**选型对比表**「`gpt-6-astra` 默认，可切 6.1 Sol / 6.1 Terra / Luna」→「`gpt-6.2-sol` 默认，可切 6.2 Astra / 6.1 Sol / 6.1 Terra / Luna」；**选型建议**「默认 `gpt-6-astra`，建议切 6.1 Sol」→「默认 `gpt-6.2-sol`（$2/$10），最难的任务切 6.2 Astra（$8/$40），视觉 / 电脑操作用 6.1 Terra（$1/$5）」。依据：Codex 0.171.0 release note「Sol as the default catalog selection」+ 官方定价页两档价格；原因：昨日改动只在表格详情单元格内落笔，未回扫同页三处摘要

- **章节十三 / 实战项目行**：外链体检发现 `github.com/langchain-ai/langchain/tree/master/templates` **已 404**——`templates` 模板目录从 LangChain 主仓移除（默认分支仍是 `master`，顶层只剩 `libs` / `openwiki` 等，`libs/` 下也无 templates；旧文档页 `python.langchain.com/docs/concepts/templates` 同时 301 回 overview）。**旧值 → 新值**：`LangChain Templates`（深链）→ **`LangChain 官方仓库`**（根地址，实测 200），说明改为「原 `templates` 目录已移除，旧链接已 404」

### 工程

- `npm run build` 通过（VitePress 1.6.4，2.21s）
- 按约定**未跑** `scripts/update_stars.sh`、未核 `stargazers_count`、未改任何 star 数字（star 由每周日的独立任务负责）
- 外链全量体检 185 条（全书去重）：除 `api.deepseek.com` 三个端点 401（需鉴权）、`arena.ai` / `claude.ai` 403、`cursor.directory` 429（反爬 / 限流）外，**2 处 404**——`langchain/tree/master/templates`（已在「修复」中处理）与 `microsoft/agent-framework`（**未改动**：微软官方文档 `learn.microsoft.com/agent-framework` 与 `Agent-Framework-Samples` 仓库的 homepage 仍指向该地址，同日 `microsoft/autogen` 正常 200，故判为临时不可达或刚发生变更，待次日复查）；`easy-vibe` 一次 000 复检 200，属瞬时超时

---

## 2026-11-20 23:00 · 每日时效更新

> 例行日增量：核对 11-19 之后的官方口径。模型侧全线静止（四家旗舰的价格、上下文、弃用表都没动），实质变化集中在工具版本与世界模型的 API 化：Codex 换代并把默认模型写进 release note、OpenClaw 出补丁版、Genie 4 从「订阅者可用」变成「API 可买」。

### 新增

- **章节一 / 最新动态**：新增 **2026-11-19 v2026.11.6** 行（当前 stable / npm `latest`，**386 个 PR / 157 位贡献者**、48 个直接提交）。三条行为变化：① macOS / Linux 上一部分原本自动执行的 shell 命令改为弹审批或被拒（安全修复）；② 默认日志迁到所选状态目录，外部日志收集器需改路径或改用 `openclaw logs`；③ Git 更新默认不再构建 TypeScript 声明，需 `.d.ts` 要设 `OPENCLAW_RUN_NODE_SKIP_DTS_BUILD=0`。另记两条值得警觉的修复（更新技能会把 API Key 引用静默替换成明文、Doctor 与更新迁移错误合并 API 与 Claude/Gemini CLI 路由），并注明捆绑 Codex 升到 0.169.0、Grok OAuth 代理 1.0.13、`beta` 标签为 2026.11.10-beta.1。依据：`gh api repos/openclaw/openclaw/releases/tags/v2026.11.6`（386 PR / 157 contributors）+ `docs.openclaw.ai/releases/2026.11.6`（行为变化与修复清单）+ `npm view openclaw dist-tags`（latest / extended-stable 2026.10.33 / beta 三值互证）
- **章节三 / 世界模型 · Genie 4**：补 API 侧口径——**2026-11-19 起 `genie-4` 在 Interactions API（`v1beta`）GA**，只开付费档 **$1.50 / 百万输入、$9.00 / 百万文本输出、$17.50 / 百万视频输出**（约 $0.10/秒，含立体声），输出 **24 fps 16:9 可操纵视频 + 48 kHz 立体声**、走 WebRTC / WebSockets 流式，可用 WASD / 方向键与中途文本事件实时改机位。依据：Gemini API 官方 release notes 11-19 条目（"Genie 4 (`genie-4`) generally available (GA)"，含三条单价）

### 变更

- **章节四 / Codex CLI 行**：`最新 0.170.0（2026-11-18）` → **`0.171.0`（2026-11-20）**，要点前置为「**模型目录纳入 `gpt-6.2-sol` / `gpt-6.2-astra`，Sol 是目录默认项**」，另补 TUI 工作区默认开启、undo / redo 快捷键、`codex exec --remote`、`/rc`、`/remote`、`/statusline`。依据：`gh api repos/openai/codex/releases/tags/rust-v0.171.0`（00:44Z，`prerelease=false`）+ `npm view @openai/codex dist-tags`（`latest=0.171.0`，`alpha=0.173.0-alpha.1` 不计）
- **章节四 / Codex 默认模型口径**：`0.170 的变更记录没提默认值，6.2 要用 /model 自选、别假设会跟着换` → **`0.171 起模型目录默认项是 gpt-6.2-sol`**（官方原话 default catalog selection），保留「目录默认 ≠ 已存配置被改写」的提醒。**上次判断错在哪 → 11-17 至 11-18 看的是 0.170 的 release note，它确实没写默认值，据此写成「官方未交代」；0.171 的 New Features 第一条直接写明 Sol 为 default catalog selection**，这次以该条为准
- **章节四 / Claude Code 行**：`2.1.328` → **`2.1.329`（2026-11-19）**：`/tasks` 升为会话级总览（定时任务 / `/loop` 唤醒 / 目标 / 对话分叉）、`/mcp` 服务器页新增 Server message 行显示被拒 HTTP MCP 的 JSON-RPC 错误、`/status` 增 Marketplace auto-update 行、OpenTelemetry 与 Code Mode 可同时开；修 `~/.claude.json` 读不到时保存会清空 / 重置（会丢配置）、macOS Keychain 只读不写导致反复登出、`/teleport` 选云会话顶掉当前对话、`application/octet-stream` 的 PDF / 图片 / Office 被存成 `.bin`，并撤掉 2.1.326 在 `max_tokens` 报错处的自动重试。2.1.328 压成「前一版」保留。依据：官方 `CHANGELOG.md` 2.1.329 条目 + `npm view @anthropic-ai/claude-code time`（2.1.329 = 2026-11-19T18:40Z）
- **章节一 / 时间线口径**：11-17 行的「当前 stable」→ **「11-17 起为 stable，已被 11.6 接替」**；11-18 行的「stable 未动，仍是 11.5」→ **「当天 stable 仍是 11.5，次日由 11.6 接替」**。原因：原写法是当日快照，留到第二天会与表头新行自相矛盾

### 工程

- `npm run build` 通过（VitePress 1.6.4，2.40s）
- 按约定**未跑** `scripts/update_stars.sh`、未核 `stargazers_count`、未改任何 star 数字（star 由每周日的独立任务负责）
- 外链无新增，未触发体检

## 2026-11-19 23:00 · 每日时效更新

> 例行日增量：核对 11-18 之后的官方口径。主线是**Google 补上中间档**——Gemini 4 Neon 直接 GA，位置明确「夹在 Hydrogen 与 Carbon 之间」，顺带把 Genie 4 从「10 月发布」推进到「已向 AI Ultra 开放」；工具侧是 Claude Code 与 Antigravity CLI 的连续补丁。

### 新增

- **章节三 / 编程对比表**：新增 **Gemini 4 Neon** 行（$3 / $15，1M，快）。依据同下条
- **章节三 / Gemini 行**：新增「同日 API 另开一项能力」——**Word / PowerPoint / Excel 等 Office 与 OpenDocument 文件可直接传**，可按页码范围、工作表页签、单元格区域、时间段或内容层（页图 / 提取文本 / 公式 / 视频逐字稿）切片计费。依据：官方 release notes 11-18 条目「Multimodal file processing and slicing」

### 变更

- **章节三 / Gemini 行**：`三档并列（Argon / Carbon / Hydrogen）` → **四档**，补 **Gemini 4 Neon**（**2026-11-18 直接 GA**，$3/$15、缓存 $0.15 且**只支持隐式缓存**、统一 1M 上下文、长输出可续写到 1M（同步档默认 64K）、四档思考默认 `high`、**无免费档**、同日成为 Antigravity 的默认模型）。依据四处一手互证：`/docs/changelog` 11-18 条目明写 "generally available (GA)" 与价格档位、`/docs/pricing#gemini-4-neon`（逐档价 + Batch $1.50/$7.50）、`/docs/whats-new-gemini-4-neon`（定位原文 "sits between Hydrogen and Carbon"）、`/docs/deprecations`（Neon 11-18 发布、四个 Gemini 4 档位**均无下线日**）
- **章节三 / Gemini 行 · 促销窗口口径**：`$2/$10 推广价、2026-11-30 后恢复 $4/$20` → **只到 11-30，12-01 起 $4/$20**（缓存输入同步 $0.10 → $0.20）。官方定价页原文是 "through November 30, 2026 / starting December 1, 2026"，原写法容易读成「11-30 当天就涨」
- **章节三 / 对比表下方注释**：`Hydrogen 是常规价，不在此列` → 补 Neon 同为常规价；**Orchestrator 的规划档 `Carbon → Neon`**（2026-11-18 起 Neon 规划、Hydrogen 执行）。依据：Antigravity 官方 changelog 11-18「Gemini 4 Neon」条 + Google 官方 whats-new 页「pair with Hydrogen in multi-model workflows」
- **章节三 /《怎么读版本号》**：同代档位一行补 Neon（`Neon / Carbon / Argon / Hydrogen`）
- **章节三 / 世界模型**：`Genie 3（11B / 720p / 24fps，2026-01 起经 Project Genie 开放）` → **Genie 4**（2026-10 发布，**11 月起经 Project Genie 向合格的 AI Ultra 订阅者开放**；架构上是「建在 Gemini 家族之上」——Gemini Omni 负责真实感、其他 Gemini 模型负责连贯性与推理，可边跑边改事件 / 机位 / 声音），Genie 3 降为上一代。依据：`deepmind.google/models/genie/` 页面正文 + DeepMind 博客索引两条（10 月 "Genie 4: A new generation of world simulation"、11 月 "Genie 4 is now available"）
- **章节七 / Antigravity 行 · CLI**：`11 月连发 10 版至 1.5.9` → **最新 1.5.12（2026-11-19）**，并补 1.5.10（11-17，`--remote-agent` 加 accept-edits 模式、Orchestrator 开放给 Gemini Enterprise / ADC）、1.5.11（11-18，subagent 标签拖拽引用、Vim 撤销语义、`agy plugin validate` 支持 `.zip` 与 GitHub URL）、1.5.12（11-19，Remote Control 并排分屏、配 `GEMINI_API_KEY` 可用 Neon、`/fork` 提速）。原「连发 10 版」这个计数无法复核，删掉改用具体版本号。依据：`antigravity.google/docs/changelog` 的 Antigravity CLI 标签页（三条均带日期，"Latest" 标在 1.5.12）
- **章节七 / Antigravity 行 · 模型列与 Orchestrator**：模型列补 **Neon** 并注明「11-18 起为没手动选模型时的默认」；Orchestrator 由「Carbon 规划、Hydrogen 执行」改为「**11-18 起 Neon 规划、Hydrogen 执行**（此前是 Carbon 规划）」
- **章节四 / Antigravity CLI 行 · 模型列**：补 `Gemini 4 Neon`，并注明 1.5.12 起配 `GEMINI_API_KEY` 也可用
- **章节四 / Claude Code 行**：`2.1.327` → **`2.1.328`**（2026-11-18，144 条修复：auto 模式的自动判断扩到 Bedrock / Google Cloud Agent Platform / Microsoft Foundry / Claude apps gateway，未指定权限模式的交互式会话直接落在 auto；MCP 工具 schema 以 `anyOf/oneOf/allOf` 开头不再整段消失，单个坏 schema 只跳过该工具；自动压缩不再复用旧系统提示词；修 zsh `=cmd` 被误展开；`mcp_tool` hook 增 `"onFailure": "block"`；自托管 runner 增三个参数与两个编排器指标）。2.1.327 的内容压缩为「前一版，侧重凭证与体检」保留。依据：Anthropic 官方 `CHANGELOG.md`（raw 源）+ `npm view @anthropic-ai/claude-code version` 双确认

### 修复

- **章节四 / DSH 版本口径**：`npm latest 仍是 0.2.2-rc.1（11-04），next 已到 rc.5` → **`latest` 与 `next` 两个 dist-tag 现在都指向 `0.2.2-rc.5`（11-18）**，即 `npm i -g @deepseek-ai/dsh` 拿到的就是 rc.5。上次判断错在哪 → 当时只查了 dist-tag 的静态值、把「latest 停在 rc.1」当成长期状态，实际 npm 在 rc.5 之后把 `latest` 一起迁了；这次用 registry 的 `dist-tags` + 各版本 `time` 两处对过

### 工程

- `npm run build` 通过（VitePress 1.6.4，2.25s）
- 外链体检：ai.google.dev（首页 / pricing）、antigravity.google、deepmind.google/models/genie、api-docs.deepseek.com 五条均 200

### 观察到但未写入

- **微软 Ignite 2026 的七款 MAI 模型**（11-17）：MAI-Code-2 称达 GPT-6.1 Sol 98% 性能、成本 40%，已在 GitHub Copilot 全档上线。**价格两套口径互相矛盾**——TechTarget 写「标准价 $1/$5」，北京商报引从业者称「$1/$5 是五折促销价，2027-05-17 起翻倍」；且 Code-2-Flash 仅 Foundry 私有预览、无公开通用 API 与定价页，先不写
- **腾讯 Q3 财报称「受先进半导体进口限制，下一代混元推出节奏会拉长」**：财报电话会口径，非产品事实，且与 Hy4 / Hy4 flash 的在役状态不冲突
- **Anthropic IPO 定价 $83 / 股**（11-19 纳斯达克挂牌）：资本市场事件，不属本书章节范围
- **MiniMax H3 Image**（11-10 开源权重图像模型）：与本章「文本 / 语音 / 视频」叙事无关，暂不单列
- **MTEB eng v2 榜首分数**：仍取不到官方 featured 榜的可引用数值，维持不写

---

## 2026-11-18 23:00 · 每日时效更新

> 例行日增量：核对 11-17 19:00 之后约 28 小时的官方口径。今天三件事——**OpenAI 把旗舰换成 GPT-6.2 双子并降价 20%**、**腾讯把 Hy4 flash 的权重放出来了**、**DeepSeek 把「模型自己触发的搜索」改成免费**。

### 变更

- **章节三 / OpenAI 行**：`四层并列（Astra / 6.1 Sol / 6.1 Terra / Luna）` → **GPT-6.2 双档置顶**：`gpt-6.2-astra`（$8/$40、缓存 $0.40，输入输出较上代降 20%、缓存降 60%）与 `gpt-6.2-sol`（$2/$10、缓存 $0.10，维持 6.1 Sol 价），均 1.05M / 128K、五档 effort、Ultrafast 加速档（2027-02-28 前 3 倍价、之后 6 倍）、**>272K 输入按长上下文另计**（Astra $16/$60、Sol $4/$15）。同时把「旧档怎么办」写清：GPT-6 Astra / 6.1 Sol / 6.1 Terra / Luna **都不在弃用名单，API 仍可调用**，6.2 是往顶上插一层而不是把旧档下线；**没有 6.2 Terra / 6.2 Luna**。依据：OpenAI 官方 changelog（11-17 条目）、`developers.openai.com/api/docs/pricing`（逐个模型核价）、`/api/docs/models`（上下文与 effort 档）、`/api/docs/deprecations`（确认 6.0 / 6.1 未被弃用）四处一手互证
- **章节三 / 编程对比表**：`GPT-6 Astra $10/$50`、`GPT-6.1 Sol $2/$10` → **`GPT-6.2 Astra $8/$40`、`GPT-6.2 Sol $2/$10`**
- **章节三 / 非编程表与选型建议**：长文档分析、多轮对话、日常编码、长文档 / 多模态四处引用同步换成 6.2（6.1 Terra 保留——视觉推理档没有换代）
- **章节三 / 《怎么读版本号》**：代际行补 `GPT-6.1 → GPT-6.2`；第 3 条原只讲「新档插在旧旗舰下方」，补上反例——**6.2 是「同名换代、往上盖一层」**，旧旗舰不下架但不再是首选，最容易按旧价做预算
- **章节三 / 腾讯混元行**：`计划开源，权重未放` → **2026-11-18 已开放权重**（Hy4-flash / Hy4-flash-FP8 / Hy4-flash-base 三个仓库，Hugging Face / ModelScope / GitCode / GitHub，腾讯 Hy License，官方同时预告 Hy4 本体也在加速开源）。依据：HF 仓库实测存在（三个 repo，11-17T03:44Z 建库）+ 腾讯官方新闻稿 + 凤凰 / IT之家 / 新浪同源报道
- **章节三 / DeepSeek 周边 API**：`Web Tools 随对话触发同样计费` → **2026-11-18 12:00（北京）起，模型侧触发的服务端搜索与抓取不再计费，只算 token**；显式调 `/v1/tools/search`、`/v1/tools/fetch` 仍按 $0.75/千次成功请求。下方「计费仍是 token 费 + 工具调用费两条线，开参数不会让工具调用变免费」整段作废并重写。依据：`api-docs.deepseek.com/quick_start/pricing` 页内公告原文
- **章节一 / 最新动态**：新增 **2026-11-18 发版 extended-stable 2026.10.33**（LTS 渠道接替 2026.9.37，stable 未动；兼容性基线锁 11.4；四条重点是有界内存、更新中断自愈、回复跨重启存活、共享会话隐私；分发只含 npm 核心包 + 官方插件 + Gateway 镜像，不含原生应用）；09-19 行的「现 extended-stable 为 2026.9.37」同步改为 2026.10.33
- **章节四 / Claude Code 行**：`2.1.326` → **`2.1.327`**（2026-11-17：`claude mcp add-json <name> -` 支持从 stdin 读 JSON，令牌不进命令行历史；`/status` 新增损坏文件 / 键位冲突 / 不可用沙箱 / 被忽略权限 / 永不匹配的 hook matcher 体检清单；`/tui classic` 成为非全屏渲染器的正式名）
- **章节四 / Codex CLI 行**：`0.169.0` → **`0.170.0`**（2026-11-18：TUI 实时语音走 WebRTC 协商、OTel 导出器支持刷新鉴权头、实验性支持跨环境同名 MCP 服务器；修 MCP OAuth 凭证竞态、Cloud 会话重连、Windows 沙箱权限保留）。默认模型表述从「仍为 `gpt-6-astra`」改为**「此前是 `gpt-6-astra`，11-17 起 6.2 两档可经 `/model` 选用」**——0.170 release notes 没有提默认值，官方 ChatGPT 文档也只写「用 model picker / `/model`」，不替它猜
- **章节四 / DSH 版本段**：`next 已到 0.2.2-rc.3（11-13）` → **`next` 迭代到 0.2.2-rc.5（11-18）**，`latest` 仍停在 rc.1

### 修复

- **Hy4 flash 参数量**：`224B 总参 / 激活 12B` → **`220B 总参 / 每 token 激活 11.3B 文本 + 0.43B 视觉`**。上次是照 11-16 新闻稿的整数口径写的；本轮权重开放后官方模型卡给了可核对的拆解——155.5B 主干 + 63.5B Engram + 0.43B ViT + 0.85B DFly2 = 220.25B，与 HF safetensors 实际统计（220,251,201,958）一致，故以模型卡为准
- **同一行的「计划开源」**：11-17 的稿子写「权重未放」当时正确，但只隔一天就失效——**权重类表述的保质期同样很短**，以后写「计划开源」一律带上核查日期

### 工程

- `vitepress build` 通过（2.13s）
- 本轮**未触碰任何 star 数字**，未运行 `update_stars.sh`——star 由独立任务每周刷新
- 外链体检：新增引用无死链（`huggingface.co/tencent/Hy4-flash`、`github.com/Tencent-Hunyuan/Hy4-flash`、`modelscope.cn/.../Hy4-flash` 均 200）
- 核过但**未改**：Anthropic 四档（Fable 5.2 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5，价与上下文一字未变）、Gemini 三档（Argon / Carbon 仍 $2/$10 推广价，11-30 后 $4/$20；Hydrogen $1.50/$7.50）、DeepSeek 两档模型价、Qwen4-Max（仍未开放权重）、Kimi K3.1 Pro（HF 建库仍是 11-02）、GLM-5.3（5.4 / 5.5 未发布）、MiniMax M3.1 Flash、Antigravity CLI 官方 changelog 仍 **1.5.9**、OpenClaw stable 仍 **2026.11.5**、ch02 各套餐刊例价

### 未写入（依据不足或不在范围）

- **Codex 默认模型是否已切 6.2**：0.170 release notes 与官方文档都没写默认值，只有「用 `/model` 选」。按「官方没说就不替它断言」处理，正文改成提示读者自己确认
- **OpenAI 的法律 / 生命科学门类变体**（`gpt-6.2-astra-law`、`gpt-6-rosalind`）：定价页确有这两行，但 24 小时内找不到发布公告或模型页，暂不单列
- **MTEB English v2 榜首**：官方 featured 榜显示 `ingot-8b-r3` 居首，但具体分数取不到（榜单前端渲染），无法与正文的 74.22 做同口径对比，故不动 ch11
- **Antigravity CLI 1.5.10**：官方 `/docs/changelog` 的 CLI 目录仍到 1.5.9，维持上轮判断不写
- **Gemini 4 Krypton / Helix**：仍只有传闻，官方模型页无此二档
- **腾讯 Hy4 本体开源**：官方只说「加速开源」，无日期无仓库，不当既成事实

---

## 2026-11-17 19:00 · 每日时效更新

> 例行日增量：核对 11-16 19:00 之后 24 小时的官方口径。今天的主角是**两家国产厂商同时把「旗舰」重新定价**——阿里把 Qwen4-Max 从预览转正式并给出书面价格，腾讯把激活参数砍到 12B 的 Hy4 flash 压到 ¥0.5/百万 token。

### 变更

- **章节三 / 阿里 Qwen 行**：`现役旗舰 Qwen3.8-Max` + `Qwen4-Max 仅 11-11 预览、11-25 下线、参数 / 价格 / 权重均未公布` → **`现役旗舰 Qwen4-Max（2026-11-16 正式发布，qwen4-max）`**：2.4T 总参 / **71B 激活**（另有 328B N-gram embedding）、Gated DeltaNet + Qwen 稀疏注意力、原生视觉（文本 / 图片 / 视频入、文本出）、1M 上下文；北京 **¥10 / ¥30**、缓存命中 ¥0.5，国际站 **$1.50 / $4.50**、缓存 $0.075；**权重不开放**，官方只说「中小尺寸 Qwen4 将陆续开源」。依据为阿里云 11-16 新闻稿、alibabacloud.com 企业版博文（11-17）、百炼价格页三处互证，另有南都 / 品玩 / IT之家同日转述。⚠️ **11-14 与 11-16 两轮都只核到 11-11 的预览公告**，据此写成「参数价格权重全无」，这次被正式发布直接推翻——`preview` 口径最多撑一周，旗舰档尤其不能只信预售稿
- **章节三 / 腾讯混元行**：原单行 Hy4 → **两档并行**，新增 **Hy4 flash（2026-11-16）**：224B 总参（含 64B Engram）/ **激活仅 12B**、多模态、1M 上下文、**¥0.5 / ¥2 / 缓存 ¥0.02**、解码 >150 tps、KV cache 为 Hy4 的 1/6；官方定位「大多数日常任务用它，长程软件工程才上 Hy4」，单任务成本 **Hy4 的 1/20** 按的是自家 WorkIndex 内部评测（已在正文标明不是公开榜单）。依据为腾讯官网中英文新闻稿 + 环球网 + 新京报三方一致
- **章节三 / OpenAI 行**：补一条**受审核的门类专用线 GPT-6 Cyber**（2026-11-05，`gpt-6-cyber`，$20/$100，1.05M 上下文 / 922K 输入 / 128K 输出），只对通过 Daybreak Red 审核的组织开放；正文明确写「通用编码并不优于 Astra」以免被当成 Astra 的升级版。这是一条**补漏**：11-05 的发布在前两轮日增量与 11-14 的季度审计里都没抓到
- **章节三 / 对比表与选型建议**：编程场景表 `Qwen3.8-Max $2/$6` → **`Qwen4-Max ¥10/¥30`**；中文写作、中文项目优先两处的首选同步换名；新增一条「预算敏感又要多模态 → 混元 Hy4 flash」
- **章节三 / 《怎么读版本号》第 2 条**：例子从「Qwen4-Max 预览只到 11-25」改为「11-11 上线、**11-16 就出了正式版并给出书面价格**」，并补判断标准——看它有没有**价格页**与**明确下线日**，两者都没有就只当试用
- **章节一 / 最新动态**：新增 **2026-11-17 发版 v2026.11.5**（官方口径 **351 个 PR**）。七条 Highlight 六条是可靠性（重启保留排队消息、Doctor / Gateway 启动失败**自动回滚**、Telegram 内渲染交互组件、内存索引重建恢复、主账号不再阻断 Claude CLI 兜底、设备文件夹可选、二进制附件不串成提示词），**夹了一条破坏性变更**：第三方 harness 要在宿主 `runAttempt` 内注册会话级活跃运行，插件 RPC 改用授权 Gateway 方法派发，start-owner 观察字段改名 `startDeadlineAtMs`。11.4 / 11.3 两行的「当前 stable」标注同步下移
- **章节四 / Claude Code 行**：`2.1.325` → **`2.1.326`**（2026-11-16，Code Mode 可与 agent teams 同开、`/status` 新增「功能被 provider 还是环境变量关掉」一行、Ctrl+O 展开折叠的启动提示、新增 `OTEL_RESOURCE_INCLUDE_HOST`）
- **章节二 / 腾讯云 Token Plan 行**：Hy 线可选模型 `Hy3、Hy4 preview` → **`Hy3、Hy4（正式版）、Hy4 flash`**（价格档位未变）

### 工程

- `vitepress build` 通过（2.13s）
- 本轮**未触碰任何 star 数字**，未运行 `update_stars.sh`——star 由独立任务每周刷新
- 核过但**未改**：Codex CLI 仍 `0.169.0`（`0.170` / `0.171` 只有 alpha）、DSH 仍 `0.2.2-rc`（`rc.3`，11-13）、OpenClaw extended-stable 仍 `2026.9.37`、Antigravity CLI 官方 changelog 仍 **1.5.9**；Anthropic 四档价、OpenAI 四档价、Gemini 三档价（Argon / Carbon 推广价 $2/$10 **11-30 后** $4/$20）、DeepSeek 两档价均无变化

### 未写入（依据不足或不在范围）

- **Antigravity CLI 1.5.10**：两家第三方 changelog 镜像（devagentradar、havoptic）已挂 1.5.10 与详细修复清单，但**官方 `/docs/changelog` 的 CLI 目录只到 1.5.9**，按「官方未确认的版本号不写」处理，等官方页更新再补
- **阿里 Token Plan 的 Qwen4 尝鲜价**（19.5 元 / 2 万 Credits、39.5 元 / 4.5 万 Credits）：是**活动价且只 1 个月**，与主表「只写刊例价」的口径冲突，不入表
- **GLM-5.4 / 5.5**：仍未发布（智谱侧无任何模型页或价格页）；**Kimi / MiniMax / Meta / Mistral** 24 小时内无新版本、无调价
- **Qwen4 中小尺寸开源**：官方只说「将陆续开源」，**没有日期也没有仓库**，正文按预告写、不当既成事实

---

## 2026-11-16 19:00 · 每日时效更新

> 例行日增量：核对 11-15 19:00 之后 24 小时的官方口径。三处实质变化——**OpenClaw 出了新 stable**、**ch03 关于 DeepSeek 两档模型「只差一处」的判断已经不成立**、**决策模型不再是创业公司专属**。

### 变更

- **章节一 / 最新动态**：新增 **2026-11-16 发版 v2026.11.4**（当前 stable，npm `latest` 已指向它），并给 11.3 那行补上「现已被 11.4 接替」。依据是 GitHub release `v2026.11.4`（2026-11-16T04:17Z，`prerelease=false`）与 `npm view openclaw version` = `2026.11.4` 双向确认。11.4 是**纯稳定性版**：Highlight 六条（大会话内存 / 大库启动 / 回复可靠性 / 会话隐私 / 升级安全 / Safe Files）没有一条是新功能，故按「发版节奏快、功能靠大版本」的既定判断只记要点，不逐条展开 PR
- **章节三 / DeepSeek 接口层**：把「**唯一的**硬差异是图像输入只有 Flash 支持」改成**两条硬差异都在 Flash 一侧**——新增第二条：2026-11-13 开放的内置应用工具也只挂在 `deepseek-flash` 上。这条是纠错：原句会让读者以为 Pro 只是不能看图，实际连联网 / 读链接 / 文件输入 / 安全检查都用不了
- **章节三 / DeepSeek 新增小节「内置应用能力」**：补 11-13 官方 changelog《Releasing the full suite of application APIs》那一层——在原有请求里打开参数即可获得 `deepseek_web_search`（关思考=按需搜、开思考=多轮推理式搜读）、文件输入、`deepseek_read_url`、安全检查（面向公众必须开启），工具调用与上下文拼接由服务端完成；并注明官方同时开源了 `chat-demo` 参考客户端。这一层此前完全缺失，读者只能看到「周边 API 要自己拼装」的写法
- **章节三 / 决策模型小节**：表格代表由 `Jev` 改为 `Jev、Gemini Decision 1`，并新增子节《决策模型的第二个玩家：Gemini Decision 1》。依据是 Google 官方博文《Introducing the Gemini Decisions API》（2026-11-11，作者 Min Choi / Felix Yu），并由四家中文媒体同日转述交叉验证：`gemini-decision-1` 走 `v1beta` 与 AI Studio（**Preview**），单次最多 1,000 问、256K 多模态输入、端到端 150–250ms、**$0.10/百万输入且输出不计费**。新节给了一张 Jev vs Gemini 的六维对照表，并点明两件事：① 这一品类已进入大厂生产用法（Gemini Notebook 路由、Stitch、Google 搜索的 MCP 工具安全层）；② 短板在校准不在速度——越界输入缺「其他」兜底时会被强行归类，故兜底选项与置信度阈值是设计的一部分
- **章节七 / Antigravity 行**：CLI `1.5.8` → **`1.5.9`**（2026-11-14），「11 月连发 9 版」→ **10 版**。补两条实装：`run_workflow` 从灰度转**对所有人开放**（用 CLI 自带 Python，本机不必装 Python）、新增 `pluginControls` 托管设置（非 Gemini Enterprise 组织也能整体禁插件 / 关市场）。同时把 Dynamic Workflows 那句「不再限于灰度」写清，避免与新 CLI 描述打架

### 工程

- `vitepress build` 通过（2.31s）
- 本轮**未触碰任何 star 数字**，也未运行 `update_stars.sh`——star 由独立任务每周刷新（11-15 用户定下的规则）
- 核过但**未改**：Claude Code 仍 `2.1.325`（11-13）、Codex CLI 仍 `0.169.0`（11-13，`0.171.0` 只到 alpha.7）、DSH 仍 `0.2.2-rc`、OpenClaw extended-stable 仍 `2026.9.37`；Anthropic 四档价（$8/$40、$4/$20、$2/$10、$0.10/$0.50）、OpenAI 四档价（$10/$50、$2/$10、$1/$5、$0.10/$0.50）、Gemini 三档价（Argon/Carbon 推广 $2/$10 **12-01 起 $4/$20**、Hydrogen $1.50/$7.50）、DeepSeek 两档价均无变化

### 未写入（依据不足或不在范围）

- **ZCode 3.18.2**：只有一家周报提到「下载页已移到 3.18.2」，官方站点与 npm 均无法直接取到版本号，**单一来源不写**
- **GitHub Copilot 12-14 弃用 6 个模型**：官方只说「六个」，**名单至今未公布**，无法写成可执行条目
- **华为云盘古 11-16 更新**：仅见聚合站转述，缺官方一手口径
- Anthropic 的 **Sonnet 4.5 于 2026-11-30 退役**：与本书在役模型清单无关（文档只写当前四档），不入正文

---

## 2026-11-15 19:00 · 每日时效更新

> 例行日增量：核对 11-14 19:00 之后 24 小时的官方口径。核心是一条判断被推翻了——**Gemini 3.8 Flash 并不是「仍在役」，它已被 Hydrogen 接替**。

### 变更

- **章节三 / Gemini 行**：`3.8 Flash / 3.8 Live 仍在役` → **`3.8 Flash 已被 Hydrogen 接替`**（3.8 Live 仍在役）。依据是 Google 官方迁移文档《Migrate to the latest Gemini models》把 `gemini-3.8-flash` 的迁移目标直接写成 `gemini-4-hydrogen`，并附完整迁移清单；Vertex 的模型生命周期表仍保留 `gemini-3.8-flash`（弃用日 2027-09-02），所以口径写成「已接替、Vertex 尚可调用至弃用日」而不是「已下线」。昨天（11-14）判断为「仍在役」是因为当天只核到发布公告、没核迁移文档，这次修正
- **章节三 / Gemini 行**：Hydrogen 的输出口径由「1M 上下文、1M 输出」收紧为「**输入+输出合计 1,048,576、单段输出上限 65,536**」。官方迁移文档明确这是统一额度 + 单段上限，超过 65,536 需走长解码 / 续写；原写法会让读者以为一次能吐 100 万 token
- **章节三 / Gemini 行与单价小节**：补 **11-14 起 Hydrogen 成为 Search「AI 模式」默认模型**，以及官方给的两个反差数字——Terminal-Bench 4.1 **57%**（3.8 Flash 18.2%）、默认档任务**快 2.5 倍**。这两条解释了 Google 为何敢弃用 Flash 这一档品牌
- **章节三 / 新增 Meta 行**：Muse Ember（2026-11-09）经 **Meta Model API** 对外，1M 上下文、原生文本 / 图像 / 音频 / 视频输入、**$0.10 / $0.50**，与 GPT-6 Luna、DeepSeek Flash 同价带。这是 Meta 第一次把自研模型做成付费 API，模型章此前完全没有 Meta 条目
- **章节三 / 混元行**：补**实时语音线 Hy Realtime**（2026-11-13 发布，新增 Agentic 工具调用与唱歌，已在元宝语音通话 / 腾讯客服上线，腾讯云 API 未开放、无对外定价）。同时刻意写明「无定价」，避免读者误当成可调模型
- **章节四 / Antigravity CLI 行**：模型列 `Gemini 4 Argon / Carbon、3.8 Flash、3.1 Pro` → `Gemini 4 Argon / Carbon / Hydrogen、3.1 Pro`。原写法漏了 Hydrogen 却留着已被接替的 Flash，与章节七自相矛盾，属内部不一致的修复
- **章节七 / Antigravity 行**：可选模型由 `… / Hydrogen、3.8 Flash、3.1 Pro` 改为 `… / Hydrogen、3.1 Pro（3.8 Flash 档已由 Hydrogen 接替）`

### 工程

- star 刷新 **14 处 / 4 个文件**（ch04 / ch05 / ch06 / ch08），`--check` 复验 **51 条全绿**；单次最大涨幅 `anthropics/skills` 194.6K → 194.9K
- `vitepress build` 通过（2.38s）
- 核过但**未改**：Claude Code 仍 2.1.325（11-13）、Codex CLI 仍 0.169.0（11-13，0.171.0 只到 alpha.5）、OpenClaw stable 仍 2026.11.3（11-15 的 11.5-beta.3 是预发布，不写）、DSH 仍 `0.2.2-rc.3`

---

## 2026-11-15

> 本次不是时效审计，是**章节四的内容补充**：DSH 在选型建议里只有一句「一切皆插件」，读者拿不到可执行的下一步，故补一节插件安装与发现机制 + 社区索引源 + 风险提示。外部事实均取自 `deepseek-ai/deepseek-harness` 仓库的官方文档（`docs/user/guide/plugin-market.zh.md`、`docs/cli-help.zh.md`）与 npm 元数据。

### 新增

- **章节四**：新增「DSH 插件推荐小结」。四个部分：
  1. **机制**——引官方 CLI 帮助的原文，说明 `dsh` 启动的 profile 本身就是「按序叠放的插件包补丁层，用户覆盖在最上面」；装插件的命令是 `dsh plugin --profile <name> add <包>`（该子命令实为把参数转发给 profile 目录下的 pnpm）
  2. **发现**——点明一处最容易踩空的地方：插件页的「发现」标签默认不存在，需先开启实验性组合包「自定义插件索引」；且**官方不内置任何索引源**，必须自行添加 format-1 的 JSON 索引 URL。这是 DSH 与 Claude Code 插件市场最大的差异
  3. **三个社区项目**（均标注非官方）：dsh-market（可视化市场兼索引源）、awesome-dsh-plugin（精选清单）、DSH Desktop（桌面外壳）
  4. **三条实践与一条风险**：索引源优先 npm / CDN（作者说明 dsh 对索引源有 15 秒超时）、只加可信源（引官方「DSH 检查文件格式，但不验证这些声明」）、警惕「免 Key 用前沿模型」类插件（点名 `dsh-our-free-model`，说明共享/转售凭证的条款与数据风险，但不推荐）

### 变更

- **章节四**：DSH 版本口径由「v0.1 开发者预览版」改为 **`0.2.2-rc`**（npm `latest` = `0.2.2-rc.1`，`next` = `0.2.2-rc.3`，GitHub 最新 release `dsh-v0.2.2-rc.3`，2026-11-13），并补一句指向新小节。原写法停留在 0.1，与 npm 实际发布脱节；**仍全部为预发布**，「不可用于生产」的定性不变

### 工程

- star 刷新 21 处 / 6 个文件，`--check` 复验 **51 条全绿**（原 47 条 + 新增 4 条）
- `scripts/stars.manifest` 新增 4 条（ch04 的 dsh-market / awesome-dsh-plugin / dsh-desktop / dsh-our-free-model），清单总量 47 → 51。⚠️ 表格里的 star 必须写成 `12.4K star` 而非 `12.4K`，因为脚本的 `TOKEN` 正则要求数字后紧跟 `star` / `星标`，否则会报「命中片段但该行没有 star 数字」
- `vitepress build` 通过（2.18s），产物已确认渲染出新节

## 2026-11-14

> 本次对应 2026-11 内容时效性审计（内部报告 `AUDIT-2026-11.md`，11-05 制定）的批次 A / B / C。因执行时距方案已过 9 天，**所有条目按 11-14 的现状重新核验**，其中两条与原方案不同（见文末）。外部事实均经官方文档、发布说明或一手报道交叉验证。

### 变更

- **章节三**：国际表重写。**Claude** 补 **Fable 5.2 / Mythos 5.2**（2026-11-09，$8/$40、1M 上下文 / 128K 输出、始终开启自适应思考，另有 2.5 倍速 fast 模式 $16/$80）与 Sonnet 5.5 / Haiku 5.5，并把 Opus 5.5 明确为「日常主力」；**OpenAI** 改为 Astra / 6.1 Sol / 6.1 Terra / Luna 四层并列，补 GPT-5.5 于 10-14 从 ChatGPT / Codex 下线（API 仍可调用）；**Google** 从「Gemini 4 尚未发布」改为 **Argon + Carbon 双旗舰**，并标注 $2/$10 推广价 **2026-11-30 后恢复 $4/$20**
- **章节三**：国产表换血。**DeepSeek** → V4.1-Flash-1017（10-17，MIT 权重）；**Kimi** → K3.1 Pro（10-23，2.8T / 104B 激活）；**MiniMax** 补 M3.1 Flash（10-19，428B / 23B）；**新增 腾讯混元 Hy4**（11-04 正式版，770B / 49B，首次视觉理解与 Computer Use）与 **Mistral Large 4**（10-29 开源权重）两条；**Qwen** 注明 Qwen4-Max 仅为预览（11-25 下线）；**GLM** 标注下一代未发布
- **章节三**：新增「**怎么读 2026 年的版本号**」小节——把代际 / 同代档位 / 推理强度 / 渠道别名四层拆开，配三条实用规则。这是原文档最大的认知缺口：同代 Terra 弱于 Sol 并不代表「版本更低」
- **章节三**：编程场景对比表改为带实际单价，非编程场景表新增「看图操作桌面」一行，选型建议按「日常 / 最难任务 / 中文 / 预算敏感」重排
- **章节四**：Codex CLI 从 0.156.1 更新到 **0.167.0（11-06）**，补 Vertex AI 内置 provider、`gpt-6.1-terra` 进目录、GPT-5.5 在 ChatGPT 登录会话退役、agent 指挥中心与 `/presets`；Claude Code 更新到 **2.1.325（11-13）**
- **章节四**：采用率口径替换——原「2026 年最受喜爱的 AI 编码工具（46% 偏好）」改为 **Stack Overflow 2026 开发者调查：Claude Code 65.5% vs Codex CLI 29.5%**（两者口径不同，不再混写）
- **章节二**：**方舟首两月 2.5 折已于 11-08 结束**，恢复 40 / 200 元刊例价（Agent Plan 包年五折 11-12 也已到期）；Kimi 会员覆盖模型更新为 K3.1 Pro，并标注 K2 系列 10-31 停止新用户接入；新增 **商汤 SenseNova Token Plan 公测 ¥0/月** 一行
- **章节二**：趋势节改写两处——「按请求次数计费的旧形态正在退场」补为**三分**（按次 / 按积分 / 订阅送工具额度 + 0 元公测）；「免费档没有如期普及」改为**已出现第一个真 0 元订阅**（商汤 Lite + 华为云码道），并提醒商汤给的是轻量版模型；另补「官网 / 电商 / 直播间三套价并存」
- **章节一**：时间线补 **2026-11-03（v2026.10.10 功能版，3,028 PR / 454 贡献者）** 与 **2026-11-08（v2026.11.2 修复版，当前 stable）**；能力清单补 **Chat Details 可观测面板、Advisor 自查、MCP Relay、MCP 事件触发**
- **章节七**：Cursor 补 10-20 Agent SDK、11-05 Build Live Apps、11-06 Grok Voice 实时语音三条，并说明官方已改为按功能发版、不再统一标注版本号；Antigravity 补 **CLI 1.5.x**（11-04 起连发 7 版、`agy acp`、`--remote-agent`）与 **`/swarm`** 预览；ZCode 补 **3.17.2（11-03）三个官方插件**
- **章节六**：Extensions 框架补一句三者用途（长任务托管 / 可交互 UI / 模态无关征询），并新增「**MCP 2.0**」别名说明——指的就是 2026-07-28 规范
- **章节十三**：MTEB 链接由 HF Space 改为官方 **`leaderboard.mteb.org`**，与章节十一保持一致，并提示先分清 v1 / v2
- **章节三**：DeepSeek 由单行条目扩为完整一节「**一个 Key 下的 API 全家桶**」，补齐此前完全缺失的旗舰档 **`deepseek-v4-pro`**（V4-Pro-0813：1.6T / 49B 激活、纯文本、1M 上下文 / 384K 输出、并发 500）。内容分三层：① 模型层——两档并列，给全低峰 / 高峰价与缓存命中比价，并指出「高峰」其实是北京时间 09:00–12:00 与 14:00–18:00，夜间与周末一律半价；② 接口层——OpenAI Chat Completions / Responses / Anthropic / Beta 四条 Base URL，说明 Claude Code 可直连；③ 周边层——Search & Fetch、Web Tools、文件解析与 OCR、TTS / ASR 的单价、计费条件与 QPS 口径。另补三个改名坑（`deepseek-chat` / `deepseek-reasoner` 已于 07-24 退役、`deepseek-v4-flash` 等旧别名被路由到新版、**「V4.1-Pro」并不存在**）与思考模式默认开启带来的三个 400 陷阱；编程对比表加 V4-Pro 一行，「怎么读版本号」补第 4 条（滚动别名会静默换代）

### 工程

- **star 批量刷新 43 处 / 8 个文件**：`scripts/update_stars.sh --apply` 执行，`--check` 复验 **47 条全绿**。涨幅最大的是 `deepseek-ai/deepseek-harness`（234.1K → 280.6K）、`anomalyco/opencode`（209.6K → 226.7K）、`farion1231/cc-switch`（135.5K → 154.3K）
- 新增外链 5 条均实测 200（`leaderboard.mteb.org`、腾讯云混元页、Mistral、商汤 Token Plan、Claude 模型总览）；`vitepress build` 通过

### 与 11-05 方案的偏差（按实际核验修正）

1. **Gemini 4 Carbon 原判「受限渠道、不能当公开 API 写」已被推翻**：Google 于 **2026-11-10** 起对全部付费开发者与企业开放 Carbon，Google AI Ultra 用户也可在 Gemini 应用、搜索 AI 模式与 Antigravity 中使用。原方案是按 10-28 的 Fairwind 阶段写的，执行时已过期
2. **Qwen4 原计划「只写已官宣、未开放」也需再收紧**：11-11 上线的只有 `qwen4-max-preview`，**仅 Token Plan 可调、11-25 下线**，参数 / 价格 / 权重均未公布——不是「四档已官宣」的状态
3. **GPT-6.1 Sol 发布日**：官方与多家追踪站均为 **09-29**（原方案写 10-01），按实测值改正

### 明确不写（沿用谣言隔离区）

- **Claude Opus 5.6**：截至 11-14 无模型 ID、无价格、无榜单条目，Anthropic 未确认
- **GLM-5.4 / 5.5**：官方目录仍止于 5.3 家族，且 11-01 复核确认无新代际
- **Qwen4 参数与跑分**：仅有非官方站点给出的数值，官方页面无 benchmark
- **GPT-6.1 Astra 取消**：单一来源，不写入

### 变更（当日 19:00 增量复核：补齐 11-10 ~ 11-13 的三条发布）

- **章节三**：Google 从「双旗舰」改为**三档并列**，补 **Gemini 4 Hydrogen**（**2026-11-12 发布**，$1.50/$7.50、1M 上下文 / 1M 输出、四档思考 `low/medium/high/xhigh`，官方定位「快速执行引擎」，可与 Carbon / Argon 搭班）。编程对比表加 Hydrogen 一行，「怎么读版本号」的同代档位补 Hydrogen。依据：Google 官方发布（Pichai 帖文 + 模型卡）+ 印度《商业线报》《IT 之家》《腾讯新闻》多源一致；**AA 智能指数 51 / xhigh 54，高于 Argon 的 50**，但这是厂商自评，正文只作定位说明不写成结论
- **章节四**：Codex CLI **0.167.0 → 0.169.0**（**2026-11-13**，同日连发 0.168 / 0.169，其间另有 0.167.1、0.167.2 补丁）。补 0.168 的 TUI 内 provider 选择、侧栏会话缩放（`leader z`）、音频附件与动图；0.169 的多标签侧栏、历史任务按名称/提示/目录搜索、终端内自定义 provider（SSH 走 device code）、`codex exec` 在不可信目录需 `--trust`。依据：`gh api repos/openai/codex/releases` 一手 release 正文
- **章节一**：OpenClaw **v2026.11.2 → v2026.11.3**（**2026-11-10**，当前 stable）。安全修复版、**无新功能**，官方口径 **56 PR / 36 位贡献者**：缓存与复用的插件结果按连接凭证隔离、插件传输钩子锁回 provider 源站、Signal 守护进程与内置语言服务器不再继承 Gateway 密钥、空指纹时保留已存证书并在传输前校验、必需沙箱下图片预览限在允许目录；另修更新中断后 Gateway 停摆、慢存储备份超时。extended-stable 同步为 **2026.9.37**。依据：GitHub release 正文 + 官方 docs 页
- **章节七**：Antigravity CLI 由「1.5.x / 连发 7 版」改为 **1.5.8（11 月共 9 版）**，可选模型补 Hydrogen；补两处调度层能力——**Orchestrator**（Carbon 规划 / Hydrogen 执行，Pro 与 Ultra 可用）与 **Dynamic Workflows**（`/run-workflow`，agent 先写 Python 脚本再确定性并发/分阶段跑 subagent，脚本需用户确认）

### 工程（同一时点）

- star 刷新 **9 处 / 4 个文件**，`--check` 复验 **47 条全绿**
- `vitepress build` 通过（2.22s）
- ⚠️ **`--check` 会因四舍五入边界抖动**：`ChromeDevTools/chrome-devtools-mcp` 实测 55,851（55.85K 临界点），首次 apply 记 55.8K、复验时又报 55.9K。二次 apply 后稳定。边界值仓库应一次 apply 到位再复验，不要误判成脚本 bug

### 与上午审计的出入

- 上午的审计方案（11-05 制定）**没有覆盖 11-10 ~ 11-13 这三天的新发布**：OpenClaw 11.3（11-10）、Gemini 4 Hydrogen（11-12）、Codex 0.168/0.169（11-13）都在方案之外，靠当晚增量复核补上。**教训**：季度审计之后仍需每日扫一遍「发布类」事实，方案冻结日之后的新版本它抓不到

## 2026-11-12

> 本次为**新增章节**，不是审计。前十六章围绕「用什么工具去造」，缺一层落地场景的视角，故补入第十七章。全部外部事实于 2026-11-12 联网核验，涉及版本号与日期的条目均已标注发布日期。

### 新增

- **新增第十七章「AI 应用与多模态创作」**（`docs/chapter17/17-ai-apps.md`），补足此前缺失的**多模态与应用场景**视角，共 10 个小节：基础大模型与通用助手、ChatGPT 类应用、AI 搜索、写作、编程开发（以指针引用章节二/四/七，不重复）、翻译、图像生成、语音识别与合成、影音创作、视频生成、视频内容总结，另附「按人群的组合建议」与「为什么不要照抄旧清单」
- **章节定位**：作为「应用层」接入，`docs/index.md` 全景架构图与章节目录、`docs/.vitepress/config.ts` 侧边栏均新增对应条目；章节十六页脚补「下一章」互链
- **README 同步**：内容结构范围更新为 `chapter01 ~ chapter17`，章节目录表补第十七章

### 核验要点（本章中易过期的判断）

- **Sora 已停服**：OpenAI 于 2026-03-24 宣布停止独立应用与 API，应用 2026-04-26 关闭、API 于 2026-09 关闭。本章明确标注，避免读者按旧资料选型
- **DALL·E 已从 ChatGPT 退役**，图像能力由 ChatGPT Images 系列承担（2.5 于 2026-09-08、2.6 于 2026-11-04 发布）
- **Suno 当前主力为 v6**（2026-09-09，含 v6-wild / v6-mini），旧版本随 v6 铺开退役，且**无公开 API**
- **ElevenLabs 当前为 Eleven v4 / v4 Turbo**（2026-09-28），90+ 语言，支持 `[audio tags]`
- **视频模型按能力分工**：Veo 3.1（口型与音频）、Kling 3.0（人体动作）、Seedance 2.0 Pro（多镜头一致性，港大 2026-10 评测文字生成视频项第一）、Runway Gen-4.5（编辑控制）、Gemini Omni Flash（对话式改片）
- **Kimi K3.1 Pro**（2026-10-27）2.8T 参数、1M 上下文，AA 智能指数 55 分列第 4

## 2026-09-23

> 本节对应内容时效性审计（内部报告 `AUDIT-2026-09.md`）。截至目前已完成：**批次 1**（P0 硬错误修复）、**批次 2 全部**（star 数 + 模型版本 / 上下文窗口 / 零散数据）、**批次 3**（章节二 Coding Plan 整章重构）、**批次 4 全部**（IDE/ADE、向量知识库、国产 Claw 扩军、CLI 模型矩阵），以及**术语落位**（新增章节十六）。全部外部事实均经实测或官方来源核验。

### 修复

- **章节三**：修正 Claude API 文档链接（`platform.claude.com/docs/zh-CN/claude/claude-api` 实测 404，改为 `platform.claude.com/docs/en/models/overview`）
- **章节四**：Gemini CLI 已于 2026-06-18 对免费 / Google AI Pro / Google AI Ultra 用户停服，条目改为继任者 **Antigravity CLI（命令名 `agy`）**，并标注企业版 Code Assist 不受影响；选型建议与对比矩阵同步更新
- **章节五**：Anthropic 官方技能数 **17 → 19**，补入 `academy-guide`（回答"怎么用 Claude"时推荐 Claude Academy 课程）与 `discernment-nudge`（给出实质回答后追加 2-3 个核查性追问）；分类导航的「团队协作」扩充为「团队协作与质量管理」
- **章节六 / 七**：**Windsurf 已于 2026-06-02 更名 Devin Desktop**，厂商由 Codeium 变更为 Cognition。章节七全章更名、链接改为 `devin.ai/desktop`（原 `windsurf.com` 实测 301 跳转）、核心模式 Cascade 改为 Devin Local（Rust 重写）；章节六的 MCP 客户端表同步更名
- **章节七**：补充 Cursor 归属变更——**Anysphere 于 2026-08-14 被 SpaceX 全资收购**（时间线：2026-04-21 签期权协议 → 2026-06-16 官宣 → 2026-08-14 交割完成）；版本号修正为约 3.21.x，Pro 价仍 20 美元/月并补充 Pro+/Ultra/Teams 档位
  > ⚠️ **请勿回退本项**：本项目 2026-05-11 曾将「Cursor 被 SpaceX 收购」作为**虚假信息删除**。当时该交易尚未官宣（2026-06-16 才官宣），删谣是正确的；交易此后真实发生并有官方与多源媒体来源，故本次补回。**这不是旧谣言复活。**
- **章节八**：AutoGen 已进入**维护模式**（仅安全补丁与关键修复，不再有新功能），标注新项目建议改用 Microsoft Agent Framework；MAF 补注 1.0 GA（2026-04-02）与统一 AutoGen + Semantic Kernel 的关系；选型对比矩阵与决策树同步调整
- **章节十三 / 十四**：统一 Anthropic 文档链接为 `platform.claude.com`（`docs.anthropic.com` 已非规范地址，实测 301 至 `platform.claude.com/docs/en/home`）；章节十四的 prompt-engineering 路径改为 `platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview`（实测 200）
- **章节六 / 十五**：修正 Claude Code 的 MCP 配置位置——原写 `.claude/settings.json`，实际该文件只承载 env / hooks / permissions，**不含 `mcpServers` 键**；改为项目级 `.mcp.json`（或 `claude mcp add`，用户级落 `~/.claude.json`）
- **章节七 / 十四 / 十五**：修正章节页脚互链末尾**多余的 `]`**（此前会渲染为字面量）

### 变更

- **章节六**：重写协议说明——**MCP 2026-07-28 规范**是发布以来最大修订，协议核心转为**无状态**：移除 `initialize` / `initialized` 握手（SEP-2575）与 `Mcp-Session-Id` 会话标识（SEP-2567）；新增 `Mcp-Method` / `Mcp-Name` 请求头路由、`server/discover`、可缓存列表结果、Multi Round-Trip Requests（SEP-2322）与 Extensions 框架（Tasks / MCP Apps / EMA）；OAuth 2.1 加固并确立 12 个月弃用窗口。**Roots / Sampling / Logging 三个早期能力及旧 HTTP+SSE 传输已弃用**。新增「协议演进」对照表与迁移提示

- **star 数批量刷新（30 处）**：覆盖 26 个仓库、6 个章节文件，数值全部经 `gh api` 实测；该批改动由新增的 `scripts/update_stars.sh` 自动完成（工具说明见下方「工程」）

| 仓库 | 原值 | 实测 |
| --- | --- | --- |
| `openclaw/openclaw` | 370K | **390.3K** |
| `nousresearch/hermes-agent` | 142K | **248.3K** |
| `anomalyco/opencode` | 158K | **209.6K** |
| `n8n-io/n8n` | 187K | **205.8K** |
| `ultraworkers/claw-code` | 191K | **195.3K** |
| `anthropics/skills` | 132K | **177.8K** |
| `anthropics/claude-code` | 122K | **147.7K** |
| `farion1231/cc-switch` | 66K | **135.4K**（翻倍） |
| `punkpeye/awesome-mcp-servers` | 87K | **95.5K** |
| `upstash/context7` | 55K | **62.4K** |
| `ChromeDevTools/chrome-devtools-mcp` | 39K | **52.5K** |
| `VoltAgent/awesome-openclaw-skills` | 48K | **52.7K** |
| `microsoft/playwright-mcp` | 32K | **37.5K** |
| `microsoft/graphrag` | 23K | **36.1K** |
| `github/github-mcp-server` | 30K | **33.1K** |
| `oraios/serena` | 24K | **29.7K** |
| `PrefectHQ/fastmcp` | 25K | **27.9K** |
| `NVIDIA/NemoClaw` | 20K | **22.5K** |
| `travisvn/awesome-claude-skills` | 12K | **15.1K** |
| `aiming-lab/AutoResearchClaw` | 12K | **14.5K** |
| `HKUDS/ClawWork` | 8K | **8.6K** |
| `ValueCell-ai/ClawX` | 7K | **7.6K** |
| `HKUDS/ClawTeam` | 5K | **5.5K** |
| `qingchencloud/clawpanel` | 2.7K | **2.9K** |
| `1186258278/OpenClawChineseTranslation` | 3.8K | 3.8K（持平） |
| `microsoft/agent-framework` | 13.7K | 13.7K（持平） |

- 后续每季度审计时，直接跑 `scripts/update_stars.sh` 即可完成全部星标刷新，无需手工核对

### 工程

- **新增 `scripts/update_stars.sh` + `scripts/stars.manifest`**：用 `gh api` 批量刷新文档中的 GitHub star 数。默认只输出差异（预演），`--apply` 才写入，`--check` 供 CI 使用；值统一格式化为一位小数的 K/M，并把旧写法里的保守 `+` 去掉（有精确实测值后不再需要）
- 清单按「**行级唯一片段**」而非仓库名定位——同一仓库星标常在同一章节出现多次、且可能跨章节（`openclaw` 在章节一出现 4 次，`Claude Code` 跨章节四/八），按仓库名泛匹配会误伤
- 有意排除「历史快照」类星标，例：章节一时间线 `| 2025-11-24 | 项目创建，仅 6 个月达到 370K star |` 描述的是当时节点，不随最新值变动
- 链接体检经验：**CSDN 对脚本请求返回 521 属反爬，并非死链**（同一 URL 用带浏览器标识的抓取工具可正常读取）。判定死链前先做站点对照测试，避免误删有效链接
- 仓库卫生：VitePress 构建期会向 `docs/.vitepress/` 泄漏 `config.ts.timestamp-*.mjs` 临时文件，已加入 `.gitignore`
- **README 同步与「维护」小节**：内容结构范围更新为 `chapter01 ~ chapter16`、章节目录表补第十六章；新增「维护」一节说明 `scripts/update_stars.sh` 的用法与清单定位约定；「参与贡献」补一条「内容变更请同步更新 log.md」
- **star 清单扩至 47 条 / 37 个仓库**（本批新增 LightRAG）；脚本预演 0 歧义警告

### 新增（批次 4 · IDE / ADE 部分）

- **章节七**：新增开篇「先搞清楚：IDE、Agent CLI、ADE 是三件事」——按「交出多少控制权」区分三种形态（AI IDE / Agent CLI / ADE），并说明 **ADE（Agentic Development Environment，智能体开发环境）** 是 2026 年的新品类：**没有传统编辑器**、以任务（Goal）为单位、原生支持多 agent 并行。同时标注 **ADE 一词的双重含义**（Letta 原义指"开发和调试 agent 本身的平台"，开发工具圈现指"用 agent 造软件的工作台"），避免读者误读
- **章节七**：新增「ADE（Agent-first 开发环境）」小节，收录 4 款：
  - **ZCode**（智谱 Z.ai）——国内名 **Z Code**，2025-12-26 首发；2026-07-02 发布 ADE 版并登顶 Hacker News；内核已适配 **GLM-5.3-Flash**。⚠️ 2026-09-18 就"代码库数据上传"公开致歉并宣布将开源代码库，条目中已加企业采用提示
  - **JetBrains Air**——**2026-09-22 发布**，含 Air in IDEs（插件）/ Air Teams（团队云端协作）/ Air Governance（原 JetBrains Central）/ Air Context / Air Gateway；坚持多供应商，可接 Claude Agent、Codex、Copilot、OpenCode、Junie 及任何实现 **ACP**（Agent Client Protocol，JetBrains 与 Zed 共同制定）的 agent
  - **Warp**——2026-04-28 开源核心产品（`warpdotdev/warp` 实测 **65,134** star），配云端编排平台 **Oz**，可把 Claude Code / Codex / Warp Agent 并排跑在同一控制面，带跨 harness 持久记忆与企业级权限、成本上限
  - **Emdash**（开源，YC W26，MIT）——桌面端多 agent 编排，可接 **31+ 种 CLI agent**，用 **git worktree** 给每个 agent 隔离工作目录（实测 5,808 star）
- **章节七**：新增 **Visual Studio 2026** 条目——**2025-11-11 正式发布**（与 .NET 10 LTS 同期，Fluent UI 重做），**GitHub Copilot 免费内置**（Copilot Free 每月 2,000 次补全 + 50 次高级请求），内置 Profiler Agent / Debugger Agent 与 C#、C++ 专用 agent

### 变更（批次 4 · IDE / ADE 部分）

- **章节七**：**Trae 已拆分产品线**——原 TRAE IDE 更名为 **TraeCode**（IDE 模式 + SOLO 模式），办公能力独立为 **TraeWork**（AI 原生工作台，网页 / 桌面 / 移动三端，Work / Code / Design 三模式）。原文"已升级为 TRAE SOLO"的表述已不成立，全章同步更名并补充两条产品线的关系
- **章节七**：Antigravity 补 **GA** 状态与定价——个人档 **$0/月**（不限量 Tab 补全与命令请求 + 每周基础 agent 额度；可选 Gemini 3 系列 Flash、Gemini 3.1 Pro，另可调 Claude Sonnet/Opus 4.6 与 gpt-oss-120b），付费走 Google AI Pro（$19.99/月）与 Ultra（$99.99 / $199.99）；**Antigravity 2.0 已从 IDE 转为「命令中心」**，另有 CLI 与 SDK 入口
- **章节七**：选型对比表「类型」列改为「形态」以统一新术语，并新增 ZCode / JetBrains Air / Warp 三行；选型建议与决策树补入 ADE 与办公向 AI 工作台分支；「各 IDE 核心体验」更名为「各工具核心体验」并补 ZCode / JetBrains Air / Warp 三节
- **章节五 / 六 / 十二**：同步 Trae → **TraeCode**；章节十二「范式与工具映射」表的 `Cursor / Windsurf` 改为 `Cursor / Devin Desktop`，并在表下补 ADE 与 Harness Engineering 的关联说明
- **章节七**：相关文章首条为 2026 年原文标题（含 Windsurf / Trae 旧名），**加注现名**以免读者混淆；另补 JetBrains Air、Warp、Emdash 三个官方 / 仓库链接

> **两点与内部审计报告 `AUDIT-2026-09.md` 的偏差（已按实测修正）**
>
> 1. 报告 P2-04 把 JetBrains Air 定性为「Fleet 演进」。实测其官方发布说明并未将其描述为 Fleet 的继任者，而是把 **JetBrains Central** 与六个月的 agentic 开发工作整合成一套产品体系（Air in IDEs / Teams / Governance）。
> 2. 报告 P2-04 提到 Visual Studio 2026，但未给日期。实测 GA 日期为 **2025-11-11**（微软 Learn 生命周期页），部分第三方文章所写 2026-07-22 有误。

### 新增（批次 4 · 向量知识库）

- **章节十**：新增开篇「四种技术路线」框架——把选型的第一层判断从"谁 benchmark 更高"改为**架构路线**：全托管专用库（Pinecone / Zilliz Cloud）、开源自托管（Milvus / Qdrant / Weaviate）、**寄生于既有数据库**（pgvector / pgvectorscale、LanceDB）、**对象存储原生**（Turbopuffer）
- **章节十**：新增 4 个条目：
  - **Turbopuffer**——对象存储（S3 / GCS / Azure）原生的 serverless 向量 + 全文检索，索引不常驻内存；Cursor / Notion / Anthropic 生产使用（官方口径实测 1T+ 文档）；闭源，无免费档，$16/月起
  - **LanceDB**——进程内嵌入式（Apache-2.0），**Lance 列存格式（基于 Apache Arrow）**，同一张表存向量与多模态数据，自带版本管理与回滚；实测 **11.5K star**
  - **pgvector**——PostgreSQL 向量扩展，与业务数据同事务查询，Supabase / Neon / RDS 等默认自带；实测 **23.1K star**
  - **pgvectorscale**——Timescale 出品，在 pgvector 之上叠加 **StreamingDiskANN** 磁盘索引与量化压缩，突破内存上限；实测 **3.1K star**
- **章节十**：「向量索引类型」补 **DiskANN** 一行（图索引与向量存盘、按需流式读取），索引选择建议补上"内存装不下时改用 DiskANN"
- **章节十**：本章原先**没有任何 star 数**（工具类章节中唯一的例外），本次补入 7 个实测值并登记进 `scripts/stars.manifest`

### 变更（批次 4 · 向量知识库）

- **章节十**：选型对比表新增 4 行；选型建议补「已在用 Postgres → pgvector（内存吃紧时再加 pgvectorscale）」「海量冷数据 + 成本敏感 → Turbopuffer」「多模态 / 数据工程栈 → LanceDB」三条，并把原「原型验证」条目的规模上限由 `<1M` 明确为 `< 100 万`
- **章节十**：新增「选型路径」决策树（按数据量 / 部署形态 / 运维能力分支），与章节七的决策树体例对齐
- **章节十**：「混合检索」的支持列表由 3 个扩为 5 个（补 Turbopuffer、LanceDB），并补 Postgres 侧可配合 BM25 扩展（如 ParadeDB）补齐关键词一路

> **与内部审计报告的偏差（已按实测修正）**
>
> 报告 P2-06 称 Turbopuffer 的客户包含「AWS Bedrock 后端」。实测多个来源一致列出的生产用户为 Cursor / Notion / Anthropic / Linear / Superhuman 等，**未找到 Bedrock 相关证据**，故未写入。

### 新增（术语落位 · 章节十六）

- **新增章节十六「AI 时代的角色与商业」**——这是全站的新维度：前面十五章都是「技术栈视角」（模型 → 框架 → 工具 → 范式），本章从「人与商业」切入，并让 Token 成为贯穿各层的成本线索。含三节：
  - **FDE（前沿部署工程师）**——Palantir 于 2010 年代发明（早期内部称「Deltas」，2016 年前 FDE 比软件工程师还多）；Indeed 岗位数 2025-04 的 643 个 → 2026-04 的 5,330 个（约 +729%）；与 MLE / 解决方案顾问 / 技术支持的区别（交付物是跑在生产环境的系统）；薪资量级（海外中位 base 约 $190K，头部 $350K–550K 含股权）；三个能力交集
  - **OPC（一人公司）**——与自由职业的**结构性区别**（卖时间 vs 卖可复用系统，AI 是「管理层」而非任务工具）；2026-09 工信部专项计划 + 全国 20 省 106 项地方政策；存量 1600 万家 / 占企业总量 27.4%（2025-06 快照）；四类高杠杆赛道与三条底线
  - **Token（词元）**——作为 FDE / OPC 共同的边际成本项，说明它如何决定 loop 的可行性、模型分层调度（快判断用小模型 / 决策模型），以及订阅制与按量付费的取舍
- **章节三**：新增「延伸：三种不是『LLM』的模型形态」小节
  - **决策模型 Jev**（TypeSafe AI，2026-09 发布）——System One 路线，**不生成任何文本**，只返回带校准置信度的类型化判定；三种原语 Choice / Score / Noul；约 $0.042 / 百万输入 token。⚠️ 同时标注两个前提：官方与 Pydantic 均提示 **prompt injection 可影响其判定**，以及英文优先、**目前未向中国大陆开放**
  - **世界模型（World Model）**——两条技术路线的分歧：生成式（DeepMind Genie 3、NVIDIA Cosmos）vs 隐空间（Meta V-JEPA 2、LeCun 的 AMI Labs）
  - **专家混合（MoE）**——架构而非产品，强调需区分**总参数**与**激活参数**
- **章节十二**：新增「范式之上：四层工程谱系」——把 **Prompt → Context → Harness → Loop** 讲成**层叠**关系而非并列；含 Loop Engineering 五组件表（Trigger / Goal / Actions / Verification / Memory）、社区参考实现与风险提示、**L1 只报告 → L2 待审 → L3 无人值守**的放权节奏，并注明再上一层的「graph engineering」暂不展开
- **章节四**：新增 **DSH**（`deepseek-ai/deepseek-harness`，2026-08-13 开源的 Agent 运行时，主打「一切皆插件」；⚠️ v0.1 开发者预览版，官方明示不可用于生产）与 **Pi**（`earendil-works/pi`，极简底座仅保留读 / 写 / 改文件与跑命令四个工具，支持单会话内跨供应商接力）
- **总览页**：术语表新增 12 条（MoE / Jev / World Model / CE / Harness / Harness Engineering / Loop Engineering / DSH / FDE / OPC / Token）

### 变更（术语落位）

- **章节十二**：**校准 Harness 的定义**——原文把 Harness Engineering 只讲成「质检门禁」（偏窄）。本次明确区分：**「Harness」本身指承载 agent 的运行时**（工具、权限、记忆、验证的总和，Claude Code / Codex / DSH / Pi 均属此层），而 Harness Engineering 是**设计它的方法论**，两者不在同一层。同时补实操建议一条（先定 trigger / goal / 验证方式 / 停止规则，再逐级放权）
- **章节四**：cc-switch 的切换目标列表中 `Gemini CLI` 更新为 `Antigravity CLI`，与批次 1 的停服结论保持一致
- **章节十五**：页脚补「下一章」互链至章节十六；**总览页**架构图说明由「15 个章节」更新为「16 个章节」，依赖关系补一条（章节十六为横切视角），章节目录表补一行
- **star 清单新增 3 个仓库**（DSH / Pi / loop-engineering）并登记实测值；`anthropics/claude-code` 因自然增长由 147.7K 刷新为 **147.8K**

> **术语归属的两处核实（落笔前已确认，避免照抄二手来源）**
>
> 1. **Pi 的作者归属**：中文文章普遍写作「Mario Zechner（@mitsuhiko）」，实为**把两人混写**。实测 `@mitsuhiko` 是 **Armin Ronacher**（Flask / Rye 作者、Earendil Works 创始人），`@badlogic` 才是 Mario Zechner（libGDX 作者）。Pi 的规范仓库为 `earendil-works/pi`（旧路径 `badlogic/pi-mono` 会重定向至此），其 README 自称「**Pi Agent Harness**」。
> 2. **Jev 的官方定名是 `Jev`**（首字母大写，非全大写 JEV），取自 Jevons / 杰文斯悖论。

### 变更（批次 2 · 模型版本与上下文窗口）

- **章节三**：两张模型表按现役版本重写
  - **国际**：Claude 主力 → **Opus 5.5**（2026-09-22，`claude-opus-5-5`，$4/$20），并说明 **Fable 5.1 / Mythos 5.1**（2026-09-01）是「同权重、防护等级不同」的两个可用面（Fable 通用可用，Mythos 为邀请制可信访问）；GPT → **GPT-6 Astra / Sol / Luna**，上一代 GPT-5.6 的 Sol/Terra/Luna 仍在役；Gemini → **3.8 Flash / 3.8 Live**，Pro 档仍为 3.1 Pro，并注明 Gemini 4 已进入预训练但未发布
  - **国产**：DeepSeek → **V4.1-Flash**（552B MoE、原生多模态）；Qwen → **Qwen3.8-Max**（2.4T 总参 / 95B 激活）；Kimi → **K3**（2.8T）；GLM → **5.3**（744B 总参 / 40B 激活）；MiniMax → **M3**（428B / 23B 激活）
  - **上下文窗口**：200K / 256K / 128K → 普遍 **1M 级**（GPT-6 Astra 1.05M；GLM-5.3 输入 1M / 输出 128K），编程与非编程两张对比表同步
  - 新增一条**口径提示**：上下文窗口是厂商规格书上限，实际可用量受输出预留、计费与接入渠道影响，跨云（如 AWS Bedrock）标注可能不一致
- **章节三**：OpenRouter 提供商数 **60+ → 80+**（模型数 500+ 不变）
- **章节一**：最新动态补三条——**OpenClaw 2.0**（2026-08-31，官方口径 987 位贡献者 / 16,977 PR）、**2026-07-08 转入 OpenClaw Foundation**（美国 501(c)(3) 非营利组织，协议保持 MIT，OpenAI 为主要捐赠方）、最新发版 **v2026.9.5**（2026-09-19），并说明另有 extended-stable 渠道 v2026.7.35；技能系统补 **ClawHub 已拆为 Skills + Plugins 双结构** 与中国官方镜像 mirror-cn.clawhub.com
- **章节八**：LangChain / LangGraph 补 **1.0 GA**（LangChain 2025-10-23、LangGraph 2025-10-24）与核心新抽象 `create_agent`（`create_react_agent` 已废弃）
- **章节九**：LightRAG 补实测 star（39.8K），并登记进 star 清单
- **章节十一**：**MTEB 表述纠正**——原文「Qwen3-Embedding 榜单领先」已不准确，现为 MTEB(eng,v1) 第 2；多语言榜首已换为微软 **Harrier-OSS-v1-27B**（74.27），KaLM 退居第 2（72.32 分数字属实）。新增 Conan-embedding-v2（eng,v1 第 1，74.22）与 Harrier-OSS-v1 两条目；榜单链接改官方 `leaderboard.mteb.org`，并**加注 v1/v2 分数不可横比**的警示与「认准榜单名」的选型提示

> **与内部审计报告的偏差（批次 2，5 处，已按实测修正）**
>
> 1. **GPT-6 没有 Terra**。报告把 Terra 列入 GPT-6 世代；实测 Terra 属 **GPT-5.6** 一代，GPT-6 只有 Astra / Sol / Luna。
> 2. **Qwen 的「主力」判断过时**。报告称 3.7-Max / 3.7-Plus 等为主力；实测这些型号在售但**已非旗舰**，旗舰是 Qwen3.8-Max。
> 3. **OpenClaw 2.0 的贡献者数**。报告沿用第三方转载口径「933 位贡献者」；官方 release notes 为 **987 contributors / 16,977 PR**，已改用官方数字。另报告写「2026-08-31/09-01」，实际是 8 月 30 日宣布、**8 月 31 日以 v2026.8.1 发布**。
> 4. **ClawHub 技能数不可确证**。报告记「可确证至 19,000+（2026-08 口径）」；实测官方从不公布总数，第三方给出 3,286 / 5,705 / 13,000 / 19,000 / 43,000 五个互相冲突的数字（多为 SEO 内容站）。**故正文不写任何 ClawHub 技能数**，只写已确证的结构性变化。
> 5. **LangChain 1.0 GA 日期**。报告写 2025-10-22（博客发稿日），官方 changelog 为 **10-23**（LangGraph 为 10-24），已按官方口径写。
>
> 另：MTEB 多语言榜首的更替（KaLM → Harrier）报告亦未提及，仅要求「加注口径说明」，本次一并修正了名次表述。

### 重构（批次 3 · 章节二 Coding Plan）

> 本章是全站改动幅度最大的一章：原有价格**几乎全部过期**（原标注「2026 年 5 月整理」），且两张对比图是 **2026-04-22** 的第三方截图。本次逐家回官方定价页重核，并改为脚本生成原创图表。

- **章节二**：整章重写。新增「先搞清楚：三种订阅形态」一节，点明 2026 年真正的变化是**计费逻辑与产品名在重构**——`Coding Plan`（按请求次数）/ `Token Plan`（按积分、额度通兑）/ 会员共享额度池（Kimi），并提示「看到 Coding Plan 不要默认它还是按次计费」
- **价格修正（六家主流）**
  - **方舟**：Lite **40 元** / Pro **200 元**（原「40 元起」准确）；补充 2026-06-08 至 11-08 **首两月 2.5 折**（9.9 / 49.9）与优惠资格共享规则；补 **Agent Plan** 平行线（Small 40 / Medium 200，Large 与 Max 未公布）
  - **智谱 GLM**：49 元起 → **118 / 538 / 1078 元**（年付折合 94.4 / 430.4 / 862.4）；改为**积分制**（Lite 每周 10,000 积分）；模型升 **GLM-5.3 / 5.3-Flash（内测代号 OX Alpha）**
  - **Kimi**：由独立套餐 → **会员权益**。四档 **49 / 99 / 199 / 699 元**，四档**均可调用 Kimi Code**；所有会员功能共享额度池，Kimi Code 另有独立 5 小时/周限额
  - **MiniMax**：10 美元 → 国内 **49 / 119 / 469 元**；补国际站 $22 / $55 / $132
  - **阿里云**：Lite **已停售**（03-20 停新购、04-13 停续费），现仅 **Pro 一档 200 元/月**，新客首月 ¥39.90，每日 09:30 限量补货
  - **腾讯云**：原「28 元起、Hy/通用两条线」**完全吻合**，补全 8 个档位（Hy 28/78/238/468，通用 39/99/299/599）、迁移至 **TokenHub**、2026-08-31 起改积分抵扣、不支持退款/降配/到期续费
- **新增厂商**：小米 **MiMo Token Plan**（39/99/329/659）、联通云**元景 Token Plan**（15/30/45）、华为云**码道**（体验版永久免费）、摩尔线程 **AI Coding Plan**（按季）、科大讯飞 **Astron**（199/999）、**OpenCode Go**（$10，国际产品单列）
- **新增「已停售 / 已迁移」提示**：百度千帆 Coding Plan（06-25 停续费、07-13 停新购）、阿里云 Lite、讯飞无忧版/专业版、腾讯云旧混元大模型平台（旧接口 2026-09-30 终止）
- **对比图重做**：两张 2026-04 的第三方截图 → 由 **`scripts/gen_coding_plan_charts.py`** 生成的原创图表（入门档价格对比 + 对数刻度价格带对比），页内标注核查日期；体积从 188 / 257 KB 降至 146 / 141 KB
- **趋势一节重写**：原「字节方舟、智谱、Kimi 仍以自有模型为主」已不成立（方舟早已多模型聚合）；新增「价格分层而非普涨」（入门下探至 15 元、顶配上移至 1078 元）、「免费档未如期普及」、「出现企业版 + 席位制」

> **与内部审计报告的偏差（批次 3，3 处，已按官方口径修正）**
>
> 1. **Kimi 是四档而非三档，且 49 元档可用 Kimi Code**。报告写「官方三档 ¥99/199/699，¥49 为会员 Andante 档、**不支持** Kimi Code」。官方帮助中心权益表明确四档 **Andante ¥49 / Moderato ¥99 / Allegretto ¥199 / Allegro ¥699**，且**四档均标注「Kimi Code 可调用」**。报告该条为误。
> 2. **「GLM 含 Claude Pro 额度」是原文档的误读**。原文写 GLM 套餐「含 Claude Pro 额度」、多维对比表写「Claude + GLM」。官方定价页只列 **GLM-5.3 / 5.3-Flash**，「支持 Claude Code」指的是**支持在该工具里使用**，不是提供 Claude 模型。已删除该表述，并在 FAQ 单列一条澄清——这是本章过去最容易误导读者的一处。
> 3. **讯飞 ¥19 已下线**。报告把「讯飞星辰 ¥19/月」列为建议新增；实测该价属「无忧版」，**已于 2026-07 下线**，现役最低为高效版 199 元。已按现价收录并标注。
>
> 另：报告「腾讯云 28 元起」的怀疑不成立，官方文档逐档吻合；报告未提及的 **MiniMax 国际站价格**与**联通云 15 元档**本次一并补入。

### 新增（批次 4 · P2-01 / P2-02 国产 Claw 扩军）

- **章节一**：国内"龙虾"产品矩阵由 **6 款扩至 12 款**，并新增「端形态」维度（本地 / 云端 / 手机 / 跨端）
  - 新增：**小艺Claw**（华为，HarmonyOS 5.0+ 全机型，手机/平板/PC 三端）、**JVSClaw**（阿里云无影）、**DuMate 搭子**（百度智能云，PC+移动）、**Xiaomi miclaw**（小米，邀请制）、**LobsterAI 有道龙虾**（网易有道，国内首个 100% 开源桌面 Agent）、**AstronClaw**（科大讯飞）
  - 另列 4 款「值得关注但未入主表」：**HiClaw**（阿里云 Higress，开源团队版）、**纳米Work**（原 360 安全龙虾）、**UniClaw**（中国联通）、**Mavis**（MiniMax）
- **章节一**：新增「按端形态选型」表；原「六款 Claw 产品对比」改为「重点产品能力对照」并补**企业版**一行
- **章节一**：新增 **「厂商标注易错点」** 小节，收录 6 条社区常见错误（AutoClaw 厂商、UniClaw 属联通、阿里云三个团队、MaxClaw≠Mavis、AutoClaw 模型开放、KimiClaw 官方入口）
- **现有 6 款状态逐条更新**：AutoClaw 补中文名**澳龙**与 Pony-Alpha-2（内测代号）；KimiClaw 入口改为 **kimi.com/bot**，模型补「默认 K2.6，可切 K3」并注明一键部署需 Allegretto 及以上；ArkClaw 补**企业版**（席位制）；QClaw 补 **V2**（3 Agent 并行 + 智能连接器 + 龙虾管家）
- **章节一**：选型建议按新矩阵重写

> **与内部审计报告的偏差（批次 4 · P2-02，2 处，已按官方口径修正）**
>
> 1. **「MaxClaw 母产品更名 Mavis」不成立**。报告如此写；实测 MiniMax 在 2026 年 2-5 月**连续推出三款产品**——2 月 MaxClaw（云端 Claw 托管）、4 月 MaxHermes、5 月将 **MiniMax Agent 升级并更名 Mavis**。Mavis 与 MaxClaw 是**并列关系**，MaxClaw 本身未改名。已在正文与「易错点」中明确区分。
> 2. **「KimiClaw 调用 K2.6」需限定口径**。报告只要求改主入口；实测官方帮助文档写明**默认 K2.6、可在设置中切换 K3**，两个说法并存不矛盾。已按官方口径写。
>
> ⚠️ **原文一处硬错误（非报告提出，本次核实发现）**：章节一原写 AutoClaw「生态绑定 GLM 系列」「与 GLM 模型深度绑定」。实测 AutoClaw **完全开放模型接入**，官方明确支持接入**任意模型的 Coding Plan 或 API**，推荐 DeepSeek / Kimi / MiniMax / GLM。已改正。

### 变更（批次 4 · P2-03 CLI 模型支持矩阵）

- **章节四**：新增 **「CLI 模型支持矩阵」** 一节（工具 × 默认模型 × 可切换范围 × 自由度），点明 CLI 工具最关键的分化点是"能不能换模型"，并补两种换模型方式（内置选择器 / Base URL 指向第三方端点）
- **章节四**：**Codex CLI** 由「据 2026 年 4 月报道已升级至 GPT-5.2-Codex」改为现役口径——最新 **0.156.1**，出厂默认 **`gpt-6-astra`** 且默认挂 Low 推理档，`gpt-6-sol` / `gpt-6-luna` 自 0.156.1 起可选但**都不是默认**。选型对比表同步
- **章节四**：**Antigravity CLI** 补「已全面开放（官方未用 GA 字样）」「个人档 **$0/月**」与可选模型（Gemini 3.x + **Claude Sonnet 4.6 / Claude Opus 4.6 / gpt-oss-120b**，不支持 BYOK）；选型对比表与选型建议同步
- **章节二**：因 Antigravity 免费档可选 Claude 模型，把「没有任何套餐提供 Claude」收窄为「**本章这六家国产套餐都不提供**」，避免绝对化表述

---

## 2026-05-17

### 新增

- **总览页**：新增全景架构图（三层架构 + 依赖关系）、3 条学习路径（AI编程入门/RAG开发者/Agent工程师）、术语表（15 个核心术语）
- **章节十四**：新增 Prompt Engineering 章节——核心原则、CRISPE/RISEN/Few-Shot 三大框架、CoT/自我反思/结构化输出等高级技巧、常见陷阱、章节关联
- **章节十五**：新增端到端实战项目章节——RAG 知识库问答（30分钟，含完整代码）、MCP Server 创建（5分钟，含 FastMCP 代码和配置）、Vibe Coding MVP（1小时，两种方案）
- **章节四**：新增"5 分钟快速上手：Claude Code"段落
- **章节六**：新增"5 分钟快速上手：用 FastMCP 创建 MCP Server"段落
- **章节八**：新增"Agent 设计模式"（ReAct/Plan-Execute/Multi-Agent/Reflection/Router 5种模式）和"5 分钟快速上手：CrewAI"段落
- **章节九**：新增"5 分钟快速上手：LlamaIndex 搭建最简 RAG"段落
- **章节十**：新增"核心概念"——向量索引类型（HNSW/IVF/Flat）、混合检索、过滤策略
- **章节十一**：新增"核心概念"——维度选择、Chunk 策略、多向量 vs 单向量
- **README**：章节目录新增 14、15 章

### 变更

- **总览页**：更新时间从 2026-04-22 更新至 2026-05-17；章节目录从 13 章扩展至 15 章
- **章节十三**：导航链接新增"下一章：Prompt Engineering"

---

## 2026-05-16

### 修复

- **章节四**：修正 Qoder CLI 厂商归属（非阿里出品，为独立组织 Qoder-AI）和产品定位（Agentic Coding Platform，非纯 CLI）
- **章节七**：更新 Trae 条目，产品已升级为 TRAE SOLO，定位从 AI IDE 扩展为跨平台 AI 协作平台

### 新增

- **章节七**：Antigravity 补充社区生态信息（antigravity-skills、vscode-antigravity-cockpit 插件）
- **章节十二**：新增"范式与工具映射"表（4 种范式 × CLI/IDE/Skill 推荐）和"实操建议"（4 条实践路径）
- **章节十三**：新增 MTEB Leaderboard（Embedding 排行榜）和 MCP Server 市场（mcp.so）资源

---

## 2026-05-11

### 修复

- **章节七**：移除 Cursor 条目中 SpaceX 收购的虚假信息
- **章节十三**：修正 AutoGen 与 Semantic Kernel 合并为 Microsoft Agent Framework 的不准确表述
- **全局**：更新所有 Anthropic 文档链接（`docs.anthropic.com` → `platform.claude.com` / `code.claude.com`）
- **章节十三**：更新 LMArena URL（`lmarena.ai` → `arena.ai`）

### 新增

- **章节一**：更新 OpenClaw 至最新状态（370K star/76K fork/每日发版），新增最新动态时间线（创始人加入 OpenAI / ClawCon / Moltbook），新增 6 款 Claw 产品 8 维对比矩阵，新增 OpenClaw 周边生态（8 个精选项目）
- **章节三**：模型选型对比矩阵（编程 8 维对比 + 非编程 6 场景推荐）+ 选型建议
- **章节四**：CLI 工具选型对比矩阵 + 场景化选型建议
- **章节六**：MCP Server 列表扩展至 12 个（补充 Chrome DevTools/Serena/FastMCP/n8n），新增场景分类表和选型建议
- **章节七**：IDE 选型对比矩阵 + 场景化选型建议
- **章节八**：Agent 框架选型对比矩阵 + 决策树
- **章节九**：RAG 框架选型对比矩阵 + 选型路径
- **章节十**：向量数据库选型对比矩阵 + 规模/场景选型指南
- **章节十一**：Embedding 模型选型对比矩阵 + 场景化选型建议

### 变更

- **章节八**：Hermes Agent 星标数更新（109K → 142K），新增 Microsoft Agent Framework 条目
- **章节四**：OpenCode 星标数更新（147K → 158K），Claude Code 补充星标数
- **章节六**：补充 MCP Streamable HTTP 协议说明
- **章节二**：完整刷新 Coding Plan 价格表——腾讯云拆分为 Hy/通用两条线（最低 28 元起），阿里云改为 Lite/Pro 两档并扩充模型与工具列表，Kimi 更新至 K2.6，刷新趋势分析
- **章节五**：重构改写——新增 Skill 项目文件构成（SKILL.md/references/scripts/assets 四层结构），补全全部 17 个官方技能，新增分类导航和选型建议，新增延伸学习视频
- **章节九**：RAG 框架新增 Haystack；GraphRAG 和 Agentic RAG 方向补充核心流程、代表项目、4 个典型实践案例和落地建议；新增多模态 RAG 和上下文工程方向
- **章节十一**：Embedding 模型新增 Cohere Embed，KaLM-Embedding 分数表述修正为历史数据

---

## 2026-04-22

### 新增

- 新增项目封面图（`docs/public/ai-wiki-project.png`），更新 README 和 index 页面展示

### 变更

#### 模型 API（章节三）
- **Claude API**：更新至 Claude Opus 4.7（2026年4月发布），补充 4.6 版本信息
- **GPT 系列**：更新至 GPT-5.4（2026年3月发布），新增 Pro/Thinking 版本说明及原生 Computer Use 能力
- 统一表格列宽格式

#### CLI 工具（章节四）
- 更新各工具描述信息

#### 编程工具 IDE（章节七）
- 更新各工具描述信息

#### Agent 框架（章节八）
- 新增 **Hermes Agent**（Nous Research 出品，109K star，持久记忆 + 自进化 + 多平台接入）

#### 资源导航（章节十三）
- 新增 **LMArena**（LLM 对战榜 / Elo 排名）
- 所有条目补充简短功能描述标签

### 移除

- 移除 VitePress 构建配置（`docs/.vitepress/` 目录），简化项目结构
- 移除 GitHub Actions 部署流程（`.github/workflows/deploy.yml`）

### 工程

- `.gitignore` 新增 `docs/.DS_Store` 忽略规则

---

## 2026-04-22 · 初始结构

### 新增

- 项目初始化，建立 13 章知识体系框架
- 章节一：龙虾 Claw 产品系列
- 章节二：Coding Plan
- 章节三：三方模型（API）
- 章节四：CLI 种类
- 章节五：好用的 Skill
- 章节六：MCP
- 章节七：编程工具 IDE
- 章节八：Agent 框架
- 章节九：RAG 框架
- 章节十：向量知识库
- 章节十一：Embedding 模型
- 章节十二：Vibe Coding 四种
- 章节十三：资源导航
- VitePress 站点搭建与 GitHub Actions 自动部署

---

格式说明：每次更新按日期分组，分为 **新增**、**变更**、**移除**、**修复**、**工程** 五类。
