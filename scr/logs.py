"""
Логирование в проекте.
"""

import logging
from functools import wraps

from scr.cfg import config


logging.basicConfig(
    level=logging.INFO,
    filename=config.logs_directory,
    format="%(filename)s %(asctime)s %(levelname)s %(message)s"
)
logging.info("start logger")


def log_db(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:

            result = func(*args, **kwargs)

            return result
        except Exception as error:
            logging.exception(error)
    return wrapper

