#!/usr/bin/env python3
"""
Simple static docs server for ai-systems-notes.

Run:
    python serve.py
Then open http://localhost:8000
"""
import os
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", "8000"))
HOST = os.environ.get("HOST", "127.0.0.1")
HERE = os.path.dirname(__file__)
DOCS_DIR = os.path.join(HERE, "docs")

if not os.path.isdir(DOCS_DIR):
    print("No docs directory found at", DOCS_DIR)
    sys.exit(1)

def main():
    addr = (HOST, PORT)
    handler = partial(SimpleHTTPRequestHandler, directory=DOCS_DIR)
    httpd = ThreadingHTTPServer(addr, handler)
    print(f"Serving {DOCS_DIR} at http://{addr[0]}:{addr[1]}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    main()
