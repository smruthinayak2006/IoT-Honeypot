# Day 27 Notes

## Topic
Security Hardening


## Problem

Plain text passwords are unsafe for authentication systems.


## Solution

Implemented password hashing using bcrypt.


## Implemented

- bcrypt password hashing
- Secure password verification
- Removed plaintext admin password
- Improved authentication security


## Why Hash Passwords?

Hashing prevents exposure of original passwords even if stored credentials leak.


## Files Modified

honeypot/auth.py

honeypot/config.py

.env


## Result

Dashboard authentication now uses secure password verification.