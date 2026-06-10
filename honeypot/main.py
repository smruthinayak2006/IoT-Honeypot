"""
IoT Honeypot Starter
"""

from server import start_server

from database import create_database



if __name__ == "__main__":


    create_database()


    start_server()