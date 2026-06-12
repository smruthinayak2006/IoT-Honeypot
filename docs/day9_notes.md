Day 9 Notes

Learned:

- Threat intelligence basics
- SQL SELECT
- COUNT
- GROUP BY
- ORDER BY

Analyzer Features:

1. Total attack count

2. Most targeted usernames

3. Most common passwords


Purpose:

Convert raw attack data into useful security information.

Additional Debugging:

Issue:
Analyzer showed duplicate usernames.

Cause:
Raw Telnet input contained hidden terminal characters.

Examples:
- Backspace characters
- Escape sequences from arrow keys

Fix:
Created input sanitization module.

Added:
utils.py

Purpose:
Clean attacker input before database storage.

Learning:
Security logs must be normalized before analysis.