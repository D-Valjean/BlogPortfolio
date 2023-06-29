from django.contrib import admin
from . import models
# Register your models here.



@admin.register(models.Project)
class AProject(admin.ModelAdmin):
    list_display = ('title',)