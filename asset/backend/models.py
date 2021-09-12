from django.db import models
from dry_rest_permissions.generics import allow_staff_or_superuser, authenticated_users
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Asset(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    asset_name = models.CharField(max_length =150)
    asset_description = models.CharField(max_length = 150)
    asset_owner = models.CharField(max_length = 150)
    created_by = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    @staticmethod
    @authenticated_users
    def has_publish_permission(request):
        return True
      
    @allow_staff_or_superuser
    def has_object_publish_permission(self, request):
        return request.user == self.owner

    
    

# Create your models here.
