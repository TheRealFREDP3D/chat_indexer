---
tags:
  - "#openai"
  - "#text"
  - "#images"
  - "#audio"
  - "#ai"
  - "#gemini-api"
  - "#large-language-models"
  - "#multimodal-models"
description: 
author: 
x: 
github: 
website: 
source: 
created: Monday, March 31st 2025, 7:12:56 pm
title: Gemini Models Gemini API
---

# Gemini Models Gemini API

Gemini 2.5 Pro Experimental, our most advanced model, is now available! [Learn more](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/)

## Model Variants

The Gemini API offers different models that are optimized for specific use cases. Here's a brief overview of Gemini variants that are available:

| Model variant | Input(s) | Output | Optimized for |
| --- | --- | --- | --- |
| [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/#gemini-2.5-pro-exp-03-25)   `gemini-2.5-pro-exp-03-25` | Audio, images, videos, and text | Text | Enhanced thinking and reasoning, multimodal understanding, advanced coding, and more |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/#gemini-2.0-flash)   `gemini-2.0-flash` | Audio, images, videos, and text | Text, images (experimental), and audio (coming soon) | Next generation features, speed, thinking, realtime streaming, and multimodal generation |
| [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/#gemini-2.0-flash-lite)   `gemini-2.0-flash-lite` | Audio, images, videos, and text | Text | Cost efficiency and low latency |
| [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/#gemini-1.5-flash)   `gemini-1.5-flash` | Audio, images, videos, and text | Text | Fast and versatile performance across a diverse variety of tasks |
| [Gemini 1.5 Flash-8B](https://ai.google.dev/gemini-api/docs/#gemini-1.5-flash-8b)   `gemini-1.5-flash-8b` | Audio, images, videos, and text | Text | High volume and lower intelligence tasks |
| [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/#gemini-1.5-pro)   `gemini-1.5-pro` | Audio, images, videos, and text | Text | Complex reasoning tasks requiring more intelligence |
| [Gemini Embedding](https://ai.google.dev/gemini-api/docs/#gemini-embedding)   `gemini-embedding-exp` | Text | Text embeddings | Measuring the relatedness of text strings |
| [Imagen 3](https://ai.google.dev/gemini-api/docs/#imagen-3)   `imagen-3.0-generate-002` | Text | Images | Our most advanced image generation model |

You can view the rate limits for each model on the [rate limits page](https://ai.google.dev/gemini-api/docs/rate-limits).

### Gemini 2.5 Pro Experimental

Gemini 2.5 Pro Experimental is our state-of-the-art thinking model, capable of reasoning over complex problems in code, math, and STEM, as well as analyzing large datasets, codebases, and documents using long context.

[Try in Google AI Studio](https://aistudio.google.com/?model=gemini-2.5-pro-exp-03-25)

#### Model Details

| Property | Description |
| --- | --- |
| Model code | `gemini-2.5-pro-exp-03-25` |
| Supported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  1,048,576  **Output token limit**  65,536 |
| Capabilities | **Structured outputs**  Supported  **Caching**  Not supported  **Tuning**  Not supported  **Function calling**  Supported  **Code execution**  Supported  **Search grounding**  Supported  **Image generation**  Not supported  **Native tool use**  Supported  **Audio generation**  Not supported  **Live API**  Not supported  **Thinking**  Supported |
| Versions | Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details. - Experimental: `gemini-2.5-pro-exp-03-25` |
| Latest update | March 2025 |
| Knowledge cutoff | January 2025 |

### Gemini 2.0 Flash

Gemini 2.0 Flash delivers next-gen features and improved capabilities, including superior speed, native tool use, multimodal generation, and a 1M token context window.

[Try in Google AI Studio](https://aistudio.google.com/?model=gemini-2.0-flash-001)

#### Model Details

| Property | Description |
| --- | --- |
| Model code | `models/gemini-2.0-flash` |
| Supported data types | **Inputs**  Audio, images, video, and text  **Output**  Text, images (experimental), and audio(coming soon) |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| Capabilities | **Structured outputs**  Supported  **Caching**  Coming soon  **Tuning**  Not supported  **Function calling**  Supported  **Code execution**  Supported  **Search**  Supported  **Image generation**  Experimental  **Native tool use**  Supported  **Audio generation**  Coming soon  **Live API**  Experimental  **Thinking**  Experimental |
| Versions | Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details. - Latest: `gemini-2.0-flash` - Stable: `gemini-2.0-flash-001` - Experimental: `gemini-2.0-flash-exp` - Experimental: `gemini-2.0-flash-thinking-exp-01-21` |
| Latest update | February 2025 |
| Knowledge cutoff | August 2024 |

### Gemini 2.0 Flash-Lite

A Gemini 2.0 Flash model optimized for cost efficiency and low latency.

[Try in Google AI Studio](https://aistudio.google.com/?model=gemini-2.0-flash-lite)

#### Model Details

| Property | Description |
| --- | --- |
| Model code | `models/gemini-2.0-flash-lite` |
| Supported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| Capabilities | **Structured outputs**  Supported  **Caching**  Not supported  **Tuning**  Not supported  **Function calling**  Not supported  **Code execution**  Not supported  **Search**  Not supported  **Image generation**  Not supported  **Native tool use**  Not supported  **Audio generation**  Not supported  **Live API**  Not supported |
| Versions | Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details. - Latest: `gemini-2.0-flash-lite` - Stable: `gemini-2.0-flash-lite-001` |
| Latest update | February 2025 |
| Knowledge cutoff | August 2024 |

### Gemini 1.5 Flash

Gemini 1.5 Flash is a fast and versatile multimodal model for scaling across diverse tasks.

[Try in Google AI Studio](https://aistudio.google.com/?model=gemini-1.5-flash)

#### Model Details

| Property | Description |
| --- | --- |
| Model code | `models/gemini-1.5-flash` |
| Supported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| Audio/visual specs | **Maximum number of images per prompt**  3,600  **Maximum video length**  1 hour  **Maximum audio length**  Approximately 9.5 hours |
| Capabilities | **System instructions**  Supported  **JSON mode**  Supported  **JSON schema**  Supported  **Adjustable safety settings**  Supported  **Caching**  Supported  **Tuning**  Supported  **Function calling**  Supported  **Code execution**  Supported  **Live API**  Not supported |
| Versions | Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details. - Latest: `gemini-1.5-flash-latest` - Latest stable: `gemini-1.5-flash` - Stable: - `gemini-1.5-flash-001`  - `gemini-1.5-flash-002` |
| Latest update | September 2024 |

### Gemini 1.5 Flash-8B

Gemini 1.5 Flash-8B is a small model designed for lower intelligence tasks.

[Try in Google AI Studio](https://aistudio.google.com/?model=gemini-1.5-flash)

#### Model Details

| Property | Description |
| --- | --- |
| Model code | `models/gemini-1.5-flash-8b` |
| Supported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| Audio/visual specs | **Maximum number of images per prompt**  3,600  **Maximum video length**  1 hour  **Maximum audio length**  Approximately 9.5 hours |
| Capabilities | **System instructions**  Supported  **JSON mode**  Supported  **JSON schema**  Supported  **Adjustable safety settings**  Supported  **Caching**  Supported  **Tuning**  Supported  **Function calling**  Supported  **Code execution**  Supported  **Live API**  Not supported |
| Versions | Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details. - Latest: `gemini-1.5-flash-8b-latest` - Latest stable: `gemini-1.5-flash-8b` - Stable: - `gemini-1.5-flash-8b-001` |
| Latest update | October 2024 |

### Gemini 1.5 Pro

Try [Gemini 2.0 Pro Experimental](https://ai.google.dev/gemini-api/docs/models/experimental-models#available-models), our most advanced Gemini model to date.

Gemini 1.5 Pro is a mid-size multimodal model that is optimized for a wide-range of reasoning tasks. 1.5 Pro can process large amounts of data at once, including 2 hours of video, 19 hours of audio, codebases with 60,000 lines of code, or 2,000 pages of text.

[Try in Google AI Studio](https://aistudio.google.com/?model=gemini-1.5-pro)

#### Model Details

| Property | Description |
| --- | --- |
| Model code | `models/gemini-1.5-pro` |
| Supported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  2,097,152  **Output token limit**  8,192 |
| Audio/visual specs | **Maximum number of images per prompt**  7,200  **Maximum video length**  2 hours  **Maximum audio length**  Approximately 19 hours |
| Capabilities | **System instructions**  Supported  **JSON mode**  Supported  **JSON schema**  Supported  **Adjustable safety settings**  Supported  **Caching**  Supported  **Tuning**  Not supported  **Function calling**  Supported  **Code execution**  Supported  **Live API**  Not supported |
| Versions | Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details. - Latest: `gemini-1.5-pro-latest` - Latest stable: `gemini-1.5-pro` - Stable: - `gemini-1.5-pro-001`  - `gemini-1.5-pro-002` |
| Latest update | September 2024 |

### Imagen 3

Imagen 3 is our highest quality text-to-image model, capable of generating images with even better detail, richer lighting and fewer distracting artifacts than our previous models.

#### Model Details

| Property | Description |
| --- | --- |
| Model code | **Gemini API**  `imagen-3.0-generate-002` |
| Supported data types | **Input**  Text  **Output**  Images |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  N/A  **Output images**  Up to to 4 |
| Latest update | February 2025 |

### Gemini Embedding Experimental

`Gemini embedding` achieves a [SOTA performance](https://deepmind.google/research/publications/157741/) across many key dimensions including code, multi-lingual, and retrieval.

#### Model Details

| Property | Description |
| --- | --- |
| Model code | **Gemini API**  `gemini-embedding-exp-03-07` |
| Supported data types | **Input**  Text  **Output**  Text embeddings |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  8,192  **Output dimension size**  Elastic, supports: 3072, 1536, or 768 |
| Latest update | March 2025 |

### Text Embedding and Embedding

#### Text Embedding

Try our new [experimental Gemini embedding model](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/) which achieves state-of-the-art performance.

[Text embeddings](https://ai.google.dev/gemini-api/docs/embeddings) are used to measure the relatedness of strings and are widely used in many AI applications.

`text-embedding-004` achieves a [stronger retrieval performance and outperforms existing models](https://arxiv.org/pdf/2403.20327) with comparable dimensions, on the standard MTEB embedding benchmarks.

##### Model Details

| Property | Description |
| --- | --- |
| Model code | **Gemini API**  `models/text-embedding-004` |
| Supported data types | **Input**  Text  **Output**  Text embeddings |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  2,048  **Output dimension size**  768 |
| Rate limits <sup><a href="https://ai.google.dev/gemini-api/docs/#rate-limits">[**]</a></sup> | 1,500 requests per minute |
| Adjustable safety settings | Not supported |
| Latest update | April 2024 |

#### Embedding

You can use the Embedding model to generate [text embeddings](https://ai.google.dev/gemini-api/docs/embeddings) for input text.

The Embedding model is optimized for creating embeddings with 768 dimensions for text of up to 2,048 tokens.

##### Embedding Model Details

| Property | Description |
| --- | --- |
| Model code | `models/embedding-001` |
| Supported data types | **Input**  Text  **Output**  Text embeddings |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  2,048  **Output dimension size**  768 |
| Rate limits <sup><a href="https://ai.google.dev/gemini-api/docs/#rate-limits">[**]</a></sup> | 1,500 requests per minute |
| Adjustable safety settings | Not supported |
| Latest update | December 2023 |

### AQA

You can use the AQA model to perform [Attributed Question-Answering](https://ai.google.dev/gemini-api/docs/semantic_retrieval) (AQA)–related tasks over a document, corpus, or a set of passages. The AQA model returns answers to questions that are grounded in provided sources, along with estimating answerable probability.

#### Model Details

| Property | Description |
| --- | --- |
| Model code | `models/aqa` |
| Supported data types | **Input**  Text  **Output**  Text |
| Supported language | English |
| Token limits <sup><a href="https://ai.google.dev/gemini-api/docs/#token-size">[*]</a></sup> | **Input token limit**  7,168  **Output token limit**  1,024 |
| Rate limits <sup><a href="https://ai.google.dev/gemini-api/docs/#rate-limits">[**]</a></sup> | 1,500 requests per minute |
| Adjustable safety settings | Supported |
| Latest update | December 2023 |

See the [examples](https://ai.google.dev/examples) to explore the capabilities of these model variations.

\[\*\] A token is equivalent to about 4 characters for Gemini models. 100 tokens are about 60-80 English words.

## Model Version name Patterns

Gemini models are available in either *preview* or *stable* versions. In your code, you can use one of the following model name formats to specify which model and version you want to use.

- **Latest:** Points to the cutting-edge version of the model for a specified generation and variation. The underlying model is updated regularly and might be a preview version. Only exploratory testing apps and prototypes should use this alias.
 To specify the latest version, use the following pattern:`<model>-<generation>-<variation>-latest`. For example,`gemini-1.0-pro-latest`.
- **Latest stable:** Points to the most recent stable version released for the specified model generation and variation.
 To specify the latest stable version, use the following pattern:`<model>-<generation>-<variation>`. For example, `gemini-1.0-pro`.
- **Stable:** Points to a specific stable model. Stable models usually don't change. Most production apps should use a specific stable model.
 To specify a stable version, use the following pattern:`<model>-<generation>-<variation>-<version>`. For example,`gemini-1.0-pro-001`.
- **Experimental:** Points to an experimental model (not for production use). We release experimental models to gather feedback, get our latest updates into the hands of developers quickly, and highlight the pace of innovation happening at Google.
 To specify an experimental version, use the following pattern:`<model>-<generation>-<variation>-<version>`. For example,`gemini-2.0-pro-exp-02-05`.

## Experimental Models

In addition to the production ready models, the Gemini API offers experimental models (not for production use, as defined in our [Terms](https://ai.google.dev/gemini-api/terms) ).

We release experimental models to gather feedback, get our latest updates into the hands of developers quickly, and highlight the pace of innovation happening at Google. What we learn from experimental launches informs how we release models more widely. An experimental model can be swapped for another without prior notice. We don't guarantee that an experimental model will become a stable model in the future.

### Previous Experimental Models

As new versions or stable releases become available, we remove and replace experimental models. You can find the previous experimental models we released in the following section along with the replacement version:

| Model code | Base model | Replacement version |
| --- | --- | --- |
| `gemini-2.0-pro-exp-02-05` | Gemini 2.0 Pro Experimental | `gemini-2.5-pro-exp-03-25` |
| `gemini-2.0-flash-exp` | Gemini 2.0 Flash | `gemini-2.0-flash` |
| `gemini-exp-1206` | Gemini 2.0 Pro | `gemini-2.0-pro-exp-02-05` |
| `gemini-2.0-flash-thinking-exp-1219` | Gemini 2.0 Flash Thinking | `gemini-2.0-flash-thinking-exp-01-21` |
| `gemini-exp-1121` | Gemini | `gemini-exp-1206` |
| `gemini-exp-1114` | Gemini | `gemini-exp-1206` |
| `gemini-1.5-pro-exp-0827` | Gemini 1.5 Pro | `gemini-exp-1206` |
| `gemini-1.5-pro-exp-0801` | Gemini 1.5 Pro | `gemini-exp-1206` |
| `gemini-1.5-flash-8b-exp-0924` | Gemini 1.5 Flash-8B | `gemini-1.5-flash-8b` |
| `gemini-1.5-flash-8b-exp-0827` | Gemini 1.5 Flash-8B | `gemini-1.5-flash-8b` |

## Supported Languages

Gemini models are trained to work with the following languages:

- Arabic ( `ar` )
- Bengali ( `bn` )
- Bulgarian ( `bg` )
- Chinese simplified and traditional ( `zh` )
- Croatian ( `hr` )
- Czech ( `cs` )
- Danish ( `da` )
- Dutch ( `nl` )
- English ( `en` )
- Estonian ( `et` )
- Finnish ( `fi` )
- French ( `fr` )
- German ( `de` )
- Greek ( `el` )
- Hebrew ( `iw` )
- Hindi ( `hi` )
- Hungarian ( `hu` )
- Indonesian ( `id` )
- Italian ( `it` )
- Japanese ( `ja` )
- Korean ( `ko` )
- Latvian ( `lv` )
- Lithuanian ( `lt` )
- Norwegian ( `no` )
- Polish ( `pl` )
- Portuguese ( `pt` )
- Romanian ( `ro` )
- Russian ( `ru` )
- Serbian ( `sr` )
- Slovak ( `sk` )
- Slovenian ( `sl` )
- Spanish ( `es` )
- Swahili ( `sw` )
- Swedish ( `sv` )
- Thai ( `th` )
- Turkish ( `tr` )
- Ukrainian ( `uk` )
- Vietnamese ( `vi` )
