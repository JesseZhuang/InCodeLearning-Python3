import logging

logger = logging.getLogger(__name__)  # default logging goes to consoleg
logging.basicConfig(level=logging.INFO)  # default level is warning

try:
    logging.info("start running")
    1 / 0
except ZeroDivisionError:
    logging.exception("Deliberate divide by zero traceback")
    raise

logging.info("continuing?")
