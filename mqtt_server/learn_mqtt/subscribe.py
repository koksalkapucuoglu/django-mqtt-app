import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="mqtt.eclipseprojects.io"

"""
client_id: Smartphone
client_id is the unique client id string used when connecting to the broker
"""
client = mqtt.Client("Smartphone")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("TEMPERATURE")
client.on_message=on_message 

time.sleep(30)
client.loop_stop()