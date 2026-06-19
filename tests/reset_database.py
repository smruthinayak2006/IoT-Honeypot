"""
Reset Honeypot Database
"""

import sqlite3
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "attacks.db"
)


print(
    "Cleaning:",
    DATABASE
)


connection = sqlite3.connect(
    DATABASE
)


cursor = connection.cursor()


tables = [
    "attacks",
    "alerts",
    "blocked_ips"
]


for table in tables:

    cursor.execute(
        f"DELETE FROM {table}"
    )


cursor.execute(
    """
    DELETE FROM sqlite_sequence
    WHERE name IN 
    ('attacks','alerts','blocked_ips')
    """
)


connection.commit()


connection.close()


print(
    "[+] Database reset successfully"
)