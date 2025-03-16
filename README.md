# Home Assistant MCP

A Model Context Protocol (MCP) integration for controlling Home Assistant devices using AI assistants.

## Overview

This MCP allows AI assistants to control your Home Assistant devices. It provides tools to:

1. Search for entities in your Home Assistant instance
2. Control devices (turn them on/off)
3. Control light colors and brightness

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
      "args": [
        "--directory",
        "/path/to/your/home-assistant-mcp",
        "run",
        "main.py"
      ],
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
- Control light colors: "Set my living room lights to red"
- Adjust brightness: "Set my dining room lights to blue at 50% brightness"

### Light Control Features

The MCP now supports advanced light control capabilities:

1. **Color Control**: Set any RGB color for compatible lights
   - Specify colors using RGB values (0-255 for each component)
   - Example: `set_device_color("light.living_room", 255, 0, 0)` for red

2. **Brightness Control**: Adjust light brightness
   - Optional brightness parameter (0-255)
   - Can be combined with color changes
   - Example: `set_device_color("light.dining_room", 0, 0, 255, brightness=128)` for medium-bright blue

## Troubleshooting

- If you get authentication errors, verify your token is correct and has not expired
- Check that your Home Assistant instance is reachable at the configured URL
- For color control issues:
  - Verify that your light entity supports RGB color control
  - Check that the light is turned on before attempting to change colors

## Future Capabilities

### Dynamic Entity Exposure

The current implementation requires a two-step process to control devices:

1. Search for entities using natural language
2. Control the entity using its specific entity_id

A planned enhancement is to create a more dynamic way to expose entities to the control devices tool, allowing the AI to:

- Directly control devices through more natural commands (e.g., "turn off the kitchen lights")
- Cache frequently used entities for faster access
- Support more complex operations like adjusting brightness, temperature, or other attributes
- Handle entity groups and scenes more intuitively

This would significantly reduce the time to action and create a more seamless user experience when controlling Home Assistant devices through an AI assistant.