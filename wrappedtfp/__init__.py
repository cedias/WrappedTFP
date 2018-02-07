import http.server
import socketserver
import os
import wrappedtfp
import sys

print(sys.argv)
print(sys.dir)
print(os.path.curdir())

PORT = 8989

os.chdir(os.path.dirname(__file__)) #set path to here


os.symlink(os.path.curdir(),"emb_dir")


Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()