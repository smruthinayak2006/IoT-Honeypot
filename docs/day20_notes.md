# Day 20 Notes

## Topic
Configuration Management


## Implemented

- Added centralized configuration file
- Removed hardcoded values
- Added configurable security settings


## Configuration File

Created:

honeypot/config.py


Stores:

- Server IP
- Server port
- Database path
- Brute force limit
- Report folder


## Advantages

- Easier maintenance
- Cleaner code structure
- Faster deployment changes
- Better scalability


## Example

Before:

Change port manually in server code


After:

Update PORT value in config.py


## Concepts Learned

- Configuration management
- Code maintainability
- Production project structure