from django.db import models
from gametopia import settings

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    brand_name = models.CharField(max_length=20)
    developer = models.CharField(max_length=30, default='')
    publisher = models.CharField(max_length=30, default='')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    release_date = models.DateField(editable=True)

    GENRE_CHOICES = [
        ('AXN', 'Action'),
        ('JRPG', 'JRPG'),
        ('FPS', 'First Person Shooter')
    ]
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, default='')

   

    # CATEGORY_CHOICES = [
    #     ('TS', 'Top Seller'),
    #     ('NR', 'New Releases'),
    #     ('UC', 'Upcoming Releases')
    # ]
    # category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='')

