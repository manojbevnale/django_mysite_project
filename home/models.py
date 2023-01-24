from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    image = models.ImageField(upload_to='services/',default='')

class About(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    image = models.ImageField(upload_to='upload/about/',default='')

class Contact(models.Model):
    name=models.CharField(max_length=250,default='')
    email=models.EmailField(max_length=254,default='')
    message=models.TextField(default='')
    number=models.CharField(max_length=10,default='')
