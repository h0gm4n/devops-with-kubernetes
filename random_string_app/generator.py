import os
import time
import random
import string
import datetime
import signal

OUT_DIR = "/shared"
OUT_FILE = os.path.join(OUT_DIR, "random.txt")

running = True

def handle_sigterm(signum, frame):
    global running
    running = False


signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGINT, handle_sigterm)

os.makedirs(OUT_DIR, exist_ok=True)

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

with open(OUT_FILE, "a", buffering=1) as f:
    while running:
        ts = datetime.datetime.now().isoformat()
        line = f"{ts} {random_string}\n"
        try:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        except Exception:
            # swallow errors briefly and continue
            pass
        time.sleep(5)
