import json
from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from persons.models import Person, Relationship, Address
from criminal_management.models import Incident, Faction
from persons.forms import PersonCreateModelForm, RelationPersonCreateModelForm, AddressCreateModelForm
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        incident = Incident.objects.all()
        factions = Faction.objects.all()
        labels = []
        values_labels = []
        for label in incident:
            if label.get_type_incident_display() not in labels:
                labels.append(label.get_type_incident_display())
                values_labels.append(Incident.objects.filter(type_incident=label.type_incident).count())
        context['factions'] = factions
        context['incident'] = incident
        context["values_labels"] = json.dumps(values_labels)
        context["labels"] = json.dumps(labels)
        return context


class PersonListView(generic.ListView):
    model = Person
    template_name = 'list_persons.html'
    context_object_name = 'persons'


class PersonCreateView(generic.CreateView):
    model = Person
    form_class = PersonCreateModelForm
    template_name = 'create_person.html'
    success_url = '/persons/'


class PersonUpdateView(generic.UpdateView):
    model = Person
    form_class = PersonCreateModelForm
    template_name = 'update_person.html'
    success_url = '/persons/'
    context_object_name = 'person'


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'detail_person.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = self.object
        involved_incidents = Incident.objects.filter(involved=person)
        context["involved_incidents"] = involved_incidents
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            return redirect('person-list')


class PersonDeleteView(generic.DeleteView):
    model = Person
    success_url = '/persons/'

class RelationPersonCreateView(generic.CreateView):
    model = Relationship
    form_class = RelationPersonCreateModelForm
    template_name = 'create_relation.html'
    # success_url = '/persons/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person_id = self.request.GET.get("id_person")
        person = Person.objects.get(pk=person_id)
        context["person_id"] = person_id
        context["person"] = person

        return context

    def form_valid(self, form):
        person_id = self.request.POST.get('id_person')
        person = Person.objects.get(pk=person_id)
        relationship = form.save()
        person.person_relations.add(relationship)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        person_id = self.request.POST.get('id_person')
        return reverse_lazy("person-detail", kwargs={'pk': person_id})


class AddressCreateView(generic.CreateView):
    model = Address
    form_class = AddressCreateModelForm
    template_name = 'create_address.html'
    # success_url = '/persons/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person_id = self.request.GET.get("id_person")
        context["person_id"] = person_id
        return context

    def form_valid(self, form):
        person_id = self.request.POST.get('person')
        print(person_id)
        person = Person.objects.get(pk=person_id)
        address = form.save()
        person.address = address
        person.save()
        return super().form_valid(form)

    def get_success_url(self):
        person_id = self.request.POST.get("person")
        return reverse_lazy("person-detail", kwargs={"pk": person_id})
