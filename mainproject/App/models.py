from django.db import models


# Create your models here.
class Student (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(),
    
class Data (models.Model):
    name=models.CharField(max_length=100)
    prize=models.IntegerField()
    image = models.ImageField(upload_to='img/',)



    
