from rest_framework import serializers
from .models import *

class ProductSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'brand_name', 'genre', 'developer', 'publisher']