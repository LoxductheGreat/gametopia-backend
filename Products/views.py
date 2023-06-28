from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response


# Create your views here.

class ProductView(APIView):
    def get(self, request):
        output = [{'name': output.name}
                  for output in Product.objects.all()]
        return Response(output)


