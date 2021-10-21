from django.db import models
from datetime import datetime, date


# Create your models here.

class KidModel(models.Model):
    
    name = models.CharField(("Name"), max_length=20)
    Date = models.DateField(("Date"), auto_now_add=True)




class ParentModel(models.Model):
    name = models.CharField(("Name"), max_length=20)
    Date = Date = models.DateField(("Date"), auto_now_add=True)