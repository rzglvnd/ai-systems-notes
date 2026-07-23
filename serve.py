#!/usr/bin/env python3
"""
Simple static docs server for ai-systems-notes.

Run:
    python serve.py
Then open http://localhost:8000
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8000"))
HERE = os.path.dirname(__file__)
DOCS_DIR = os.path.join(HERE, "docs")

if not os.path.isdir(DOCS_DIR):
    print("No docs directory found at", DOCS_DIR)
    sys.exit(1)

os.chdir(DOCS_DIR)
class Handler(SimpleHTTPRequestHandler):
    pass

def main():
    addr = ("127.0.0.1", PORT)
    httpd = HTTPServer(addr, Handler)
    print(f"Serving {DOCS_DIR} at http://{addr[0]}:{addr[1]}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    main()
