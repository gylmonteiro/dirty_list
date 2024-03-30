from django.contrib import admin
from .models import Person, Address, Relationship
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('type_relation', 'person', 'observation',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('state', 'city', 'street', 'number', 'district', 'zip_code')
