"""
Threat Intelligence Engine
"""

import sqlite3

from config import DATABASE_PATH



def analyze_threat(
    ip_address
):


    connection = sqlite3.connect(
        DATABASE_PATH
    )


    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attacks
        WHERE ip_address=?
        """,
        (
            ip_address,
        )
    )


    attack_count = cursor.fetchone()[0]


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM blocked_ips
        WHERE ip_address=?
        """,
        (
            ip_address,
        )
    )


    blocked = cursor.fetchone()[0]


    connection.close()



    if blocked:


        risk = "CRITICAL"

        reason = (
            "Attacker IP has been blocked"
        )


    elif attack_count >= 5:


        risk = "HIGH"

        reason = (
            "Multiple failed login attempts detected"
        )


    elif attack_count >= 3:


        risk = "MEDIUM"

        reason = (
            "Suspicious login activity detected"
        )


    else:


        risk = "LOW"

        reason = (
            "Limited activity detected"
        )



    return {
        "ip": ip_address,
        "attempts": attack_count,
        "risk": risk,
        "reason": reason
    }