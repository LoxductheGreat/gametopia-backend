from django.contrib import admin
from django.urls import path
from Products.views import *

urlpatterns = [
   path('', ProductView.as_view(), name='product')
]
