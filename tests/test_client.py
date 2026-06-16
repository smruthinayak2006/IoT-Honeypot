"""
Fake attacker client

This script simulates multiple attackers
trying different usernames and passwords
against our IoT honeypot.
"""

import socket
import time


TARGET_IP = "127.0.0.1"
TARGET_PORT = 2323


usernames = [
    "admin",
    "root",
    "camera"
]


passwords = [
    "123456",
    "admin123",
    "password",
    "camera123"
]


for username in usernames:

    for password in passwords:


        try:

            client = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )


            client.connect(
                (
                    TARGET_IP,
                    TARGET_PORT
                )
            )


            # Receive fake camera banner
            client.recv(
                1024
            )


            # Receive username prompt
            client.recv(
                1024
            )


            # Send fake username attempt
            client.send(
                (
                    username + "\n"
                ).encode()
            )


            # Receive password prompt
            client.recv(
                1024
            )


            # Send fake password attempt
            client.send(
                (
                    password + "\n"
                ).encode()
            )


            # Receive login result
            response = client.recv(
                1024
            ).decode(
                errors="ignore"
            )


            print(
                "\n========== ATTACK ATTEMPT =========="
            )


            print(
                "Username:",
                username
            )


            print(
                "Password:",
                password
            )


            print(
                "Server Response:",
                response.strip()
            )


            client.close()


            time.sleep(
                0.5
            )


        except Exception as error:


            print(
                "Attack failed:",
                error
            )