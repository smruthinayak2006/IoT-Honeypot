"""
Central Configuration Management
"""

import os

from dotenv import load_dotenv


load_dotenv()


HOST = os.getenv(
    "HONEYPOT_HOST",
    "0.0.0.0"
)


PORT = int(
    os.getenv(
        "HONEYPOT_PORT",
        2323
    )
)


DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "database/attacks.db"
)


BRUTE_FORCE_LIMIT = int(
    os.getenv(
        "BRUTE_FORCE_LIMIT",
        5
    )
)


SECURITY_LOG_PATH = os.getenv(
    "SECURITY_LOG_PATH",
    "logs/security.log"
)


ATTACK_LOG_PATH = os.getenv(
    "ATTACK_LOG_PATH",
    "logs/attack_logs.txt"
)

REPORT_FOLDER = os.getenv(
    "REPORT_FOLDER",
    "reports"
)

ADMIN_USERNAME = os.getenv(
    "ADMIN_USERNAME",
    "admin"
)

ADMIN_PASSWORD_HASH = os.getenv(
    "ADMIN_PASSWORD_HASH"
)