#!/usr/bin/env python3
"""Simple API server using http.server"""

import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Custom handler for our simple API."""

    def do_GET(self):
        """Handle GET requests to various endpoints."""

        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpoint: returns a JSON object
        elif self.path == "/data":
            data = json.dumps({
                "name": "John",
                "age": 30,
                "city": "New York"
            })
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(data.encode())

        # /status endpoint: returns plain text OK
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Any other path: return 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    # Set up and run the HTTP server on localhost:8000
    server_address = ("", 8080)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running at http://localhost:8080...")
    httpd.serve_forever()
