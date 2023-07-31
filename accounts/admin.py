from django.contrib import admin
from accounts.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'email', 'username', 'is_active', 'is_staff']
    search_fields = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
