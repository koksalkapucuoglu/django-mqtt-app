# publishing to a topic

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import json

mqttBroker ="mqtt.eclipseprojects.io" 
# mqttBroker ="test.mosquitto.org" 

"""
> mqtt.eclipseprojects.io <
This is a public test MQTT broker service. It currently listens on the following ports:

1883 : MQTT over unencrypted TCP
8883 : MQTT over encrypted TCP
80 : MQTT over unencrypted WebSockets (note: URL must be /mqtt )
443 : MQTT over encrypted WebSockets (note: URL must be /mqtt )
"""

"""
client_id: Temperature_Inside
client_id is the unique client id string used when connecting to the broker
"""
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

while True:

    randNumber_temp = uniform(20.0, 22.0)
    randNumber_hum = uniform(20.0, 40.0)
    randNumber_lat = uniform(35.0, 45.0)
    randNumber_lon = uniform(20.0, 30.0)

    payload = {
            "device_serial":"LOREM1234",
            "temperature":randNumber_temp,
            "humidity":randNumber_hum,
            "error":False,
            "lat":randNumber_lat,
            "lon":randNumber_lon
            }
            
    data_out=json.dumps(payload) # encode object to JSON
    client.publish("topic1", data_out)
    print("Just published " + data_out + " to topic1")

    # randNumber_temp = uniform(20.0, 22.0)
    # randNumber_hum = uniform(20.0, 40.0)
    # randNumber_lat = uniform(35.0, 45.0)
    # randNumber_lon = uniform(20.0, 30.0)
    # client.publish("temperature", randNumber_temp)
    # client.publish("humidity", randNumber_hum)
    # client.publish("error", False)
    # client.publish("lat", randNumber_lat)
    # client.publish("lon", randNumber_lon)
    # print("Just published " + str(randNumber_temp) + " to topic temperature")
    # print("Just published " + str(randNumber_hum) + " to topic humidity")
    # print("Just published " + str(False) + " to topic error")
    # print("Just published " + str(randNumber_lat) + " to topic lat")
    # print("Just published " + str(randNumber_lon) + " to topic lon")
    print("##########################################################################")
    time.sleep(1)
