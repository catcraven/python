import http.server
import socketserver
import sys

req_handler = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer

protocol = "HTTP/1.0"

# passing remote server port
if sys.argv[1:]:
    http_port = int(sys.argv[1])
else:
    http_port = 8080

server_address = ('localhost', http_port)

# invoking server
req_handler.protocol_version = protocol
http = socketserver.TCPServer(server_address, req_handler)

# Getting logs
sa = http.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
http.serve_forever()

