import sqlite3


conn = sqlite3.connect(
    "database/attacks.db"
)


cursor = conn.cursor()


cursor.execute(
    "SELECT * FROM alerts"
)


for alert in cursor.fetchall():

    print(alert)


conn.close()