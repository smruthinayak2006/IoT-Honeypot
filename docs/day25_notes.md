# Day 25 Notes

## Topic
Threat Intelligence Engine


## Problem

Raw attack data does not explain attacker severity.


## Solution

Created a risk scoring engine that analyzes attacker behavior.


## Implemented

- IP based analysis
- Attack counting
- Risk classification
- Threat reasoning


## Risk Levels

LOW:
Few attempts

MEDIUM:
Suspicious activity

HIGH:
Repeated attacks

CRITICAL:
Blocked attacker


## Files Added

honeypot/threat_intel.py

tests/test_threat.py


## Result

The honeypot can classify attacker risk automatically.