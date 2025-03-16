#!/bin/bash

# Configuration
HA_URL="https://homeassistant.austrheim.ca7.fm"
# Token should be set in environment variable
if [ -z "$HOME_ASSISTANT_TOKEN" ]; then
    echo "Error: HOME_ASSISTANT_TOKEN environment variable is not set"
    echo "Please set it with: export HOME_ASSISTANT_TOKEN='your_long_lived_access_token'"
    exit 1
fi

# Headers for all requests
HEADERS="Authorization: Bearer ${HOME_ASSISTANT_TOKEN// /}"  # Remove any spaces from token
CONTENT_TYPE="Content-Type: application/json"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "Home Assistant API Test Script"
echo "=============================="
echo "Using Home Assistant URL: $HA_URL"
echo "Authorization Token: ${HOME_ASSISTANT_TOKEN:0:20}..."

# Function to get current state of an entity
get_entity_state() {
    local entity_id=$1
    echo -e "\n${GREEN}Getting state for: $entity_id${NC}"
    
    echo "Raw response:"
    curl -v -X GET \
        -H "$HEADERS" \
        "$HA_URL/api/states/$entity_id"
    echo
}

# Function to turn a light on
turn_light_on() {
    local entity_id=$1
    echo -e "\n${GREEN}Turning ON: $entity_id${NC}"
    
    echo "Raw response:"
    curl -v -X POST \
        -H "$HEADERS" \
        -H "$CONTENT_TYPE" \
        -d "{\"entity_id\": \"$entity_id\"}" \
        "$HA_URL/api/services/light/turn_on"
    echo
}

# Function to turn a light off
turn_light_off() {
    local entity_id=$1
    echo -e "\n${GREEN}Turning OFF: $entity_id${NC}"
    
    echo "Raw response:"
    curl -v -X POST \
        -H "$HEADERS" \
        -H "$CONTENT_TYPE" \
        -d "{\"entity_id\": \"$entity_id\"}" \
        "$HA_URL/api/services/light/turn_off"
    echo
}

# Function to set light color
set_light_color() {
    local entity_id=$1
    local r=$2
    local g=$3
    local b=$4
    echo -e "\n${GREEN}Setting color for: $entity_id to RGB($r,$g,$b)${NC}"
    
    echo "Raw response:"
    curl -v -X POST \
        -H "$HEADERS" \
        -H "$CONTENT_TYPE" \
        -d "{
            \"entity_id\": \"$entity_id\",
            \"rgb_color\": [$r, $g, $b],
            \"brightness\": 255
        }" \
        "$HA_URL/api/services/light/turn_on"
    echo
}

# Function to list all entities
list_entities() {
    echo -e "\n${GREEN}Listing all entities:${NC}"
    
    echo "Raw response:"
    curl -v -X GET \
        -H "$HEADERS" \
        "$HA_URL/api/states"
    echo
}

# Test sequence
echo "Starting test sequence..."

# 1. Test connection
echo -e "\n${GREEN}Testing connection to Home Assistant${NC}"
curl -v -X GET \
    -H "$HEADERS" \
    "$HA_URL/api/"
echo

# 2. List all entities
list_entities

# 3. Test with living room lights
LIGHT_ENTITY="light.living_room_lights"

# 4. Get initial state
get_entity_state "$LIGHT_ENTITY"

# 5. Turn light on
turn_light_on "$LIGHT_ENTITY"

# 6. Wait 2 seconds
echo -e "\n${GREEN}Waiting 2 seconds...${NC}"
sleep 2

# 7. Get state after turning on
get_entity_state "$LIGHT_ENTITY"

# 8. Turn light off
turn_light_off "$LIGHT_ENTITY"

# 9. Wait 2 seconds
echo -e "\n${GREEN}Waiting 2 seconds...${NC}"
sleep 2

# 10. Get final state
get_entity_state "$LIGHT_ENTITY"

# 11. Set light to blue
echo -e "\n${GREEN}Testing color change to blue...${NC}"
turn_light_on "$LIGHT_ENTITY"
sleep 1
set_light_color "$LIGHT_ENTITY" 0 0 255
sleep 2
get_entity_state "$LIGHT_ENTITY"

echo -e "\n${GREEN}Test sequence completed!${NC}" 