"""
IoT Honeypot

Day 4:
Fake Telnet login capture
"""

import socket


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


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


server.bind((HOST, PORT))


server.listen(5)


print("[+] Fake IoT Camera Started")
print(f"[+] Listening on port {PORT}")


while True:

    client, address = server.accept()

    attacker_ip = address[0]

    print(f"[!] Connection from {attacker_ip}")


    client.send(
        b"Fake IoT Camera\n"
    )


    client.send(
        b"Username: "
    )


    username = receive_input(client)

    client.send(
        b"Password: "
    )


    password = receive_input(client)


    print("----- Login Attempt -----")
    print(f"IP: {attacker_ip}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("-------------------------")


    client.send(
        b"Login failed\n"
    )


    client.close()