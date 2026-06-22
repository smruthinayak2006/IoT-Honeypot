"""
Dashboard Authentication
"""

from config import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD
)



def verify_login(
    username,
    password
):


    if (
        username == ADMIN_USERNAME
        and
        password == ADMIN_PASSWORD
    ):


        return True


    return False
