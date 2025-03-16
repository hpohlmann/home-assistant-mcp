# Home Assistant MCP

A Model Context Protocol (MCP) integration for controlling Home Assistant devices using AI assistants.

## Overview

This MCP allows AI assistants to control your Home Assistant devices. It provides tools to:

1. Search for entities in your Home Assistant instance
2. Control devices (turn them on/off)

## Prerequisites

- Python 3.11 or higher
- Home Assistant instance running and accessible via API
- Home Assistant Long-Lived Access Token

## Installation

1. Clone this repository
2. Set up a Python environment:

```bash
cd home-assistant
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -U pip
pip install uv
uv pip install -e .
```

## Configuration

### Get a Home Assistant Long-Lived Access Token

1. Go to your Home Assistant instance
2. Navigate to your profile (click on your username in the sidebar)
3. Scroll down to "Long-Lived Access Tokens"
4. Create a new token with a descriptive name like "MCP Integration"
5. Copy the token (you'll only see it once)

### Set up in Cursor AI

Add the following configuration to your MCP configuration in Cursor:

```json
{
  "mcpServers": {
    "home_assistant": {
      "command": "uv",
      "args": ["--directory", "/path/to/your/home-assistant", "run", "main.py"],
      "env": {
        "HOME_ASSISTANT_TOKEN": "your_home_assistant_token_here"
      },
      "inheritEnv": true
    }
  }
}
```

Replace:

- `/path/to/your/home-assistant` with the actual path to this directory
- `your_home_assistant_token_here` with your Home Assistant Long-Lived Access Token

### Home Assistant URL Configuration

By default, the MCP tries to connect to Home Assistant at `http://homeassistant.local:8123`.

If your Home Assistant is at a different URL, you can modify the `HA_URL` variable in `app/config.py`.

## Usage

Once configured, you can use Cursor AI to control your Home Assistant devices:

- Search for devices: "Find my living room lights"
- Control devices: "Turn on the kitchen light"

## Troubleshooting

- If you get authentication errors, verify your token is correct and has not expired
- Check that your Home Assistant instance is reachable at the configured URL
