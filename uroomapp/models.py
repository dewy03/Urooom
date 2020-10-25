from django.db import models

# Create your models here.
class Room(models.Model):
    insurance = models.CharField(max_length=5)
    monthly = models.CharField(max_length=5)
    adress = models.CharField(max_length=500)
    contact = models.CharField(max_length=20)
    explain = models.TextField()