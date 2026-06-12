"""
Utility functions
"""

import re


def clean_input(text):


    # Handle backspace characters

    while "\x08" in text:


        position = text.find("\x08")


        if position > 0:


            text = (
                text[:position - 1]
                +
                text[position + 1:]
            )


        else:


            text = text.replace(
                "\x08",
                ""
            )


    # Remove terminal escape sequences

    text = re.sub(
        r"\x1b\[[0-9;]*[A-Za-z~]",
        "",
        text
    )


    return text.strip()