from django.db import models
from os import device_encoding
from django.db.models.base import Model
#Insert the data mode
'''
1.id
2.device
3.timestamp
'''

'''
//For the trans data.
1. air temp
2. soil temp
3. humidity  (soil)
4. Co2
5. light
'''
class Recv_Sensor(models.Model):

    #id=models.AutoField(primary_key=True)
    #device=models.CharField(max_length=25)
    time=models.FloatField()
    air_temp=models.FloatField()
    soil_temp=models.FloatField()
    humidity=models.FloatField()
    Co2=models.FloatField()

# Create your models here.
