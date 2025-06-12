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
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))

        # /status endpoint: returns plain text OK
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            info = {
                    "Version": "1.0", 
                    "Description": "A simple API built with http.server"
                    }
            self.wfile.write(json.dumps(info).encode())

        # Any other path: return 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    # Set up and run the HTTP server on localhost:8000
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running at http://localhost:8000...")
    httpd.serve_forever()
