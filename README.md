# AI-Wiki：AI开发者全景式工具与资源导航

> [!CAUTION]
> ⚠️ Alpha 内测版本：内容持续更新中，欢迎通过 Issue / PR 提交建议与修订。

![AI-Wiki 项目封面](docs/public/ai-wiki-project.png)

`ai-wiki` 是一个开源、社区驱动的 AI 开发知识导航项目，聚焦工具链、模型服务、框架选型与实践范式，帮助开发者降低学习与决策成本。

## 项目受众

面向三类人群：

1. **开发者**：快速做框架/模型/工具选型，跟进前沿动态。
2. **学习者**：按结构化路径建立 AI 生态认知，直达优质资源。
3. **贡献者**：通过补充内容和修正信息共建开放知识库。

**欢迎使用、参与并共同建设 ai-wiki，让 AI 开发更简单、更高效。**

## 快速入口

- 在线阅读：[https://datawhalechina.github.io/ai-wiki](https://datawhalechina.github.io/ai-wiki)
- 正文总览：[`docs/index.md`](docs/index.md)
- 章节正文：`docs/chapterXX/XX-*.md`

## 内容结构

- `README.md`：项目介绍、导航入口、贡献说明
- `docs/index.md`：正文总览目录页
- `docs/chapter01` ~ `docs/chapter16`：按主题介绍；每章支持前后章与总览互链
- `scripts/`：维护工具（star 数批量刷新）

## 章节目录

| 章节 | 文件 |
| --- | --- |
| 一、龙虾 Claw 产品系列 | [`01-openclaw-ecosystem.md`](docs/chapter01/01-openclaw-ecosystem.md) |
| 二、Coding Plan | [`02-coding-plan.md`](docs/chapter02/02-coding-plan.md) |
| 三、三方模型（API） | [`03-model-api.md`](docs/chapter03/03-model-api.md) |
| 四、CLI 种类 | [`04-cli-tools.md`](docs/chapter04/04-cli-tools.md) |
| 五、好用的 Skill | [`05-skills.md`](docs/chapter05/05-skills.md) |
| 六、MCP | [`06-mcp.md`](docs/chapter06/06-mcp.md) |
| 七、编程工具 IDE | [`07-ide-tools.md`](docs/chapter07/07-ide-tools.md) |
| 八、Agent 框架 | [`08-agent-frameworks.md`](docs/chapter08/08-agent-frameworks.md) |
| 九、RAG 框架 | [`09-rag-frameworks.md`](docs/chapter09/09-rag-frameworks.md) |
| 十、向量知识库 | [`10-vector-databases.md`](docs/chapter10/10-vector-databases.md) |
| 十一、Embedding 模型 | [`11-embedding-models.md`](docs/chapter11/11-embedding-models.md) |
| 十二、Vibe Coding 四种 | [`12-vibe-coding.md`](docs/chapter12/12-vibe-coding.md) |
| 十三、资源导航 | [`13-resources.md`](docs/chapter13/13-resources.md) |
| 十四、Prompt Engineering | [`14-prompt-engineering.md`](docs/chapter14/14-prompt-engineering.md) |
| 十五、端到端实战项目 | [`15-hands-on-projects.md`](docs/chapter15/15-hands-on-projects.md) |
| 十六、AI 时代的角色与商业 | [`16-roles-and-business.md`](docs/chapter16/16-roles-and-business.md) |

## 参与贡献

- 发现问题欢迎提 [Issue](https://github.com/datawhalechina/ai-wiki/issues)
- 欢迎通过 PR 完善内容、修复链接、补充新工具
- 如需参与 Datawhale 项目协作，可参考 [Datawhale 开源项目指南](https://github.com/datawhalechina/DOPMC/blob/main/GUIDE.md)
- 内容变更请同步更新 [`log.md`](log.md)（Changelog，按日期分组）

## 维护

本项目的时效性内容（模型版本、订阅价格、GitHub 星标）会持续过期，约**每季度**做一次核查。其中星标数据已脚本化，无需手工核对：

```bash
scripts/update_stars.sh                    # 预演：只输出差异表，不写盘
scripts/update_stars.sh --apply            # 写入文件
scripts/update_stars.sh --check            # 有差异时退出码 1，可挂 CI
scripts/update_stars.sh --repo owner/name  # 单仓库快查
```

脚本用 `gh api` 取实测值（需先 `gh auth login`），目标行由 [`scripts/stars.manifest`](scripts/stars.manifest) 按「行级唯一片段」定位。新增条目时请先跑预演——若出现"命中片段但该行没有 star 数字"的警告，说明片段不够唯一，需据其收紧。

## 关注我们

<div align=center>
<p>扫描下方二维码关注公众号：Datawhale</p>
<img src="https://raw.githubusercontent.com/datawhalechina/pumpkin-book/master/res/qrcode.jpeg" width = "180" height = "180">
</div>

## LICENSE

本作品采用 [知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/) 进行许可。
