"""
Security Event Logger
"""

import logging
import os


LOG_FOLDER = "logs"


os.makedirs(
    LOG_FOLDER,
    exist_ok=True
)


logging.basicConfig(

    filename="logs/security.log",

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)



def log_info(message):

    logging.info(
        message
    )



def log_warning(message):

    logging.warning(
        message
    )



def log_critical(message):

    logging.critical(
        message
    )