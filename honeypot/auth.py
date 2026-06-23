"""
Dashboard Authentication System
with Password Hash Verification
"""


import bcrypt


from config import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD_HASH
)



def verify_login(
    username,
    password
):


    if username != ADMIN_USERNAME:


        return False



    if not ADMIN_PASSWORD_HASH:


        return False



    result = bcrypt.checkpw(
        password.encode(),
        ADMIN_PASSWORD_HASH.encode()
    )



    return result