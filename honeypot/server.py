"""
Fake IoT Telnet Server
"""

import socket

from logger import save_log
from detector import detect_bruteforce
from database import save_attack


HOST = "0.0.0.0"
PORT = 2323


# -----------------------------
# SAFE RECEIVE FUNCTION
# -----------------------------
def receive_input(client):

    data = ""

    try:

        while True:

            character = client.recv(1).decode(errors="ignore")

            if not character:
                break

            if character == "\n":
                break

            data += character


    except (ConnectionResetError, ConnectionAbortedError):

        # client disconnected suddenly
        pass


    return data.strip()


# -----------------------------
# SAFE SEND FUNCTION (FIX)
# -----------------------------
def safe_send(client, message):

    try:

        client.send(message)

    except (
        BrokenPipeError,
        ConnectionResetError,
        ConnectionAbortedError
    ):
        # client already disconnected
        pass


# -----------------------------
# MAIN SERVER
# -----------------------------
def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind(
        (HOST, PORT)
    )

    server.listen(5)

    server.settimeout(1)

    print("[+] IoT Honeypot Running")
    print(f"[+] Listening on {PORT}")

    while True:

        try:
            client, address = server.accept()

        except socket.timeout:
            continue

        attacker_ip = address[0]

        print(f"[!] Connection from {attacker_ip}")

        # -----------------------------
        # INTERACTION FLOW
        # -----------------------------

        safe_send(client, b"Fake IoT Camera\n")

        safe_send(client, b"Username: ")
        username = receive_input(client)

        safe_send(client, b"Password: ")
        password = receive_input(client)

        save_log(attacker_ip, username, password)
        save_attack(attacker_ip, username, password)
        detect_bruteforce(attacker_ip)

        print("[+] Attack saved")

        safe_send(client, b"Login failed\n")

        client.close()