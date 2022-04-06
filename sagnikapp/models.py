# from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    messages = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.name


class BMI(models.Model):
    name = models.CharField(max_length=30)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    bmi = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return str(self.id)
class CALORIE(models.Model):
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    physical_activity = models.CharField(max_length=50) 
    calorie =  models.CharField(max_length=50) 
    date = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return str(self.id)






