"""
Attack Analysis Engine
"""

import sqlite3



DATABASE_PATH = "database/attacks.db"



def total_attacks():


    connection = sqlite3.connect(
        DATABASE_PATH
    )


    cursor = connection.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM attacks"
    )


    result = cursor.fetchone()


    connection.close()


    print(
        f"Total Attacks: {result[0]}"
    )



def common_usernames():


    connection = sqlite3.connect(
        DATABASE_PATH
    )


    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT username, COUNT(username)

        FROM attacks

        GROUP BY username

        ORDER BY COUNT(username) DESC
        """
    )


    results = cursor.fetchall()


    print("\nMost Tried Usernames:")


    for row in results:


        print(
            f"{row[0]} : {row[1]} attempts"
        )


    connection.close()



def common_passwords():


    connection = sqlite3.connect(
        DATABASE_PATH
    )


    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT password, COUNT(password)

        FROM attacks

        GROUP BY password

        ORDER BY COUNT(password) DESC
        """
    )


    results = cursor.fetchall()


    print("\nMost Tried Passwords:")


    for row in results:


        print(
            f"{row[0]} : {row[1]} attempts"
        )


    connection.close()