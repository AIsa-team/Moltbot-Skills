# OpenClaw LLM Router 🧠

**Unified LLM Gateway for autonomous agents. Powered by AIsa.**

One API key. 70+ models. Route requests to GPT, Claude, Gemini, Grok and more.

## Quick Start

```bash
# Set your API key
export AISA_API_KEY="your-key"

# Simple chat completion
python3 scripts/llm_router_client.py chat --model gpt-4.1 --message "Hello!"

# Stream response
python3 scripts/llm_router_client.py chat --model claude-3-sonnet --message "Write a poem" --stream

# Vision analysis
python3 scripts/llm_router_client.py vision --model gpt-4o --image "https://example.com/image.jpg" --prompt "Describe this"

# Compare models
python3 scripts/llm_router_client.py compare --models "gpt-4.1,claude-3-sonnet" --message "Explain AI"

# List models
python3 scripts/llm_router_client.py models
```

## Using with OpenAI SDK

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["AISA_API_KEY"],
    base_url="https://api.aisa.one/v1"
)

response = client.chat.completions.create(
    model="gpt-4.1",  # Or claude-3-sonnet, gemini-2.0-flash, etc.
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## Supported Models

| Family | Models |
|--------|--------|
| OpenAI | gpt-4.1, gpt-4o, gpt-4o-mini, o1, o1-mini, o3-mini |
| Anthropic | claude-3-5-sonnet, claude-3-opus, claude-3-sonnet |
| Google | gemini-2.0-flash, gemini-1.5-pro, gemini-1.5-flash |
| xAI | grok-2, grok-beta |
| Meta | llama-3.1-405b, llama-3.1-70b, llama-3.1-8b |
| Mistral | mistral-large, mistral-medium, mixtral-8x7b |

> Check [marketplace.aisa.one/pricing](https://marketplace.aisa.one/pricing) for full model list.

See [SKILL.md](SKILL.md) for full documentation.
