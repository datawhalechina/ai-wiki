# 三、三方模型（API）

[← 上一章：二、Coding Plan](../chapter02/02-coding-plan.md) | [返回总览](../index.md) | [下一章：四、CLI 种类 →](../chapter04/04-cli-tools.md)

三方模型指通过 API 调用的第三方大语言模型服务，涵盖国际主流和国产模型。

## 国际主流模型 API

| 模型                                                         | 厂商      | 特点                                                         |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| **[Claude API (Opus 4.7)](https://platform.claude.com/docs/zh-CN/claude/claude-api)** | Anthropic | 最新为 **Claude Opus 4.7**（2026年4月发布），还有4.6版本（2026年2月发布） |
| **[GPT-5.4](https://developers.openai.com/api/docs)**        | OpenAI    | GPT-5.4（2026年3月6日发布），分Pro和Thinking两个版本，新增原生Computer Use能力 |
| **[Gemini 系列](https://ai.google.dev/gemini-api)**          | Google    | 多模态能力，Gemini 3 在代码评测中表现优异                    |

## 国产主流模型 API

| 模型                                                | 厂商      | 特点                      |
| ------------------------------------------------- | ------- | ----------------------- |
| **[DeepSeek 系列](https://platform.deepseek.com/)** | 深度求索    | 开源强推理模型，成本低，编码能力强       |
| **[Qwen3 系列](https://qwen.ai/apiplatform)**       | 阿里      | 多尺寸可选（32B/235B等），中文理解精准 |
| **[Kimi-K2](https://platform.moonshot.ai/)**      | 月之暗面    | 长上下文，中文场景优势             |
| **[GLM-5.x 系列](https://bigmodel.cn/console/)**    | 智谱 AI   | 国内老牌模型，编码场景持续优化         |
| **[MiniMax M2](https://www.minimaxi.com/)**       | MiniMax | 开源模型，音乐、语音、视频模型         |

## 模型聚合平台

- **[OpenRouter](https://openrouter.ai/)**：统一 API 网关，支持 500+ 模型、60+ 提供商，OpenAI 兼容接口
- **[Hugging Face](https://huggingface.co/)**：提供开源模型托管和推理服务

## 模型选型对比

### 编程场景

| 模型 | 编码能力 | 价格 | 上下文 | 速度 | 中文代码注释 |
|------|---------|------|--------|------|------------|
| Claude Opus 4.7 | ⭐⭐⭐⭐⭐ | 高 | 200K | 中 | ⭐⭐⭐⭐ |
| GPT-5.4 | ⭐⭐⭐⭐⭐ | 高 | 256K | 中 | ⭐⭐⭐ |
| Gemini 3 | ⭐⭐⭐⭐ | 中 | 1M+ | 快 | ⭐⭐⭐ |
| DeepSeek 系列 | ⭐⭐⭐⭐ | 低 | 128K | 快 | ⭐⭐⭐⭐⭐ |
| Qwen3 (235B) | ⭐⭐⭐⭐ | 中 | 128K | 快 | ⭐⭐⭐⭐⭐ |
| Kimi-K2.6 | ⭐⭐⭐⭐ | 中 | 长上下文 | 快 | ⭐⭐⭐⭐⭐ |
| GLM-5.x | ⭐⭐⭐ | 中 | 128K | 快 | ⭐⭐⭐⭐⭐ |
| MiniMax M2 | ⭐⭐⭐ | 中 | 128K | 快 | ⭐⭐⭐⭐ |

### 非编程场景

| 场景 | 首选 | 次选 | 理由 |
|------|------|------|------|
| 长文档分析 | Gemini 3 / Kimi-K2 | Claude Opus | 1M+ 上下文，原生多模态 |
| 中文写作 | Qwen3 / Kimi-K2 | DeepSeek | 中文理解精准，文风自然 |
| 多轮对话 | Claude Opus 4.7 | GPT-5.4 | 指令遵循强，逻辑一致 |
| 多模态理解 | Gemini 3 | GPT-5.4 | 原生多模态，图文理解强 |
| 低成本大批量 | DeepSeek | Qwen3-32B | 开源+低价，推理成本极低 |
| 语音/音乐生成 | MiniMax M2 | — | 原生语音和音乐模型 |

## 选型建议

- **日常编码** → **Claude Opus 4.7** 或 **DeepSeek**（前者质量最高，后者性价比最佳）
- **中文项目优先** → **Qwen3** / **DeepSeek** / **Kimi-K2**：中文理解和生成最自然
- **长文档/多模态** → **Gemini 3**：1M+ 上下文窗口，原生多模态
- **低成本试验** → **DeepSeek**：开源模型中编码能力最强，API 价格最低档
- **不想分别对接** → **OpenRouter**：一个 API 调 500+ 模型，按需切换
