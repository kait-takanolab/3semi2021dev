import http.server
import socketserver

LISTEN_PORT = 8080
SimpleHandler = http.server.SimpleHTTPRequestHandler

if __name__ == "__main__":
    HOST, PORT = '', LISTEN_PORT

    with socketserver.TCPServer((HOST, PORT), SimpleHandler) as server:
        server.serve_forever()