# publishing to a topic

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

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
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)
