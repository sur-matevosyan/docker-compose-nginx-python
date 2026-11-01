from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            response = "Hello from Task 11 Backend!"
            status = 200

        elif self.path == "/health":
            response = "OK"
            status = 200

        else:
            response = "Not Found"
            status = 404

        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))


server = HTTPServer(("0.0.0.0", 5000), RequestHandler)

print("Backend running on port 5000")

server.serve_forever()
