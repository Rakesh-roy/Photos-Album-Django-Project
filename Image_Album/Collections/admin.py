from django.contrib import admin
from Collections import models


admin.site.register(models.AlbumModel)

class AulbumAdmin(admin.ModelAdmin):
    fields = ['image', 'uploaded_time']
