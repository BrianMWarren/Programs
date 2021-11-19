import requests
import json
import subprocess
import schedule
import time

def SendScene(sceneName):
    url = "http://192.168.1.168:8888/api/scenes"

    _data = {
    "action" : "activate",
    "id" : sceneName
    }

    _data = json.dumps(_data)
    print(_data)

    x = requests.put(url, data= _data)
    print(x.content)

def StartShow():
    SendScene("haloweenscroll")

    # bashCmd = ['DISPLAY=:0.0 /usr/bin/vlc --playlist-autostart --play-and-exit --no-loop "/media/pi/PhotoBackup/Music"']
    bashCmd = ['/usr/bin/vlc', '--playlist-autostart', '--play-and-exit', '--no-loop', "/home/pi/Desktop/Music/"]
    process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

    SendScene("off")

schedule.every().day.at("18:00").do(StartShow)
schedule.every().day.at("19:00").do(StartShow)
# StartShow()
while True:
    schedule.run_pending()
    time.sleep(1)