

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import time
import logging 
import sys
from datetime import datetime
import random
import string


hostName = "localhost"
serverPort = 8000
letters = string.ascii_lowercase

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):

        start_datetime=datetime.now()
        logfile = open("startlog.txt", 'a')
        trace_id = ( ''.join(random.choice(letters) for i in range(10)) )
        start_str_date = start_datetime.strftime("%d-%m-%Y:%H:%M:%S:%f" + " Request Landed for %s" %(trace_id) + "\n")
        logfile.write(start_str_date)

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        time.sleep(0.1)
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        
        current_datetime=datetime.now()
        logfile = open("log.txt", 'a')
        #trace_id = ( ''.join(random.choice(letters) for i in range(10)) )
        str_date = current_datetime.strftime("%d-%m-%Y:%H:%M:%S:%f" + " POST successful for %s" %(trace_id) + "\n")
        logfile.write(str_date)


#httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd = HTTPServer((hostName, serverPort), SimpleHTTPRequestHandler)
print("Server started http://%s:%s" % (hostName, serverPort))
httpd.serve_forever()

