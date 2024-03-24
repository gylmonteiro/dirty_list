from django.http import Http404
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, DetailView
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
    template_name = 'create_person.html'
    success_url = '/persons/'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'detail_person.html'
    context_object_name = 'person'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            return redirect('person-list')