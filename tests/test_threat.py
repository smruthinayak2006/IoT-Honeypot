import sys


sys.path.append(
    "honeypot"
)


from threat_intel import analyze_threat



ip = "127.0.0.1"


result = analyze_threat(
    ip
)


print(
    "\n===== THREAT INTELLIGENCE ====="
)


print(
    "IP Address:",
    result["ip"]
)


print(
    "Attempts:",
    result["attempts"]
)


print(
    "Risk:",
    result["risk"]
)


print(
    "Reason:",
    result["reason"]
)