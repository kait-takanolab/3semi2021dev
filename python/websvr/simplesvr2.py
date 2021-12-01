import http.server
import socketserver

LISTEN_PORT = 8080

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    # GETの場合の応答
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>It works!</h1>")

    # POSTの場合の応答
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Response to POST method</h1>")

if __name__ == "__main__":
    HOST, PORT = '', LISTEN_PORT

    with socketserver.TCPServer((HOST, PORT), ServerHandler) as server:
        server.serve_forever()