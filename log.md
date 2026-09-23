# 更新日志 (Changelog)

> 本项目所有值得关注的变化都会记录在此文件中。

---

## 2026-09-23

> 本节对应内容时效性审计（内部报告 `AUDIT-2026-09.md`）。截至目前已完成：**批次 1**（P0 硬错误修复）、**批次 2 全部**（star 数 + 模型版本 / 上下文窗口 / 零散数据）、**批次 4 的 IDE/ADE 部分与向量知识库部分**，以及**术语落位**（新增章节十六）。全部外部事实均经实测或官方来源核验。

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
