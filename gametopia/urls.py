
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', include('Products.urls')),
    path('api/user/', include('Users.urls')),
]
