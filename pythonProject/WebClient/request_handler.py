# import http server libraries and socket server
import http.server
import socketserver

http_port = 8080  # Defining the port number
handler = http.server.SimpleHTTPRequestHandler  # Creating the simple request handler using the http.server
tcpserver = socketserver.TCPServer(("", http_port),
                                   handler)  # TCP server used to send & rec the msg through the req handler

print("your server is running in port " + str(http_port))

tcpserver.serve_forever()  # Starting the server
