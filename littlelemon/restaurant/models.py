from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(null=True)
    time = models.CharField(max_length=5)
    
