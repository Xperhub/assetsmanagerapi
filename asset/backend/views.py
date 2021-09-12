from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Asset
from backend.serializers import AssetSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    #permission_classes = [IsAdminUser]


class AssetRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    #permission_classes = [IsAdminUser]
    


