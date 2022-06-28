from http.server import BaseHTTPRequestHandler, HTTPServer

import time


hostname = "0.0.0.0"
port = 8080


class BasicServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Docker with Python</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Docker with python example.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webserver = HTTPServer((hostname, port), BasicServer)
    print(f"Server started http://{hostname}:{port}")

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server down")
