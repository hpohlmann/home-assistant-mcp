# Home Assistant Curl Tests

This directory contains curl-based test scripts for interacting with the Home Assistant API directly. These scripts are useful for testing and understanding the API before implementing more complex integrations.

## Prerequisites

- `curl` installed on your system
- `jq` installed for JSON formatting (optional but recommended)
- Home Assistant Long-Lived Access Token
- Home Assistant running and accessible

## Configuration

1. Set your Home Assistant token as an environment variable:
```bash
export HOME_ASSISTANT_TOKEN='your_long_lived_access_token'
```

2. (Optional) If your Home Assistant is not at the default URL (`http://homeassistant.local:8123`), modify the `HA_URL` variable in the test scripts.

## Available Tests

### test_lights.sh

Tests basic light control operations:
- Lists all available entities
- Gets the current state of a light
- Turns the light on
- Turns the light off
- Verifies state changes

Usage:
```bash
# Make the script executable
chmod +x tests/test_lights.sh

# Run the test
./tests/test_lights.sh
```

## API Endpoints Used

The test scripts demonstrate the following Home Assistant API endpoints:

1. Get States: `GET /api/states`
   - Lists all entity states

2. Get Entity State: `GET /api/states/{entity_id}`
   - Gets the current state of a specific entity

3. Turn Light On: `POST /api/services/light/turn_on`
   - Payload: `{"entity_id": "light.example"}`

4. Turn Light Off: `POST /api/services/light/turn_off`
   - Payload: `{"entity_id": "light.example"}`

## Error Handling

The scripts include basic error handling:
- Checks for the presence of the required access token
- Uses silent curl mode (-s) but pipes through jq for readable output
- Includes color-coded output for better readability

## Next Steps

After understanding these basic API interactions, you can:
1. Add more complex light controls (brightness, color, etc.)
2. Add tests for other device types
3. Implement error handling and retries
4. Add support for scenes and groups 