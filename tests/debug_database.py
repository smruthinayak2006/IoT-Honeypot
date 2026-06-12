import sqlite3


connection = sqlite3.connect(
    "database/attacks.db"
)


cursor = connection.cursor()


cursor.execute(
    "SELECT username, password FROM attacks"
)


records = cursor.fetchall()


for row in records:

    print(
        repr(row)
    )


connection.close()