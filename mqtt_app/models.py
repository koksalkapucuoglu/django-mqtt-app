from django.db import models
from django.utils import timezone


class Device(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    serial = models.CharField(
        max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = "device"


class Broker(models.Model):

    id = models.AutoField(primary_key=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    error = models.BooleanField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(
        null=True, blank=True, default=timezone.now)
    device_serial = models.ForeignKey(
        'Device', on_delete=models.CASCADE, related_name='brokers')

    class Meta:
        db_table = "broker"
