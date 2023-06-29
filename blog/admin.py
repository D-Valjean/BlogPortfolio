from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Post)
class Apost(admin.ModelAdmin):
    list_display = ('title','date')