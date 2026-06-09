"""
IoT Honeypot

Day 5:
Saving attack logs
"""

import socket
from datetime import datetime


HOST = "0.0.0.0"
PORT = 2323


def receive_input(client):

    data = ""

    while True:

        character = client.recv(1).decode()

        if character == "\n":
            break

        data += character

    return data.strip()



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



server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


server.bind(
    (HOST, PORT)
)


server.listen(5)


print("[+] IoT Honeypot Running")
print(f"[+] Listening on {PORT}")



while True:


    client, address = server.accept()


    attacker_ip = address[0]


    print(
        f"[!] Connection from {attacker_ip}"
    )


    client.send(
        b"Fake IoT Camera\n"
    )


    client.send(
        b"Username: "
    )


    username = receive_input(
        client
    )


    client.send(
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


    print(
        "[+] Attack saved"
    )


    client.send(
        b"Login failed\n"
    )


    client.close()