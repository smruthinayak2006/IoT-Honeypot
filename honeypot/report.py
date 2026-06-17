"""
Attack Report Generator
"""

import sqlite3
import csv
import os

from datetime import datetime


DATABASE = "database/attacks.db"



def generate_report():


    os.makedirs(
        "reports",
        exist_ok=True
    )


    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM attacks"
    )


    attacks = cursor.fetchall()


    filename = (
        "reports/"
        "attack_report_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".csv"
    )


    with open(
        filename,
        "w",
        newline=""
    ) as file:


        writer = csv.writer(
            file
        )


        writer.writerow(
            [
                "ID",
                "IP Address",
                "Username",
                "Password",
                "Timestamp"
            ]
        )


        writer.writerows(
            attacks
        )



    conn.close()



    print(
        "[+] Report generated:",
        filename
    )