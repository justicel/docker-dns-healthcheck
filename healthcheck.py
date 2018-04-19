import falcon
import socket
import os

class HealthCheck:
    def on_get(self, req, resp):
        try:
            socket.gethostbyname(os.getenv('HOSTNAME'))
            status = falcon.HTTP_OK
            body   = '{"status": "OK"}'
        except:
            status = falcon.HTTP_500
            body   = '{"status": "FAIL"}'

        resp.content_type = 'application/json'
        resp.status = status
        resp.body   = body

api = falcon.API()
api.add_route('/', HealthCheck())
