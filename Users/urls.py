
from django.urls import path
from . import views

urlpatterns = [
   # path('/', login.as_view(), name='product')
   path('login', views.login),
   path('signup', views.signup),
   path('logout', views.logout),
]
