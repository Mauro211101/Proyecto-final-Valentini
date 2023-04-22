from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE, primary_key=True)
    acerca_de_mi = models.CharField(max_length=128)
    imagen = models.ImageField(upload_to="profiles",null=True,blank=True)

    
