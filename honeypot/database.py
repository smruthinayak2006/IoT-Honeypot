"""
SQLite database handler
"""

import sqlite3
from datetime import datetime


DATABASE = "database/attacks.db"


def create_table():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attacks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            username TEXT,
            password TEXT,
            timestamp TEXT
        )
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS alerts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            message TEXT,
            timestamp TEXT
        )
        """
    )


    conn.commit()

    conn.close()



def save_attack(
        ip_address,
        username,
        password
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


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
        ip_address,
        username,
        password,
        str(datetime.now())
        )
    )


    conn.commit()

    conn.close()



def save_alert(
        ip_address,
        message
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO alerts
        (
        ip_address,
        message,
        timestamp
        )

        VALUES (?, ?, ?)
        """,

        (
        ip_address,
        message,
        str(datetime.now())
        )
    )


    conn.commit()

    conn.close()