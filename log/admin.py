from django.contrib import admin
from log.models import Log

# Register your models here.

class LogAdmin(admin.ModelAdmin):
    list_diplay = ('id', 'log', 'created_by')

admin.site.register(Log, LogAdmin)