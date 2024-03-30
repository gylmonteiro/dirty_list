from django import forms
from .models import Faction, Incident


class FactionForm(forms.ModelForm):
    class Meta:
        model = Faction
        fields = '__all__'


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = (
            "type_incident",
            "title",
            "location",
            "reported_at",
            "involved",
            "details",
        )
        widgets = {
            "type_incident": forms.Select(attrs={"class": "form-select"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "reported_at": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "involved": forms.SelectMultiple(attrs={"class": "form-select"}),
            "details": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
        }
