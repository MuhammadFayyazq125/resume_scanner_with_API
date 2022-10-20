from django.shortcuts import render
from resumes.models import  ResumeScan
from rest_framework import status,generics
from .serializers import resumescanserializer
from rest_framework.permissions import IsAdminUser

# Create your views here.
class resumeList(generics.ListCreateAPIView):
    # postObjects is used for getting published data
    permission_classes = [IsAdminUser]
    queryset = ResumeScan.objects.all()
    serializer_class = resumescanserializer

    
# generic.RetrieveDestroyAPIView Retrieve means to get any individual item and destroy means to delete item
class resumeDetails(generics.RetrieveAPIView):
    queryset = ResumeScan.objects.all()
    serializer_class = resumescanserializer