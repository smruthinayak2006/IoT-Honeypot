"""
Attack Detection Engine
"""


from database import save_alert, block_ip
from config import BRUTE_FORCE_LIMIT
from security_logger import log_critical

attempts = {}



def detect_bruteforce(ip):


    if ip not in attempts:

        attempts[ip] = 1


    else:

        attempts[ip] += 1



    if attempts[ip] >= BRUTE_FORCE_LIMIT:


        log_critical(
            f"Brute force detected from {ip}"
        )


        print(
            "Attacker IP:",
            ip
        )


        save_alert(
            ip,
            "Possible brute force attack detected"
        )


        block_ip(
            ip
        )