"""
Fake IoT Telnet Server
"""


import socket


from logger import save_log
from detector import detect_bruteforce
from database import save_attack


HOST = "0.0.0.0"

PORT = 2323



def receive_input(client):


    data = ""


    while True:


        character = (
            client.recv(1)
            .decode()
        )


        if character == "\n":

            break


        data += character


    return data.strip()




def start_server():


    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )


    server.bind(
        (HOST, PORT)
    )


    server.listen(5)



    print(
        "[+] IoT Honeypot Running"
    )


    print(
        f"[+] Listening on {PORT}"
    )



    while True:


        client, address = (
            server.accept()
        )


        attacker_ip = (
            address[0]
        )


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



        client.send(
            b"Login failed\n"
        )


        client.close()