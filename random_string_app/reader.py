from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import datetime

FILE_PATH = "/shared/random.txt"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status":
            if not os.path.exists(FILE_PATH):
                self.send_response(404)
                self.end_headers()
                return
            try:
                with open(FILE_PATH, "r") as f:
                    # return the last non-empty line
                    lines = [l.strip() for l in f.readlines() if l.strip()]
                    if not lines:
                        self.send_response(204)
                        self.end_headers()
                        return
                    last = lines[-1]
                    # expect: "<iso-ts> <random>"
                    parts = last.split(" ", 1)
                    ts = parts[0]
                    val = parts[1] if len(parts) > 1 else ""
                    payload = {"timestamp": ts, "random": val}
                    body = json.dumps(payload).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
            except Exception:
                self.send_response(500)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run(port: int = 3000):
    server = HTTPServer(("0.0.0.0", port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == "__main__":
    run()
