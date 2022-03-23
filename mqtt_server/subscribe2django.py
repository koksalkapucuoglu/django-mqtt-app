import paho.mqtt.client as mqtt
import time
import json
import requests
from mqtt_api import mqttAPI

def on_message(client, userdata, message):
    m_decode=str(message.payload.decode("utf-8","ignore"))
    print("received message: ",m_decode)
    m_in=json.loads(m_decode) #decode json data

    device_id = mqttAPI.get_device(serial=m_in["device_serial"])
    if device_id != "404":
        print(f'device id: {device_id}')
        
        response_broker = mqttAPI.create_broker(m_in, device_id)

        if response_broker != "404":
            print(f'response_broker: {response_broker}')

mqttBroker ="mqtt.eclipseprojects.io"

"""
client_id: Smartphone
client_id is the unique client id string used when connecting to the broker
"""
client = mqtt.Client("DjangoAPP")
client.connect(mqttBroker) 

mqttAPI = mqttAPI()
client.loop_start()

client.subscribe("topic1")
client.on_message=on_message 

time.sleep(12000)
client.loop_stop()