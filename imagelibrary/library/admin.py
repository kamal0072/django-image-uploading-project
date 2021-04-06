from django.contrib import admin
from .models import UserImage

@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display=['id','pics','date']    
