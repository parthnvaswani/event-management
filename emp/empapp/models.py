from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    ev_name=models.CharField(max_length=50,unique=True)
    ev_price=models.IntegerField(null=False)
    ev_description=models.CharField(max_length=1000)
    
class Booking(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ev_date=models.DateField(null=False)
    ev_location=models.CharField(max_length=100)
