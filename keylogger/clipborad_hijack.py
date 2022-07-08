# [ip omsta;; pyperclip
import pyperclip
import time

list = []

while True:
    if pyperclip.paste() != 'None':
        TempVal = pyperclip.paste() #

        if TempVal not in list:
            list.append(TempVal)

        print(list)

        time.sleep(5)
