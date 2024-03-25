from typing import Any
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView
from persons.models import Person, Relationship
from persons.forms import PersonCreateModelForm, RelationPersonCreateModelForm
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


class RelationPersonCreateView(CreateView):
    model = Relationship
    form_class = RelationPersonCreateModelForm
    template_name = 'create_relation.html'
    success_url = '/persons/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person_id = self.request.GET.get("id_person")
        context["person_id"] = person_id
        return context
    
    def form_valid(self, form):
        person_id = self.request.POST.get('id_person')
        person = Person.objects.get(pk=person_id)
        relationship = form.save()
        person.person_relations.add(relationship)
        return super().form_valid(form)
