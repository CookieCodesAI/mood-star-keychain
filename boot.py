#make sure that your esp32 has the umqttsimple.py uploaded onto it
from umqttsimple import MQTTClient
import network

# add your info here to connect to your wifi
ssid = "network name"
password = "network password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print("connected to ", wlan.ifconfig())