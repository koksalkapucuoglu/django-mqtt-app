from rest_framework import serializers

from .models import Broker, Device


class DeviceSerializer(serializers.ModelSerializer):
    brokers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Broker.objects.all(),
        required=False
    )

    class Meta:
        model = Device
        fields = ['id', 'name', 'serial', 'brokers']


class BrokerSerializer(serializers.ModelSerializer):
    device_serial = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
    )

    class Meta:
        model = Broker
        fields = ['id', 'temperature', 'humidity', 'error',
                  'lat', 'lon', 'created_at', 'device_serial']
