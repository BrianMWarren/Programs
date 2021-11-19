import requests
import json
import subprocess
import time
import paho.mqtt.client as mqtt

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

def StartShow(client, userdata, message):
    SendScene("haloweenscroll")

    # bashCmd = ['DISPLAY=:0.0 /usr/bin/vlc --playlist-autostart --play-and-exit --no-loop "/media/pi/PhotoBackup/Music"']
    bashCmd = ['/usr/bin/vlc', '--playlist-autostart', '--play-and-exit', '--no-loop', "/home/pi/Desktop/Music/"]
    process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

    SendScene("off")
# def StartShow(client, userdata, message):
#     print("Workin here")
#     print(message)
   

def OnConnect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code =",rc)
    else:
        print("Bad connection Returned code =",rc)

broker_address="homeassistant.local"
port = 1883
print("creating new instance")
client = mqtt.Client("Computer Room Pi") #create new instance
print("connecting to broker")
client.on_connect=OnConnect
client.connect(broker_address, port, 30) #connect to broker
print("Subscribing to topic","house/holidayShow")
client.subscribe("house/holidayShow")
client.on_message = StartShow
print("starting mqtt loop")

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()