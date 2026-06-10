"""
Detect suspicious activity
"""


attack_counter = {}


def detect_bruteforce(ip):


    if ip not in attack_counter:


        attack_counter[ip] = 1


    else:


        attack_counter[ip] += 1



    if attack_counter[ip] >= 3:


        print(
            "[ALERT] Possible brute force detected!"
        )


        print(
            f"Attacker IP: {ip}"
        )