from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def encrypt(message):
    publicKey = open("public.pem", "rb")
    publicKeyAfterImport = RSA.importKey(publicKey.read())
    encryptor = PKCS1_OAEP.new(publicKeyAfterImport)
    encrypted_data = encryptor.encrypt(message)
    print(encrypted_data)
    print(len(encrypted_data))
    return encrypted_data

def decrypt(Cipher):
    privateKey = open("private.pem", "rb")
    privateKeyAfterImport = RSA.importKey(privateKey.read())
    decryptor = PKCS1_OAEP.new(privateKeyAfterImport)
    print (decryptor.decrypt(Cipher).decode())

message = 'Hello World'
encrypted_data = encrypt(message.encode())
decrypt(encrypted_data)