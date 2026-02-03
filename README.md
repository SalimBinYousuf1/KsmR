<div align="center">
  <img src="ksmr_logo.png" alt="KsmR" width="500">
  <h1>KsmR: Ultra-Lightweight Personal AI Assistant</h1>
  <p>
    <a href="https://pypi.org/project/ksmr/"><img src="https://img.shields.io/pypi/v/ksmr" alt="PyPI"></a>
    <a href="https://pepy.tech/project/ksmr"><img src="https://static.pepy.tech/badge/ksmr" alt="Downloads"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue" alt="Python">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
  </p>
</div>

🐈 **KsmR** is an **ultra-lightweight** personal AI assistant rebranded from nanobot.

⚡️ Delivers core agent functionality in just **~4,000** lines of code.

## 📢 News

- **2026-02-03** 🎉 KsmR launched! Added support for **Zhipu API**, **Z.ai API**, **SerpAPI**, and **Serper API**.

## Key Features of KsmR:

🪶 **Ultra-Lightweight**: Minimal footprint, lightning-fast startup.

🔬 **Research-Ready**: Clean, readable code that's easy to understand, modify, and extend.

🤖 **Multi-Provider**: Support for OpenRouter, Anthropic, OpenAI, Gemini, **Zhipu**, and **Z.ai**.

🔍 **Web Search**: Integrated support for Brave Search, **SerpAPI**, and **Serper**.

💎 **Easy-to-Use**: One-click to deploy and you're ready to go.

## 🏗️ Architecture

<p align="center">
  <img src="ksmr_arch.png" alt="KsmR architecture" width="800">
</p>

## ✨ Features

<table align="center">
  <tr align="center">
    <th><p align="center">📈 24/7 Real-Time Market Analysis</p></th>
    <th><p align="center">🚀 Full-Stack Software Engineer</p></th>
    <th><p align="center">📅 Smart Daily Routine Manager</p></th>
    <th><p align="center">📚 Personal Knowledge Assistant</p></th>
  </tr>
  <tr>
    <td align="center"><p align="center"><img src="case/search.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/code.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/scedule.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/memory.gif" width="180" height="400"></p></td>
  </tr>
  <tr>
    <td align="center">Discovery • Insights • Trends</td>
    <td align="center">Develop • Deploy • Scale</td>
    <td align="center">Schedule • Automate • Organize</td>
    <td align="center">Learn • Memory • Reasoning</td>
  </tr>
</table>

## 📦 Install

**Install from PyPi**

```bash
pip install ksmr
```

**Install from source** (recommended for development)

```bash
git clone https://github.com/your-username/KsmR.git
cd KsmR
pip install -e .
```

## 🚀 Quick Start

> [!TIP]
> Set your API key in `~/.ksmr/config.json`.
> Get API keys: [OpenRouter](https://openrouter.ai/keys) (LLM) · [Brave Search](https://brave.com/search/api/) (optional) · [Serper](https://serper.dev/) (optional)

**1. Initialize**

```bash
ksmr onboard
```

**2. Configure** (`~/.ksmr/config.json`)

```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    },
    "zhipu": {
      "apiKey": "your-zhipu-key"
    }
  },
  "tools": {
    "web": {
      "search": {
        "serper_api_key": "your-serper-key"
      }
    }
  }
}
```


**3. Chat**

```bash
ksmr agent -m "What is 2+2?"
```

## 💬 Chat Apps

Talk to your KsmR through Telegram or WhatsApp — anytime, anywhere.

| Channel | Setup |
|---------|-------|
| **Telegram** | Easy (just a token) |
| **WhatsApp** | Medium (scan QR) |

<details>
<summary><b>Telegram</b> (Recommended)</summary>

**1. Create a bot**
- Open Telegram, search `@BotFather`
- Send `/newbot`, follow prompts
- Copy the token

**2. Configure**

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allowFrom": ["YOUR_USER_ID"]
    }
  }
}
```

**3. Run**

```bash
ksmr gateway
```

</details>

## ⚙️ Configuration

KsmR supports multiple LLM providers and search engines. You can configure them in `~/.ksmr/config.json` or via environment variables prefixed with `KSMR_`.

### Search Providers
- **Brave Search**: Set `BRAVE_API_KEY`
- **SerpAPI**: Set `SERPAPI_API_KEY`
- **Serper**: Set `SERPER_API_KEY`

### LLM Providers
- **OpenRouter**, **Anthropic**, **OpenAI**, **Gemini**, **Zhipu**, **Z.ai**

## CLI Reference

| Command | Description |
|---------|-------------|
| `ksmr onboard` | Initialize config & workspace |
| `ksmr agent -m "..."` | Chat with the agent |
| `ksmr agent` | Interactive chat mode |
| `ksmr gateway` | Start the gateway |
| `ksmr status` | Show status |
| `ksmr channels login` | Link WhatsApp (scan QR) |
| `ksmr channels status` | Show channel status |

## 🤝 License

MIT License
