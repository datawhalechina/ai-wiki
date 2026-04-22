# 更新日志 (Changelog)

> 本项目所有值得关注的变化都会记录在此文件中。

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
