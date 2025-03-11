from django.contrib import admin
from .models import Module

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'status', 'installed_at', 'repository')