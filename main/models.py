from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    banyak = models.IntegerField()
    deskripsi = models.TextField()
    harga = models.IntegerField()
    jenis = models.CharField(max_length=100)
    
#Dummy1: halotest1
#Dummy2: halotest2
