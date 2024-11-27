from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'team', 'is_active', 'is_staff')
    search_fields = ('email',)
    list_filter = ('team', 'is_active', 'is_staff')

admin.site.register(User, UserAdmin)
