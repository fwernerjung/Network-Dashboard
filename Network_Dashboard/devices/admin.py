from django.contrib import admin

# Importiere dein Model (z.B. Device aus der devices-App)
from .models import Device

# Registriere das Model im Admin
admin.site.register(Device)