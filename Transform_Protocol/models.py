from django.db import models
from os import device_encoding
from django.db.models.base import Model
#Insert the data mode
'''
1.id
2.device
3.timestamp
4. air temp
5. soil temp
6. humidity
7. Co2
'''
class Sensor(models.Model):

    #id=models.AutoField(primary_key=True)
    #device=models.CharField(max_length=25)
    time=models.FloatField()
    air_temp=models.FloatField()
    soil_temp=models.FloatField()
    humidity=models.FloatField()
    Co2=models.FloatField()

# Create your models here.
