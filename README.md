# 🌦️ Weather MCP Server

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastMCP](https://img.shields.io/badge/FastMCP-MCP_1.21-7928CA?style=for-the-badge&logo=anthropic&logoColor=white)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.style=for-the-badge)](LICENSE)

A custom **Model Context Protocol (MCP)** server implementation built with Python and `FastMCP` that integrates real-time National Weather Service (NWS) API weather alerts and location forecasts into AI assistants and LLM workflows.

---

## ✨ Capabilities & Tools

This MCP server exposes two main async tools for AI models:

| Tool | Parameters | Description |
| :--- | :--- | :--- |
| 🚨 `get_alerts` | `state: str` | Retrieves active NWS severe weather alerts for a specified US state code (e.g. `CA`, `TX`, `NY`). |
| 🌡️ `get_forecast` | `latitude: float`, `longitude: float` | Fetches multi-period weather forecasts for specific geographic coordinates. |

---

## 🚀 Quickstart & Setup

### Prerequisites
- Python `3.13+`
- [`uv`](https://github.com/astral-sh/uv) (recommended) or standard `pip`

### Installation

```bash
# Clone the repository
git clone https://github.com/Sathyabalan6/mcp_server.git
cd mcp_server

# Install dependencies using uv
uv sync
```

### Running Directly

```bash
# Run server using FastMCP stdio transport
uv run weather.py
```

---

## 🛠️ Integration with MCP Clients (Claude Desktop / Antigravity / Cursor)

Add the server to your `mcp_config.json` file:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp_server",
        "run",
        "weather.py"
      ]
    }
  }
}
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
