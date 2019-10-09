from django.contrib import admin

from blog import models


@admin.register(models.FileUpload)
class BlogAdmin(admin.ModelAdmin):
    pass
