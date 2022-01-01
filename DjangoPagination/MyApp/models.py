from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    standard = models.IntegerField()
    stream = models.CharField(max_length=100)
    city = models.CharField(max_length=100)