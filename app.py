from helmet.logger import logging
import sys

logging.info("i am ready to debug")
from helmet.exception import HelmetException

try:
    a = 2 + "3"
    print(a)
except Exception as ex:
    raise HelmetException(ex, sys) from ex
