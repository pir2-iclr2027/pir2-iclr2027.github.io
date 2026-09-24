"""Local preview server with browser caching disabled."""
import functools
import http.server
import sys
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 53647
ROOT = Path(__file__).resolve().parent


class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


handler = functools.partial(NoCache, directory=str(ROOT))
http.server.ThreadingHTTPServer(("0.0.0.0", PORT), handler).serve_forever()
