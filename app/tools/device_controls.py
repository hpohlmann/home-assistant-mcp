from typing import Dict, Any, Optional
from mcp.server.fastmcp import FastMCP
from ..api.home_assistant import make_ha_request, get_all_entities
from ..config import HOME_ASSISTANT_TOKEN
from ..utils.search import search_entities_by_keywords, format_entity_results

# Tools need to be registered with a FastMCP instance
# This will be initialized in the main.py file and passed here
mcp = None

def init_tools(fastmcp_instance: FastMCP):
    """Initialize the tools with a FastMCP instance."""
    global mcp
    mcp = fastmcp_instance
    
    # Register tools with the FastMCP instance
    fastmcp_instance.tool()(control_device)
    fastmcp_instance.tool()(search_entities)
    fastmcp_instance.tool()(set_light_color)

async def control_device(entity_id: str, state: str) -> str:
    """Control a Home Assistant entity by turning it on or off.
    
    Args:
        entity_id: The Home Assistant entity ID to control (format: domain.entity)
        state: The desired state ('on' or 'off')
    """
    # Basic validation
    if not entity_id or "." not in entity_id:
        return f"Invalid entity ID format: {entity_id}. Must be in format: domain.entity"
    
    state = state.lower()
    if state not in ["on", "off"]:
        return f"Invalid state: {state}. Must be 'on' or 'off'"
    
    # Check token
    if not HOME_ASSISTANT_TOKEN:
        return "Home Assistant token not configured. Set HOME_ASSISTANT_TOKEN environment variable."
    
    # Get domain from entity_id
    domain = entity_id.split(".")[0]
    service = "turn_on" if state == "on" else "turn_off"
    
    # Call the HA API
    result = await make_ha_request(domain, service, entity_id)
    
    if result["success"]:
        return f"Successfully turned {state} {entity_id}"
    else:
        return f"Failed to control {entity_id}: {result.get('error', 'Unknown error')}"

async def set_light_color(entity_id: str, red: int, green: int, blue: int) -> str:
    """Set the color of a light entity.
    
    Args:
        entity_id: The Home Assistant entity ID (must be a light)
        red: Red component (0-255)
        green: Green component (0-255)
        blue: Blue component (0-255)
    """
    # Basic validation
    if not entity_id or not entity_id.startswith("light."):
        return f"Invalid entity ID: {entity_id}. Must be a light entity (format: light.entity_id)"
    
    # Validate RGB values
    for color, name, value in [("red", "Red", red), ("green", "Green", green), ("blue", "Blue", blue)]:
        if not isinstance(value, int) or not 0 <= value <= 255:
            return f"{name} value must be an integer between 0 and 255"
    
    # Check token
    if not HOME_ASSISTANT_TOKEN:
        return "Home Assistant token not configured. Set HOME_ASSISTANT_TOKEN environment variable."
    
    # Call the HA API with RGB color data
    result = await make_ha_request("light", "turn_on", entity_id, {"rgb_color": [red, green, blue]})
    
    if result["success"]:
        return f"Successfully set {entity_id} to RGB({red},{green},{blue})"
    else:
        return f"Failed to set color for {entity_id}: {result.get('error', 'Unknown error')}"

async def search_entities(description: str) -> str:
    """Search for Home Assistant entities matching a natural language description.
    
    Args:
        description: Natural language description of the entity (e.g., "office light", "kitchen fan")
    
    Returns:
        A list of matching entity IDs with their friendly names, or an error message
    """
    # Check token
    if not HOME_ASSISTANT_TOKEN:
        return "Home Assistant token not configured. Set HOME_ASSISTANT_TOKEN environment variable."
    
    # Get all entities
    entities = await get_all_entities()
    if not entities:
        return "Failed to retrieve entities from Home Assistant."
    
    # Search and format results
    matches = search_entities_by_keywords(entities, description)
    return format_entity_results(matches) 