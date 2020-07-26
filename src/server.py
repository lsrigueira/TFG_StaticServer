from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import logging
from basededatos import mybd
url = "http://192.168.0.5:8000"
myobj = {'somekey': 'somevalue'}

prueba = mybd()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.headers)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        if ("IPPublica" in self.headers):
            ipPrivate = prueba.findByPublicIp(self.headers['IPPublica'])
            print(ipPrivate)
            response.write(ipPrivate.encode())
            self.wfile.write(response.getvalue())
            return
        self.wfile.write(response.getvalue())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        respuestas = body.decode("utf-8").split("&")
        if ("MAC" in respuestas[0]) and ("IPPrivada" in respuestas[1]) and ("IPPublica" in respuestas[2]):
            try:
                prueba.insertIp(respuestas[0][4:],respuestas[1][10:], respuestas[2][10:])
            except:
                prueba.updateIp(respuestas[0][4:],respuestas[1][10:], respuestas[2][10:])
            response.write(b"Todo ok")
            self.wfile.write(response.getvalue())
            return
        response.write(body)
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('192.168.0.5', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

"""
def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        respuestas = body.decode("utf-8").split("&")
        if ("MAC" in respuestas[0]) and ("IPPrivada" in respuestas[1]) and ("IPPublica" in respuestas[2]):
            try:
                prueba.insertIp(respuestas[0][4:],respuestas[1][10:], respuestas[2][10:])
            except:
                prueba.updateIp(respuestas[0][4:],respuestas[1][10:], respuestas[2][10:])
            response.write(b"Todo ok")
            self.wfile.write(response.getvalue())
            return
        response.write(body)
        self.wfile.write(response.getvalue())
"""