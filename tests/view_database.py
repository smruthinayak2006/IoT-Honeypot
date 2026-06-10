import sqlite3


connection = sqlite3.connect(
    "database/attacks.db"
)


cursor = connection.cursor()


cursor.execute(
    "SELECT * FROM attacks"
)


records = cursor.fetchall()


for record in records:

    print(record)


connection.close()