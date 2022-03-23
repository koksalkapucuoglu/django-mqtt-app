from django.contrib import admin

from .models import Broker, Device

admin.site.register(Device)
admin.site.register(Broker)
