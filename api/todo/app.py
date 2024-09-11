from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from routes.todo_routes import handle_todo_routes
from middlewares.validation_middleware import validate_todo_data


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith('/api/todos'):
            response = handle_todo_routes(self.path, "GET")
            self._send_response(200, response)

    def do_POST(self):
        if self.path.startswith('/api/todos'):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            is_valid, validation_error = validate_todo_data(post_data)
            if not is_valid:
                self._send_response(400, {"error": validation_error})
                return

            response = handle_todo_routes(self.path, "POST", post_data)
            self._send_response(201, response)

    def do_PUT(self):
        if self.path.startswith('/api/todos'):
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)

            is_valid, validation_error = validate_todo_data(put_data)
            if not is_valid:
                self._send_response(400, {"error": validation_error})
                return

            response = handle_todo_routes(self.path, "PUT", put_data)
            self._send_response(200, response)

    def _send_response(self, status_code, response):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running server on port 8080...')
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
