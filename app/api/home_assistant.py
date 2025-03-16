from typing import Dict, Any, List, Optional
import httpx
from ..config import HA_URL, HOME_ASSISTANT_TOKEN, USER_AGENT

async def make_ha_request(domain: str, service: str, entity_id: str, additional_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Make a request to the Home Assistant API with proper error handling."""
    url = f"{HA_URL}/api/services/{domain}/{service}"
    
    headers = {
        "Authorization": f"Bearer {HOME_ASSISTANT_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT
    }
    
    # Prepare the payload
    payload = {"entity_id": entity_id}
    if additional_data:
        payload.update(additional_data)
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload, timeout=10.0)
            response.raise_for_status()
            return {"success": True, "status_code": response.status_code}
        except Exception as e:
            return {"success": False, "error": str(e)}

async def get_all_entities() -> List[Dict[str, Any]]:
    """Fetch all entities from Home Assistant."""
    url = f"{HA_URL}/api/states"
    
    headers = {
        "Authorization": f"Bearer {HOME_ASSISTANT_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=10.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return [] 