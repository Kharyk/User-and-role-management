from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, default= "user")
    
    def __str__(self):
        return name
# Create your models here.
