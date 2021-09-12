from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('asset_name', 'asset_description', 'asset_owner')

         