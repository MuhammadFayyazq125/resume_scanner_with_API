from os import name
from django.urls import path
from . import views
# from .views import UserViewSet
from .models import ResumeScan
from rest_framework import routers
from django.conf.urls import include

urlpatterns = [
    path('', views.index),
    path('scan/', views.scan),
    path('health/', views.health),
    
]

# urlpatterns += router.urls