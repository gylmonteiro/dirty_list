from django import forms
from .models import Faction

class FactionForm(forms.ModelForm):
    class Meta:
        model = Faction
        fields = '__all__'