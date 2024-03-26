from django import forms
from .models import Person, Relationship, Address


class PersonCreateModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'cpf']


class RelationPersonCreateModelForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = '__all__'


class AddressCreateModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
