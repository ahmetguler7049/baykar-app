from django.contrib import admin
from .models import Team, Part, Aircraft, AircraftInventory, PartInventory


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'aircraft', 'team')
    search_fields = ('name', 'aircraft__name', 'team__name')
    list_filter = ('aircraft', 'team')

class AircraftAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class AircraftInventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'aircraft', 'team', 'created_at')
    search_fields = ('name', 'aircraft__name', 'team__name')
    list_filter = ('aircraft', 'team')

class PartInventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'aircraft', 'team', 'part', 'is_used', 'created_at', 'used_at')
    search_fields = ('name', 'aircraft__name', 'team__name', 'part__name')
    list_filter = ('aircraft', 'team', 'is_used')

admin.site.register(Team, TeamAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(AircraftInventory, AircraftInventoryAdmin)
admin.site.register(PartInventory, PartInventoryAdmin)
