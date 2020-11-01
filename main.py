import http.server
import socketserver

PORT = randrange(8000, 8999, 2)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("http://18.223.24.247" + str(PORT))
    httpd.serve_forever()
