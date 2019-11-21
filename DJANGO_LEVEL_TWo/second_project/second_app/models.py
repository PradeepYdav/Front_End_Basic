from django.db import models

# Create your models here.

class users(models.Model):
    first_name=models.CharField(max_length=256,unique=True)
    last_name=models.CharField(max_length=256,unique=True)
    email=models.EmailField()
