import logging


logger = logging.getLogger(__name__)  # default logging goes to consoleg
logging.basicConfig(level=logging.INFO)  # default level is warning


try:
    1/0
except ZeroDivisionError:
    logging.exception("Deliberate divide by zero traceback")
    raise

print("continuing?")
