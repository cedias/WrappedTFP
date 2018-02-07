import http.server
import socketserver
import argparse
import os
import webbrowser
import sys



def main(args):
    
    PORT = args["port"]
    FILE = args["file"]

    os.chdir(os.path.dirname(__file__)+"/tpf") 
    # os.symlink(os.path.curdir(),"emb_dir")
    Handler = http.server.SimpleHTTPRequestHandler


    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        webbrowser.open(f"http://localhost:{PORT}", new=0, autoraise=True)
        httpd.serve_forever()
        


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='WrappedTFP')
    parser.add_argument('--port', type=int, default=8989)
    parser.add_argument('--file', type=str, default=None)
    args = parser.parse_args()
    main(vars(args))
