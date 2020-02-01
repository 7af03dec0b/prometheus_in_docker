#!/usr/bin/env python3
# listens on given port, prints http requests to stdout
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class StaticServer(BaseHTTPRequestHandler):

    def execute_request(self,method):
        filename = 'cached-responses' + self.path + '.json'

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(f"<html><body><h1>output</h1></body></html>".encode("utf8"))
        print('#############################################')
        print('### POST {} - {} - {}'.format(self.client_address, self.request_version, self.path))
        print('### Headers ###\n' + str(self.headers))
        if (method == 'post'):
            if self.headers['Content-Length']:
                msg_length = int(self.headers['Content-Length'])
                print('### POST content ###\n{}'.format(self.rfile.read(msg_length)))
        print('#############################################\n')

    def do_POST(self):
        self.execute_request('post')

    def do_GET(self):
        self.execute_request('get')

def run(server_class=HTTPServer, handler_class=StaticServer, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting Server on port {}'.format(port))
    httpd.serve_forever()

run()
