"""
Attack Analysis Engine
"""

import sqlite3


DATABASE = "database/attacks.db"


def total_attacks():

    connection = sqlite3.connect(
        DATABASE
    )

    cursor = connection.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM attacks"
    )


    result = cursor.fetchone()


    print(
        f"Total Attacks: {result[0]}"
    )


    connection.close()



def top_usernames():

    connection = sqlite3.connect(
        DATABASE
    )

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT username, COUNT(*)

        FROM attacks

        GROUP BY username

        ORDER BY COUNT(*) DESC
        """
    )


    results = cursor.fetchall()


    print(
        "\nTop Usernames:"
    )


    for username, count in results:

        print(
            f"{username}: {count}"
        )


    connection.close()



def top_passwords():

    connection = sqlite3.connect(
        DATABASE
    )


    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT password, COUNT(*)

        FROM attacks

        GROUP BY password

        ORDER BY COUNT(*) DESC
        """
    )


    results = cursor.fetchall()


    print(
        "\nTop Passwords:"
    )


    for password, count in results:

        print(
            f"{password}: {count}"
        )


    connection.close()