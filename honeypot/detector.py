"""
Brute force detector
"""

from database import save_alert


attack_count = {}


def detect_bruteforce(ip_address):

    if ip_address not in attack_count:

        attack_count[ip_address] = 1


    else:

        attack_count[ip_address] += 1



    if attack_count[ip_address] >= 3:


        print(
            "[ALERT] Possible brute force detected!"
        )


        print(
            "Attacker IP:",
            ip_address
        )


        save_alert(
            ip_address,
            "Possible brute force attack detected"
        )