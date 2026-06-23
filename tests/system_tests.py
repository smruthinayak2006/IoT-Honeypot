"""
IoT Honeypot System Test Suite
"""


import sys
import os


sys.path.append(
    "honeypot"
)


from database import create_table
from threat_intel import analyze_threat
from auth import verify_login



def test_database():


    try:


        create_table()


        print(
            "[PASS] Database connection test"
        )


        return True


    except Exception as error:


        print(
            "[FAIL] Database test:",
            error
        )


        return False




def test_threat_engine():


    try:


        result = analyze_threat(
            "127.0.0.1"
        )


        if "risk" in result:


            print(
                "[PASS] Threat intelligence test"
            )


            return True


    except Exception as error:


        print(
            "[FAIL] Threat engine:",
            error
        )


        return False




def test_authentication():


    try:


        result = verify_login(
            "wrong",
            "wrong"
        )


        if result == False:


            print(
                "[PASS] Authentication test"
            )


            return True



    except Exception as error:


        print(
            "[FAIL] Authentication:",
            error
        )


        return False




def run_tests():


    print(
        "\n===== HONEYPOT TEST SUITE =====\n"
    )


    results = []


    results.append(
        test_database()
    )


    results.append(
        test_threat_engine()
    )


    results.append(
        test_authentication()
    )


    print(
        "\n=============================="
    )


    print(
        "Tests Passed:",
        results.count(True),
        "/",
        len(results)
    )


    print(
        "=============================="
    )




if __name__ == "__main__":


    run_tests()