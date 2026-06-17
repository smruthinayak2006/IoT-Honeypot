# Day 13 Notes

## Topic
Real-Time Alert System

---

## Implemented

- Created security alert storage system
- Added alerts table in SQLite database
- Integrated brute force detection with alert generation
- Stored suspicious activity permanently

---

## Why Alert System is Needed

Earlier the honeypot only printed alerts:

[ALERT] Possible brute force detected

The alert disappeared once the program stopped.

Now alerts are stored permanently in the database so previous attacks can be reviewed and analyzed.

---

## Alert Workflow

Attacker
    |
    v

Fake IoT Camera Honeypot
    |
    v

Login Attempt Captured
    |
    v

Brute Force Detector
    |
    v

Security Alert Generated
    |
    v

SQLite Alert Database


---

## Database Changes

Created new table:

alerts

Stores:

- Alert ID
- Attacker IP address
- Alert message
- Timestamp

---

## Brute Force Detection Logic

The honeypot tracks repeated login attempts from an IP address.

Example:

127.0.0.1 : 5 attempts

If attempts cross the limit:

Possible brute force attack detected

alert is generated.

---

## Files Modified

honeypot/database.py

Added:
- alerts table creation
- save_alert() function


honeypot/detector.py

Added:
- alert generation
- database alert storage


tests/view_alerts.py

Added:
- View stored security alerts

---

## Concepts Learned

- Security event monitoring
- Alert generation
- Persistent alert storage
- Attack history tracking
- Basic SIEM workflow

---

## Result

Successfully created a real-time alert system where brute force attacks are detected and stored for future security analysis.