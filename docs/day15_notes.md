# Day 15 Notes

## Topic
IoT Device Simulation Layer


## Implemented

- Created fake IoT device profile
- Added realistic IoT camera identity
- Added device banner information
- Integrated device details with Telnet honeypot


## Fake Device Details

Device Name:
SmartCam X100

Device Type:
Security Camera

Firmware:
v1.0.3

Service:
Telnet


## Why Device Simulation?

A honeypot pretends to be a real vulnerable device to attract attackers.

Instead of attacking real systems, attackers interact with the fake device.

The honeypot records:
- IP address
- Tried usernames
- Tried passwords
- Attack behaviour


## Files Added

honeypot/device.py

Contains:
- Device name
- Firmware version
- Service information


## Files Updated

honeypot/server.py

Added:
- IoT device banner
- Device profile integration


## Learned

- IoT device fingerprinting
- Banner simulation
- Telnet based IoT attacks
- Honeypot deception technique


## Result

Successfully created a fake IoT security camera environment.

The honeypot now:
- Displays realistic IoT device information
- Accepts login attempts
- Captures attacker credentials
- Sends data to the existing monitoring system