# Day 21 Notes

## Topic
Professional Security Logging System


## Implemented

- Added centralized security logger
- Replaced simple console messages with structured logs
- Added log severity levels


## Log Levels Used

INFO:

Normal application activity


WARNING:

Suspicious connection attempts


CRITICAL:

Confirmed security threats


## Log File

logs/security.log


Stores:

- Timestamp
- Severity
- Security event


## Benefits

- Easier incident investigation
- Better monitoring
- Maintains event history
- Similar to SOC logging systems


## Concepts Learned

- Python logging module
- Security event tracking
- Log severity classification