from django.contrib import admin
from .models import Faction, Incident
# Register your models here.


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title',)
