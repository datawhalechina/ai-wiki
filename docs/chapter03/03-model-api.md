# 三、三方模型（API）

[← 上一章：二、Coding Plan](../chapter02/02-coding-plan.md) | [返回总览](../index.md) | [下一章：四、CLI 种类 →](../chapter04/04-cli-tools.md)

三方模型指通过 API 调用的第三方大语言模型服务，涵盖国际主流和国产模型。

## 国际主流模型 API

| 模型                                                         | 厂商      | 特点                                                         |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| **[Claude API (Opus 4.7)](https://docs.anthropic.com/zh-CN/docs/claude/claude-api)** | Anthropic | 最新为 **Claude Opus 4.7**（2026年4月发布），还有4.6版本（2026年2月发布） |
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
