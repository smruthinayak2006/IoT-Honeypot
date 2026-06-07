"""
IoT Honeypot

Day 3:
Creating a fake IoT service listener
"""

import socket


HOST = "0.0.0.0"
PORT = 2323


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


server.bind((HOST, PORT))


server.listen(5)


print("[+] Fake IoT device started")
print(f"[+] Listening on port {PORT}")


while True:

    client, address = server.accept()

    print(f"[!] Connection received from {address}")

    client.send(
        b"Fake IoT Camera Login\n"
    )

    client.close()