from django.shortcuts import render

from devices.models import Device

import socket
import getpass

hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def home(request):
    hostname= "Unbekannt"
    local_ip = "127.0.0.1"
    username = "Unbekannt"
    visitor_ip = "Unbekannt"
    found_devices = []
    try:
        hostname = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()

        username = getpass.getuser()

        x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward_for:
            visitor_ip = x_forward_for.split(',')[0]
        else:
            visitor_ip = request.META.get('REMOTE_ADDR')


    except Exception as e:
        print(f"Fehler beim abrufen der Netzwerkinfos: {e}")
        
    all_devices = Device.objects.all()

    context = {
        "hostname": hostname,
        "ip": local_ip,
        "username": username,
        "visitor_ip": visitor_ip,
        "devices": all_devices,
    }

    return render(request, "index.html", context)