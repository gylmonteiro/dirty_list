# from django.shortcuts import render
from django.views.generic import CreateView, ListView
from persons.models import Person
from persons.forms import PersonCreateModelForm
# Create your views here.


class PersonListView(ListView):
    model = Person
    template_name = 'list_persons.html'
    context_object_name = 'persons'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonCreateModelForm
    template_name = 'create_persons.html'
    success_url = '/list_persons.html/'
