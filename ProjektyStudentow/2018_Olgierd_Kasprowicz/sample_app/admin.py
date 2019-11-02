from django.contrib import admin
from .models import Command, MachineType, Machine


class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ('slug', 'cpu_count', 'gpu_count', 'memory', 'disk_space', 'description')


admin.site.register(Command)
admin.site.register(Machine)
admin.site.register(MachineType, MachineTypeAdmin)
