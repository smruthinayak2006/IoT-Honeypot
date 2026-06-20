"""
Fake IoT Telnet Server
"""

import socket

from logger import save_log
from detector import detect_bruteforce
from database import save_attack, is_blocked
from device import get_device_info
from config import HOST, PORT
from security_logger import log_info, log_warning

HOST = "0.0.0.0"
PORT = 2323


def safe_send(client, message):

    try:
        client.send(message)

    except (
        ConnectionResetError,
        ConnectionAbortedError,
        BrokenPipeError
    ):
        pass



def receive_input(client):

    data = ""

    try:

        while True:

            character = client.recv(
                1
            ).decode(
                errors="ignore"
            )

            if not character:
                break

            if character == "\n":
                break

            data += character


    except (
        ConnectionResetError,
        ConnectionAbortedError
    ):

        pass


    return data.strip()



def start_server():


    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )


    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )


    server.bind(
        (
            HOST,
            PORT
        )
    )


    server.listen(5)


    server.settimeout(1)


    print("[+] IoT Honeypot Running")
    log_info(
        "IoT Honeypot server started"
    )
    print(f"[+] Listening on {PORT}")



    while True:


        try:

            client, address = server.accept()


        except socket.timeout:

            continue



        attacker_ip = address[0]



        if is_blocked(
            attacker_ip
        ):


            print(
                "[BLOCKED]",
                attacker_ip
            )
            log_warning(
                f"Blocked connection from {attacker_ip}"
            )


            safe_send(
                client,
                b"Access blocked\r\n"
            )


            client.close()


            continue



        print(
            f"[!] Connection from {attacker_ip}"
        )
        log_warning(
            f"Connection attempt from {attacker_ip}"
        )


        device = get_device_info()



        banner = (

            "\r\n"
            "====================================\r\n"
            "        IoT DEVICE LOGIN\r\n"
            "====================================\r\n"
            f"Device Name : {device['name']}\r\n"
            f"Type        : {device['type']}\r\n"
            f"Firmware    : {device['firmware']}\r\n"
            f"Service     : {device['service']}\r\n"
            "====================================\r\n"
            "\r\n"
        )



        safe_send(
            client,
            banner.encode()
        )


        safe_send(
            client,
            b"Username: "
        )


        username = receive_input(
            client
        )


        safe_send(
            client,
            b"Password: "
        )


        password = receive_input(
            client
        )



        save_log(
            attacker_ip,
            username,
            password
        )



        save_attack(
            attacker_ip,
            username,
            password
        )



        detect_bruteforce(
            attacker_ip
        )



        print(
            "[+] Attack saved"
        )
        log_info(
            f"Attack saved from {attacker_ip}"
        )


        safe_send(
            client,
            b"\r\nAccess Denied\r\n"
        )


        client.close()