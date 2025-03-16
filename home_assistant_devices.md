# Home Assistant Devices

## Living Room
### Lights
- `light.living_room_lights` - LR Ceiling Light
- `light.living_room_lights_2` - Living Room Lights
- `light.living_room_dining_lights` - Dining Lights
- `light.living_room_wall_light_north` - DR North Light
- `light.living_room_wall_light_south_west` - DR West Light

### Media
- `media_player.living_room` - Living Room
- `remote.living_room` - Living Room Remote

## Kitchen
### Lights
- `light.kitchen_lights` - Kitchen Lights (Main)
- `light.central_light` - Kitchen Central Light
- `light.side_light` - Kitchen Side Light
- `light.sink_light` - Kitchen Sink Light

### Automation
- `automation.kitchen_motion_detected` - Kitchen Motion Detection

## Master Bedroom
### Lights
- `light.master_bedroom_lights` - Master Bedroom Lights (Main)
- `light.master_bedroom_ceiling_light` - MB Ceiling Light
- `light.master_bedroom_bed_light_east` - MB East Light
- `light.master_bedroom_bed_light_west` - MB West Light

## Guest Bedroom
### Lights
- `light.guest_bedroom_lights` - Guest Bedroom Lights

## Exterior
### Lights
- `light.exterior_lights` - Exterior Lights

## Device Capabilities
### Lights
Most lights support:
- On/Off control
- Brightness adjustment (0-255)
- RGB color control (where applicable)
- Transition timing for smooth changes

### Media Players
Support:
- Play/Pause
- Volume control
- Media selection

### Automations
- Can be enabled/disabled
- Triggered by specific events (e.g., motion detection)

## Notes
- Entity IDs are shown in `code format` for precise identification
- Friendly names are shown after the hyphen
- Some devices may have multiple control points (e.g., group lights vs individual lights)
- Kitchen and Living Room have motion-based automation capabilities 