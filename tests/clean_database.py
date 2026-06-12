import sqlite3
import re


connection = sqlite3.connect(
    "database/attacks.db"
)


cursor = connection.cursor()


cursor.execute(
    "SELECT id, username, password FROM attacks"
)


records = cursor.fetchall()


def clean_text(text):


    # Handle backspace
    while "\x08" in text:

        position = text.find("\x08")


        if position > 0:

            text = (
                text[:position-1]
                +
                text[position+1:]
            )

        else:

            text = text.replace(
                "\x08",
                ""
            )


    # Remove terminal escape codes
    text = re.sub(
        r"\x1b\[[0-9;]*[A-Za-z~]",
        "",
        text
    )


    return text.strip()



for attack_id, username, password in records:


    cursor.execute(
        """
        UPDATE attacks

        SET username=?,
            password=?

        WHERE id=?
        """,

        (
            clean_text(username),
            clean_text(password),
            attack_id
        )
    )


connection.commit()


connection.close()


print(
    "Database sanitized successfully"
)