from rest_framework import viewsets
from django.shortcuts import render
from django.contrib import messages
from collections import Counter

from mqtt_server.mqtt_api import mqttAPI

from .models import Broker, Device
from .serializers import BrokerSerializer, DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = []
    filterset_fields = ['id', 'name', 'serial', 'brokers']


class BrokerViewSet(viewsets.ModelViewSet):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer
    permission_classes = []
    filterset_fields = ['id', 'temperature', 'humidity',
                        'error', 'lat', 'lon', 'created_at', 'device_serial']


from rest_framework.response import Response

def last_broker(device_id):
    # return Broker.objects.filter(device_serial=device_id).order_by('id').last()
    return Broker.objects.filter(device_serial=device_id).order_by('id').values().last()

def deviceList(request):
    """ get device list and render to html page """

    _mqttAPI = mqttAPI()

    response_device_list = _mqttAPI.get_device_list(page=1)

    if response_device_list.status_code == 200:
        device_list_dict = response_device_list.json()

        # get last broker for every devices
        for device in device_list_dict["results"]:
            device_id = device["id"]
            last_broker_at_given_device = last_broker(device_id = device_id)
            
            last_broker_dict = {
                "last_broker_id": last_broker_at_given_device["id"],
                "temperature": last_broker_at_given_device["temperature"],
                "humidity": last_broker_at_given_device["humidity"],
                "error": last_broker_at_given_device["error"],
                "lat": last_broker_at_given_device["lat"],
                "lon": last_broker_at_given_device["lon"],
                "created_at": last_broker_at_given_device["created_at"],
            }
            
            device["last_broker"] = last_broker_dict
    else:
        device_list_dict = {
                            "status_code": 404,
                            "type": "internal_error"
        }
        messages.warning(request,"Something went wrong...")


    content = {
        "device_list_dict": device_list_dict
    }
    return render(request, "devicelist.html",content)


def brokerList(request, device_id):
    """ get broker list and render to html page """

    # page control
    page = 1
    new_url = request.POST.get("hidden_nexturl")

    if new_url:
        split_list = new_url.split("page=")
        if len(split_list) == 2:
            new_page_num = int(split_list[-1])
            page = new_page_num

    _mqttAPI = mqttAPI()
    response_broker_list = _mqttAPI.get_broker_list(page=page, device_id=device_id)

    if response_broker_list.status_code == 200:
        broker_list_dict = response_broker_list.json()
        if len(broker_list_dict["results"]) > 0:
            broker_list_dict["device_serial_id"] = response_broker_list.json()["results"][0]["device_serial"]
    else:
        broker_list_dict = {
                            "status_code": 404,
                            "type": "internal_error"
        }
        messages.warning(request,"Something went wrong...")


    content = {
        "broker_list_dict": broker_list_dict
    }
    return render(request, "brokerlist.html",content)

        