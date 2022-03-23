from email.headerregistry import BaseHeader
import json
import requests
import datetime


class mqttAPI:
    def __init__(self):
        self.baseURL = 'http://127.0.0.1:8000/api/'
        self.baseHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
    
    # for mqtt server

    def get_device(self, serial):
        """ get device id by serial"""

        response = requests.get(self.baseURL+'device/?serial='+ serial,
                            headers=self.baseHeaders)    

        if response.status_code == 200:
            return response.json()["results"][0]["id"]
            
        else:
            # print(f'response: {response}')
            return "404"

    def create_broker(self, recieved_message, device_id):
        """ create broker by recieved message""" 

        url = "http://127.0.0.1:8000/api/broker/"

        payload = json.dumps({
                                "device_serial": device_id,
                                "temperature": recieved_message["temperature"],
                                "humidity": recieved_message["humidity"],
                                "error": recieved_message["error"],
                                "lat": recieved_message["lat"],
                                "lon": recieved_message["lon"],
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 201:
            return response.json()
            
        else:
            print(f'response: {response.json()}')
            return "404"
    
    # for mqtt backend service

    def get_device_list(self, serial="", page=1):
        """ get device list"""

        response = requests.get(    
                            self.baseURL+'device/?serial='+ serial +"&page="+ str(page),
                            headers=self.baseHeaders
        )    

        return response

    def get_broker_list(self, device_id="", page=1):
        """ get broker list"""

        response = requests.get(    
                            self.baseURL+'broker/?device_serial='+ str(device_id) +"&page="+ str(page),
                            headers=self.baseHeaders
        )    

        return response