# 十四、Prompt Engineering

[← 上一章：十三、资源导航](../chapter13/13-resources.md) | [返回总览](../index.md) | [下一章：十五、端到端实战项目 →](../chapter15/15-hands-on-projects.md)]

Prompt Engineering（提示词工程）是与大模型交互的核心技能——同一个模型，不同的提示词可以产出天差地别的结果。掌握提示词技巧，比切换更贵的模型更有效。

## 核心原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **明确具体** | 模型不会读心，越具体越好 | "写一封 200 字的邮件" > "写个邮件" |
| **给示例** | Few-shot 比纯指令更稳定 | 给 1-2 个输入输出样例 |
| **分步引导** | 复杂任务拆成步骤 | "第一步...第二步...第三步..." |
| **指定角色** | 角色设定影响输出风格 | "你是一位资深 Python 架构师" |
| **指定格式** | 明确输出格式 | "用 JSON 格式返回，字段包含 name, age, role" |

## 常用提示词框架

### 1. CRISPE 框架

| 要素 | 含义 | 示例 |
|------|------|------|
| **C**apacity | 角色能力 | 你是一位数据分析专家 |
| **R**ole | 具体角色 | 负责分析电商用户行为数据 |
| **I**nsight | 背景信息 | 数据来自某电商平台的 2026 年 Q1 交易记录 |
| **S**tatement | 具体任务 | 找出复购率下降的 3 个可能原因 |
| **P**ersonality | 输出风格 | 用简洁的要点列表，附数据支撑 |
| **E**xperiment | 输出格式 | 每个原因包含：现象→数据证据→建议 |

### 2. RISEN 框架

| 要素 | 含义 | 示例 |
|------|------|------|
| **R**ole | 角色 | 你是一位 DevOps 工程师 |
| **I**nstructions | 指令 | 编写一个 Docker Compose 配置 |
| **S**teps | 步骤 | 1. 定义服务 2. 配置网络 3. 设置卷挂载 |
| **E**xpectations | 期望 | 支持 MySQL + Redis + Node.js 三服务 |
| **N**arrowing | 约束 | 不使用 latest 标签，所有服务限制内存 512M |

### 3. 少样本（Few-Shot）

不解释规则，直接给示例让模型模仿：

```
将以下产品评论分类为"正面"或"负面"：

评论：这个手机拍照效果超好！→ 正面
评论：电池续航太差了 → 负面
评论：屏幕很清晰但系统有点卡 → 负面
评论：物流快，包装好 → 正面

评论：这款耳机音质不错但降噪一般 →
```

## 高级技巧

### 思维链（Chain of Thought）

让模型"一步一步思考"，显著提升推理准确率：

```
请一步一步分析以下问题：
某公司 2026 年 Q1 营收 500 万，Q2 环比增长 20%，
Q3 环比下降 10%，Q3 营收是多少？
```

> **进阶**：可以用 `"Let's think step by step"` 触发 CoT，也可以在示例中展示推理过程。

### 自我反思（Self-Reflection）

让模型检查自己的输出：

```
请写一个 Python 函数计算斐波那契数列。

写完后，请：
1. 检查边界条件是否处理正确
2. 检查是否有性能问题
3. 如有问题，修正后重新输出
```

### 结构化输出

明确要求 JSON/Markdown 表格等格式，便于程序解析：

```
请分析以下技术的优缺点，用 JSON 格式输出：

{
  "technology": "RAG",
  "pros": ["...", "..."],
  "cons": ["...", "..."],
  "best_for": "..."
}
```

### 系统提示词（System Prompt）

设定模型的全局行为，比用户消息更持久：

```
你是一个代码助手，遵循以下规则：
1. 永远使用 Python 类型注解
2. 函数必须有 docstring
3. 优先使用标准库，减少第三方依赖
4. 错误处理使用自定义异常类
```

## 常见陷阱

| 陷阱 | 问题 | 解决方案 |
|------|------|---------|
| 指令模糊 | "帮我优化一下" → 输出不可控 | 明确优化目标："将查询时间从 5s 降到 1s 以内" |
| 负面指令失效 | "不要用 JSON" → 模型可能仍用 | 用正面指令替代："使用 YAML 格式" |
| 上下文过长 | 塞入太多信息，模型忽略关键部分 | 只提供必要上下文，用分步代替一次性 |
| 过度约束 | 10 条规则互相矛盾 | 规则不超过 5 条，按优先级排列 |
| 忽略温度 | 创意任务用 temperature=0 | 事实性任务 temperature=0，创意任务 0.7-1.0 |

## Prompt Engineering 与其他章节的关系

| 章节 | 关联 |
|------|------|
| Skill(5) | SKILL.md 本质就是结构化的 System Prompt |
| RAG(9) | 检索结果拼接到 prompt 中，拼接策略直接影响 RAG 效果 |
| Agent(8) | Agent 的指令遵循能力取决于 prompt 质量 |
| CLI(4) | Claude Code 等 CLI 工具的对话即 prompt 交互 |
| Vibe Coding(12) | Vibe Coding 的核心技能就是写好 prompt |

## 延伸学习

- **[Anthropic Prompt Engineering 互动教程](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)**
- **[OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)**
- **[Learn Prompting（开源课程）](https://learnprompting.org/)**
