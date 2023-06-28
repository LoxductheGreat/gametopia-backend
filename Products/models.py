from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    brand_name = models.CharField(max_length=20)
    genre = models.CharField(max_length=100, default='pls add genre')
    developer = models.CharField(max_length=30, default='Please ADD Developer')
    publisher = models.CharField(max_length=30, default='Please ADD Publisher')
    

    # def __str__(self):
    #     return self.name

