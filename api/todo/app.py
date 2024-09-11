from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from routes.todo_routes import handle_todo_routes

API = '/api/todos'
PORT = 8080


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith(API):
            response = handle_todo_routes(self.path, "GET")
            self._send_response(200, response)

    def do_POST(self):
        if self.path.startswith(API):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            response = handle_todo_routes(self.path, "POST", post_data)
            self._send_response(200, response)

    def do_PUT(self):
        if self.path.startswith(API):
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            response = handle_todo_routes(self.path, "PUT", put_data)
            self._send_response(200, response)

    def do_DELETE(self):
        if self.path.startswith(API):
            response = handle_todo_routes(self.path, "DELETE")
            self._send_response(200, response)

    def _send_response(self, status_code, response):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Running server on port {PORT}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
