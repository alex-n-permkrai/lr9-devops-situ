"""Small HTTP server application."""

import http.server
import socketserver

PORT = 8000


class ReusableTCPServer(socketserver.TCPServer):
    """TCP server with reusable address."""

    allow_reuse_address = True


class TestMe:
    """Class used by unit tests."""

    @staticmethod
    def take_five():
        """Return five."""
        return 5

    @staticmethod
    def port():
        """Return application port."""
        return PORT


def main():
    """Start HTTP server."""
    handler = http.server.SimpleHTTPRequestHandler

    with ReusableTCPServer(("", PORT), handler) as httpd:
        print(f"serving at port {PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
