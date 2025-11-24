from flask import Flask, jsonify
import random, string, threading, datetime, logging, sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stdout,
)

app = Flask(__name__)

# Create the random string at startup
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def log_random():
    logging.info("random=%s", random_string)
    threading.Timer(5.0, log_random).start()

@app.route("/status")
def status():
    return jsonify({
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "random": random_string
    })

if __name__ == "__main__":
    log_random()
    app.run(host="0.0.0.0", port=3000)