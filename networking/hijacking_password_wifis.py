import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode().split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]

for wifi in wifis:
    res = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    for line in res:
        if 'Key Content' in line:
            res = [line.split(':')[1][1:-1]]

    try:
        print(f'name:{wifi} , Password {res[0]}')
    except:
        print(f'name:{wifi} , Password UnKnown')