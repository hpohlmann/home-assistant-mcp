import os

# Home Assistant API configuration
HA_URL = "http://homeassistant.local:8123"
HOME_ASSISTANT_TOKEN = os.environ.get("HOME_ASSISTANT_TOKEN")
USER_AGENT = "home-assistant-mcp/1.0"

def validate_config():
    """Validate that the required configuration is present."""
    if not HOME_ASSISTANT_TOKEN:
        raise ValueError("HOME_ASSISTANT_TOKEN environment variable is not set")
    return True 