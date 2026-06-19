"""
Database Operations
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


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS blocked_ips(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT UNIQUE,
        timestamp TEXT
        )
        """
    )


    conn.commit()
    conn.close()



def save_attack(ip, username, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attacks
        (ip_address,username,password,timestamp)

        VALUES(?,?,?,?)
        """,
        (
            ip,
            username,
            password,
            datetime.now()
        )
    )

    conn.commit()
    conn.close()



def save_alert(ip, message):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO alerts
        (ip_address,message,timestamp)

        VALUES(?,?,?)
        """,
        (
            ip,
            message,
            datetime.now()
        )
    )


    conn.commit()
    conn.close()



def block_ip(ip):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT OR IGNORE INTO blocked_ips
        (ip_address,timestamp)

        VALUES(?,?)
        """,
        (
            ip,
            datetime.now()
        )
    )


    conn.commit()
    conn.close()



def is_blocked(ip):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT * FROM blocked_ips
        WHERE ip_address=?
        """,
        (ip,)
    )


    result = cursor.fetchone()

    conn.close()

    return result is not None



def unblock_ip(ip):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM blocked_ips
        WHERE ip_address=?
        """,
        (ip,)
    )


    conn.commit()
    conn.close()