from django.contrib import admin
from .models import Spacecraft, Target, Mission, Instrument, MissionInstrument


@admin.register(Spacecraft)
class SpacecraftAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'launch_date', 'status']
    list_filter = ['status', 'country']
    search_fields = ['name']


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'diameter_km', 'has_ocean']
    list_filter = ['type', 'has_ocean']
    search_fields = ['name']


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'mission_name', 'spacecraft', 'target', 'start_date', 'status']
    list_filter = ['status', 'target']
    search_fields = ['mission_name']


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'mass_kg', 'power_consumption_w']
    list_filter = ['type']
    search_fields = ['name']


@admin.register(MissionInstrument)
class MissionInstrumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'mission', 'instrument', 'is_active', 'commissioning_date']
    list_filter = ['is_active']