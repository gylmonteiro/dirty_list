from django import forms
from .models import Faction, Incident


class FactionForm(forms.ModelForm):
    class Meta:
        model = Faction
        fields = '__all__'


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ('title', 'location', 'reported_at', 'involved', 'details')