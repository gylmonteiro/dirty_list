from django import forms
from .models import Person

class PersonCreateModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'cpf']

