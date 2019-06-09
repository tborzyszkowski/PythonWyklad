from django.contrib import admin

# Register your models here.

from .models import Question, Translation


admin.site.register(Question)
admin.site.register(Translation)