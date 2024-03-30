from django import forms
from .models import Person, Relationship, Address


class PersonCreateModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'nickname', 'date_birthday', 'cpf']
        widgets = {
            "date_birthday": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "nickname": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
        }


class RelationPersonCreateModelForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = ['type_relation', 'person', 'observation']
        widgets = {
            'type_relation': forms.Select(attrs={'class': 'form-select'}),
            'person': forms.Select(attrs={'class': 'form-select'}),
            'observation': forms.Textarea(attrs={'class': 'form-control'})
        }


class AddressCreateModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['state', 'city', 'street', 'number', 'district', 'zip_code', 'reference_point']
        widgets = {
            "state": forms.Select(attrs={"class": "form-select"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "street": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control"}),
            "reference_point": forms.Textarea(attrs={"class": "form-control", "rows": "4"}),
        }
