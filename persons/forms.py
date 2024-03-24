from django import forms
from .models import Person, Relationship


class PersonCreateModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'cpf']

class RelationPersonCreateModelForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = '__all__'