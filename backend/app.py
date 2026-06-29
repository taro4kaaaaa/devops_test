from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()


def run():
    server = HTTPServer(("0.0.0.0", 8080), RequestHandler)
    print("Server started on port 8080")
    server.serve_forever()


if __name__ == "__main__":
    run()