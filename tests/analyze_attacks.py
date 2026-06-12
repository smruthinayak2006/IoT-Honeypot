import sys
import os


sys.path.append(
    os.path.abspath("honeypot")
)


from analyzer import (
    total_attacks,
    top_usernames,
    top_passwords
)



print("===================")

print("HONEYPOT REPORT")

print("===================")



total_attacks()


top_usernames()


top_passwords()