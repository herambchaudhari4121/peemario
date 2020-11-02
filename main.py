import http.server
import socketserver
import random
import logging
from subprocess import Popen

logging.basicConfig(filename='loggiez.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
PORT = 8069
print("ill be alive at http://18.223.24.247" + str(PORT))

Handler = http.server.SimpleHTTPRequestHandler
p = Popen(['python3', 'app.py'])

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("im alive at http://18.223.24.247" + str(PORT))
    httpd.serve_forever()
