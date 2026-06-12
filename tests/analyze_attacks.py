import sys
import os


sys.path.append(
    os.path.abspath("honeypot")
)


from analyzer import (
    total_attacks,
    common_usernames,
    common_passwords
)



print("===================")

print("HONEYPOT REPORT")

print("===================")



total_attacks()


common_usernames()


common_passwords()