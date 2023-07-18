from rest_framework import serializers
from . models import *

class ProductSerialzer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ['id', 'name', 'brand_name', 'genre', 'developer', 'publisher','release_date']
        extra_kwargs = {'release_date':{'format': '%d-%b-%Y'}}

