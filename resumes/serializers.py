from django.db import models
from rest_framework import serializers
from .models import ResumeScan
from django.db.models import fields
from rest_framework import routers, serializers, viewsets

# class resumescanserializer(serializers.ModelSerializer):
#     class Meta:
#         fields=('id','resume','job','expected_score','outputs','ip','created_at')
#         model=ResumeScan
    # permissions = None


class resumescanserializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','resume','job','expected_score','outputs','ip','created_at')
        model = ResumeScan