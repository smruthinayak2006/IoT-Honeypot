"""
Handles attack logging
"""

from datetime import datetime


def save_log(ip, username, password):

    time = datetime.now()


    with open(
        "logs/attack_logs.txt",
        "a"
    ) as file:


        file.write(
            "====================\n"
        )


        file.write(
            f"Time: {time}\n"
        )


        file.write(
            f"IP Address: {ip}\n"
        )


        file.write(
            f"Username: {username}\n"
        )


        file.write(
            f"Password: {password}\n"
        )


        file.write(
            "====================\n\n"
        )