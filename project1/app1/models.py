# Create your models here.
from django.db import models



class Registrtion(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    email = models.EmailField()

 
