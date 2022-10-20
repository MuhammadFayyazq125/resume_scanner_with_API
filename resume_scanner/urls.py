"""resume_scanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
# from django.urls import path
from django.conf.urls import include, url
from django.urls.conf import path
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
# from resumes.views import UserViewSet
# router = routers.DefaultRouter()
# router.register(r'api', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resumescanner/', include('resumes.urls')),
    path('health/', include('health.urls')),
    path('resumeapi/', include('resumeapi.urls'))
    # url('', include(router.urls)),
    # url('', include('rest_framework.urls', namespace='rest_framework')),
    # url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
