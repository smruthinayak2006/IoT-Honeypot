"""
SOC Style Incident Report Generator
"""

import sqlite3
from datetime import datetime

from config import DATABASE_PATH



def generate_incident_report():


    connection = sqlite3.connect(
        DATABASE_PATH
    )


    cursor = connection.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM attacks"
    )

    total_attacks = cursor.fetchone()[0]


    cursor.execute(
        """
        SELECT COUNT(DISTINCT ip_address)
        FROM attacks
        """
    )

    unique_ips = cursor.fetchone()[0]


    cursor.execute(
        """
        SELECT username, COUNT(*)
        FROM attacks
        GROUP BY username
        ORDER BY COUNT(*) DESC
        LIMIT 5
        """
    )

    usernames = cursor.fetchall()


    cursor.execute(
        """
        SELECT password, COUNT(*)
        FROM attacks
        GROUP BY password
        ORDER BY COUNT(*) DESC
        LIMIT 5
        """
    )

    passwords = cursor.fetchall()


    cursor.execute(
        """
        SELECT ip_address
        FROM blocked_ips
        """
    )


    blocked = cursor.fetchall()


    connection.close()


    filename = (
        "reports/"
        +
        "incident_report_"
        +
        datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        +
        ".txt"
    )


    with open(
        filename,
        "w"
    ) as report:


        report.write(
            "IoT HONEYPOT INCIDENT REPORT\n"
        )


        report.write(
            "=" * 40 + "\n\n"
        )


        report.write(
            f"Generated: {datetime.now()}\n\n"
        )


        report.write(
            f"Total Attacks: {total_attacks}\n"
        )


        report.write(
            f"Unique Attackers: {unique_ips}\n\n"
        )


        report.write(
            "Top Usernames:\n"
        )


        for item in usernames:

            report.write(
                f"{item[0]} : {item[1]}\n"
            )


        report.write(
            "\nTop Passwords:\n"
        )


        for item in passwords:

            report.write(
                f"{item[0]} : {item[1]}\n"
            )


        report.write(
            "\nBlocked IPs:\n"
        )


        for ip in blocked:

            report.write(
                f"{ip[0]}\n"
            )


    print(
        "[+] Incident report generated:",
        filename
    )


    return filename