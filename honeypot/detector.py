"""
Attack Detection Engine
"""


from database import save_alert, block_ip
from config import BRUTE_FORCE_LIMIT


attempts = {}



def detect_bruteforce(ip):


    if ip not in attempts:

        attempts[ip] = 1


    else:

        attempts[ip] += 1



    if attempts[ip] >= BRUTE_FORCE_LIMIT:


        print(
            "[ALERT] Possible brute force detected!"
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