# Day 23 Notes

## Topic
Environment Configuration and Secret Protection


## Problem

Hardcoded configuration values make applications difficult to manage and unsafe for deployment.


Examples:

- Ports
- Paths
- Security settings


## Solution

Added environment based configuration.


## Workflow

.env file

     |

config.py

     |

Application modules


## Implemented

- Created environment variables
- Integrated python-dotenv
- Protected .env using gitignore
- Centralized application settings


## Advantages

- Better security
- Easier deployment
- Cleaner configuration management


## Files Updated

.env

honeypot/config.py

.gitignore


## Result

The honeypot now uses production-style configuration management.