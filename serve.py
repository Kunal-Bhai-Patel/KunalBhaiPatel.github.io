#!/usr/bin/env python3
"""
Simple local development server for Kunal Bhai Patel's Portfolio.
Serves the generated static files in `dist/`.
Usage: python serve.py [port]
"""

import sys
import http.server
import socketserver
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIRECTORY = Path(__file__).resolve().parent / "dist"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving Kunal Bhai Patel's portfolio from: {DIRECTORY}")
        print(f"Local URL: http://localhost:{PORT}/")
        print(f"English:   http://localhost:{PORT}/en/")
        print(f"Deutsch:   http://localhost:{PORT}/de/")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run()
