from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . models import *
from . serializer import *
    
@api_view(['GET'])
def get_all_products(request):
    product = Product.objects.all().values()
    serializer = ProductSerialzer(product, many=True)
    return Response(serializer.data)




