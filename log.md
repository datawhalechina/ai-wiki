# 更新日志 (Changelog)

> 本项目所有值得关注的变化都会记录在此文件中。

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
