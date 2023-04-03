# subscriber.py
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("wokwi-weather/#")
# the callback function, it will be triggered when receiving messages 
def on_message(client, userdata, msg):
    print(f" {msg.topic}")
    print(f" {msg.payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("broker.mqttdashboard.com",1883,60)

# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()