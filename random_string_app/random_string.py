
import random, string, threading, datetime, logging, sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stdout,
)

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def printit():
    threading.Timer(5.0, printit).start()
    logging.info("random=%s", random_string)

printit()