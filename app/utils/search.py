import re
from typing import List, Dict, Any

def search_entities_by_keywords(entities: List[Dict[str, Any]], description: str) -> List[Dict[str, Any]]:
    """Search for entities matching a natural language description.
    
    Args:
        entities: List of entity dictionaries from Home Assistant
        description: Natural language description of the entity
        
    Returns:
        A list of matching entities sorted by relevance score
    """
    # Break description into keywords
    keywords = re.findall(r'\w+', description.lower())
    
    # Search for matching entities
    matches = []
    for entity in entities:
        entity_id = entity.get("entity_id", "").lower()
        friendly_name = entity.get("attributes", {}).get("friendly_name", "").lower()
        
        # Check if any keyword matches the entity_id or friendly_name
        score = 0
        for keyword in keywords:
            if keyword in entity_id or keyword in friendly_name:
                score += 1
        
        if score > 0:
            matches.append({
                "entity_id": entity.get("entity_id"),
                "friendly_name": entity.get("attributes", {}).get("friendly_name", ""),
                "score": score
            })
    
    # Sort matches by score (descending)
    return sorted(matches, key=lambda x: x["score"], reverse=True)

def format_entity_results(matches: List[Dict[str, Any]], limit: int = 5) -> str:
    """Format entity search results into a readable string.
    
    Args:
        matches: List of matching entities with scores
        limit: Maximum number of results to include
        
    Returns:
        Formatted string with entity results
    """
    if matches:
        result = "Found matching entities:\n"
        for match in matches[:limit]:
            result += f"- {match['entity_id']} ({match['friendly_name']})\n"
        return result
    else:
        return "No matching entities found." 