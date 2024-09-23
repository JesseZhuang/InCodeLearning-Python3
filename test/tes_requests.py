import requests  # need to pip install before testing
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("starting request")
r = requests.get("https://w3schools.com/python/demopage.htm")

logger.info(f"response text: {r.text}")
logger.info(f"response: {r}")  # INFO:__main__:response: <Response [200]>
