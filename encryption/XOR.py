
import string
import random




def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])


# Random Key Generator
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))

print(key)

print ("\n" + "Key length = " + str(len(key)))

message = 'ipconfig'

print("Msg: " + message + '\n')


enc = str_xor(message, key)

print("Encrypted message is " + "\n" + enc + "\n")

dec = str_xor(enc, key)
print("Decrypted message is " + "\n" + dec + "\n")
