from django.db import models

# Create your models here.
class Product(models.Model):
    nama = models.CharField(max_length=255)
    banyak = models.IntegerField()
    deskripsi = models.TextField()
    harga = models.IntegerField()
    jenis = models.CharField(max_length=100)
    
