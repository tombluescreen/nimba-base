
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from urllib.parse import urlparse, parse_qs
import json
import action_classes as acc


hostName = "127.0.0.1"
serverPort = 8080
master_holder:acc.Holder

class ControlServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)
        
        if url.path == "/":
            #self.deliver_file("web/base_page.html")
            self.deliver_auto_file()
            return
        elif url.path[0:5] == "/api/":
            hash = url.path[5:]
            
            try:
                self.send_api_response("DataIncoming", master_holder.item_hash_dict[hash].action_f())
                
            except KeyError:
                print("API Call Failed: Hash not found")
                self.send_api_response("Hash Not Found", failed=True)
            
        
    
    def deliver_file(self, path, content_header="text/html"):
        self.send_response(200)
        self.send_header("Content-type", content_header)
        self.end_headers()
        with open(path, "rb") as file:
            self.wfile.write(file.read())

    
    def deliver_auto_file(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("web/base_page.html", "r") as file:

            by = file.read().replace("<div id=\"autodiv\"></div>", f"<div id=\"autodiv\">{master_holder.render_html()}</div>")

            self.wfile.write(by.encode())

    def send_api_response(self, msg, data=None, failed=False):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        typeStr = "successful"
        if failed:
            typeStr = "error"
        
        res = json.dumps({
            "type": typeStr,
            "msg": msg,
            "data": data
        })
        self.wfile.write(bytes(res,"utf-8"))
        

    def test_deliver(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

class WebThread(threading.Thread):
    def __init__(self,passed_holder:acc.Holder):
        threading.Thread.__init__(self)
        self.passed_holder = passed_holder

    def run(self):
        start_webserver(self.passed_holder)


def start_webserver(passed_holder:acc.Holder, new_thread=False):

    if new_thread:
        webThread = WebThread(passed_holder)
        webThread.start()
    else:
        global master_holder
        master_holder = passed_holder
        webServer = HTTPServer((hostName, serverPort), ControlServer)
        print("Server started http://%s:%s" % (hostName, serverPort))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")