from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    ip_adress = models.GenericIPAddressField()
    is_online = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name