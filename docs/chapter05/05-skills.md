# 五、好用的 Skill

[← 上一章：四、CLI 种类](../chapter04/04-cli-tools.md) | [返回总览](../index.md) | [下一章：六、MCP →](../chapter06/06-mcp.md)

Skills（技能）是一种为 AI 预定义可复用的专业能力的机制。通过 Skills，你可以把常用的操作流程、专业知识、行为规范封装成一个"技能包"，让 AI 在特定场景下自动激活和使用。

## Skill 项目文件构成

一个完整的 Skill 就像一个料理配方，由四类文件组成：

| 文件/目录 | 角色 | 类比 | 说明 |
|-----------|------|------|------|
| **`SKILL.md`** | 技能 | 🧾 配方 | 技能的核心定义文件，描述技能的功能、触发条件和执行流程。每个 Skill 必须有 |
| **`references/`** | 引用 | 📖 参考书 | 背景知识、API 文档、规范说明、示例代码等。AI 在需要时参考，但不直接执行 |
| **`scripts/`** | 工具 | 🔧 厨具 | 可执行的辅助脚本（Python/Bash 等），处理文件转换、数据提取、格式生成等确定性任务 |
| **`assets/`** | 资产 | 🥚 材料 | 模板文件、图片、字体、品牌素材等静态资源，供 AI 在处理任务时使用和引用 |

以 Anthropic 官方 [PDF 技能](https://github.com/anthropics/skills/tree/main/skills/pdf) 为例：

```
pdf/
├── SKILL.md          ← 配方：定义 PDF 处理的核心流程
├── reference.md      ← 引用：PDF 格式规范和 API 参考
├── forms.md          ← 引用：表单填写说明
├── scripts/          ← 工具：PDF 转换和处理的辅助脚本
└── LICENSE.txt
```

> 理解这个结构后，你可以用 [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 快速创建自己的 Skill，或参照官方 Skill 的结构自行组织。

## Skill 生态与市场

| 平台 | 规模 | 特点 |
|------|------|------|
| **[Anthropic 官方 Skills](https://github.com/anthropics/skills)** | 132K star，17 个官方技能 | 官方维护，质量最高，与 Claude Code 深度绑定 |
| **[OpenClaw Skills Registry](https://github.com/VoltAgent/awesome-openclaw-skills)** | 48K star，5400+ 技能 | OpenClaw 生态最大技能合集，社区驱动 |
| **[awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)** | 12K star | 精选 Claude 技能和工具列表 |
| **[Cursor Skills](https://cursor.com/cn/docs/skills)** | IDE 内建 | Cursor 生态，Agent/MCP 集成 |

## Anthropic 官方技能一览

以下为 [Anthropic Skills 仓库](https://github.com/anthropics/skills)（132K star）的全部官方技能：

| 技能 | 用途 |
|------|------|
| **[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)** | 创建、修改和评估技能 |
| **[frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)** | 生产级前端界面设计与实现 |
| **[web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder)** | 复杂 Web 应用（React + Tailwind + shadcn/ui） |
| **[webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing)** | Web 应用端到端测试（Playwright） |
| **[mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder)** | 构建 MCP Server |
| **[claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api)** | Claude API 应用开发 |
| **[doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)** | 文档协作撰写 |
| **[pdf](https://github.com/anthropics/skills/tree/main/skills/pdf)** | PDF 文件处理 |
| **[docx](https://github.com/anthropics/skills/tree/main/skills/docx)** | Word 文档生成与编辑 |
| **[pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)** | PPT 演示文稿生成 |
| **[xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx)** | Excel 电子表格处理 |
| **[brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines)** | 品牌视觉规范应用 |
| **[theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory)** | 主题与视觉风格工厂 |
| **[canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design)** | Canvas 画布设计 |
| **[algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art)** | 算法艺术生成（p5.js） |
| **[internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms)** | 内部通讯文案撰写 |
| **[slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator)** | Slack GIF 动图创建 |

## 技能分类导航

按使用场景快速定位：

### 开发编码
- **API 开发**：[claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api)、[mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder)
- **前端开发**：[frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)、[web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder)
- **测试**：[webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing)

### 文档办公
- **文档撰写**：[doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)
- **Office 三件套**：[pdf](https://github.com/anthropics/skills/tree/main/skills/pdf)、[docx](https://github.com/anthropics/skills/tree/main/skills/docx)、[xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx)
- **演示汇报**：[pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)、[canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design)

### 设计创意
- **品牌设计**：[brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines)、[theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory)
- **创意生成**：[algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art)、[slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator)

### 团队协作
- **内部沟通**：[internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms)
- **技能管理**：[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

## 选型建议

- **刚接触 Skill** → 先从 Anthropic 官方 17 个技能开始，质量高、文档全
- **需要特定功能** → 搜索 [OpenClaw Skills Registry](https://github.com/VoltAgent/awesome-openclaw-skills)（5400+），按分类筛选
- **自定义工作流** → 用 [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 创建专属技能
- **IDE 内使用** → Cursor / Windsurf / Trae 各有内建 Skills 生态，在 IDE 内直接激活

## 延伸学习

- 🎬 [手把手彻底学会 Agent Skills！【小白教程】](https://www.bilibili.com/video/BV1G3FNznEiS) — 秋芝2046（88.9 万粉），54.7 万播放，从原理到实战，手把手做出自己的 Skill
