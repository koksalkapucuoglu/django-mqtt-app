import paho.mqtt.client as mqtt
import time
import json

def on_message(client, userdata, message):
    # print("received message: " ,str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    
    m_decode=str(message.payload.decode("utf-8","ignore"))
    print("received message: ",m_decode)
    m_in=json.loads(m_decode) #decode json data
    print("temperature = ",m_in["temperature"])

mqttBroker ="mqtt.eclipseprojects.io"

"""
client_id: Smartphone
client_id is the unique client id string used when connecting to the broker
"""
client = mqtt.Client("DjangoAPP")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe([("temperature", 0), ("humidity", 0), ("error", 0), ("lat", 0), ("lon", 0)])
client.subscribe("topic1")
client.on_message=on_message 

time.sleep(60)
client.loop_stop()