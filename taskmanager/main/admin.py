from django.contrib import admin
from .models import Photos
# Register your models here.


class PhotosAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Photos, PhotosAdmin)

