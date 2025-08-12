from http.server import BaseHTTPRequestHandler, HTTPServer
import json, random, os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            return self._ok({"status": "ok"})
        
        # Simulate a fake “risk score” between 0 and 1
        payload = {
            "risk_score": round(random.uniform(0, 1), 3),
            "explanation": {
                "exposure_score": 0.42,
                "vaccinated": 1
            }
        }
        return self._ok(payload)

    def _ok(self, payload):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    print(f"Starting API server on port {port}...")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
