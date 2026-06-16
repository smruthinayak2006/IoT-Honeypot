"""
IoT Honeypot Main File
"""

from server import start_server
from database import create_table


if __name__ == "__main__":


    create_table()


    try:


        start_server()


    except KeyboardInterrupt:


        print(
            "\n[+] Honeypot stopped"
        )