from django.contrib import admin

from .models import Track

@admin.register(Track)
class MyModelAdmin(admin.ModelAdmin):
     def has_add_permission(self, request):
        return False
