"""
Database handling for IoT Honeypot
"""

import sqlite3
from datetime import datetime
from utils import clean_input

def create_database():

    connection = sqlite3.connect(
        "database/attacks.db"
    )


    cursor = connection.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attacks (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ip_address TEXT,

            username TEXT,

            password TEXT,

            timestamp TEXT

        )
        """
    )


    connection.commit()


    connection.close()



def save_attack(
        ip,
        username,
        password
):


    connection = sqlite3.connect(
        "database/attacks.db"
    )


    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO attacks
        (
        ip_address,
        username,
        password,
        timestamp
        )

        VALUES (?, ?, ?, ?)
        """,

        (
        ip,
        clean_input(username),
        clean_input(password),
        str(datetime.now())
        )
    )


    connection.commit()


    connection.close()