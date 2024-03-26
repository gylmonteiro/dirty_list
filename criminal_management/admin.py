from django.contrib import admin
from .models import Faction
# Register your models here.


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    list_display = ('name',)
