from http.client import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang='en'>")
        self.wfile.write(b"<title>")
        self.wfile.write(b"")
        self.wfile.write(b"")
        self.wfile.write(b"")
        self.wfile.write(b"")



port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)