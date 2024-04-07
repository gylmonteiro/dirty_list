from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Faction, Incident
from persons.models import Person
from .forms import FactionForm, IncidentForm
# Create your views here.


class FactionCreateView(generic.CreateView):
    model = Faction
    form_class = FactionForm
    template_name = 'create_faction.html'
    success_url = '/criminals/factions/'


class FactionListView(generic.ListView):
    model = Faction
    template_name = 'list_factions.html'
    context_object_name = 'factions'

class FactionSelectView(generic.TemplateView):
    template_name = 'select_factions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person_id = self.request.GET.get("id_person")
        factions = Faction.objects.all()
        person = Person.objects.get(pk=person_id)
        context["person"] = person
        context["factions"] = factions
        return context

    def post(self, request, *args, **kwargs):
        leader = request.POST.get("leader")
        faction_id = request.POST.get("faction")
        person_id = request.POST.get("person")
        faction = Faction.objects.get(pk=faction_id)
        person = Person.objects.get(pk=person_id)

        if leader == "is_leader":
            faction.leaders.add(person)
            return redirect("person-list")
        else:
            faction.member.add(person)
            return redirect("person-list")


class FactionDetailView(generic.DetailView):
    model = Faction
    template_name = 'detail_faction.html'
    context_object_name = 'faction'


class RegisterIncident(generic.CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = "registration_incident.html"
    success_url = "/persons/"

    def get_context_data(self, **kwargs):
        person_id = self.request.GET.get("id_person")
        person = Person.objects.get(pk=person_id)
        context = super().get_context_data(**kwargs)
        context['person'] = person
        return context

    def form_valid(self, form):
        person_id = self.request.POST.get('person')
        person = Person.objects.get(pk=person_id)
        incident_form = form.save()
        incident_form.person_relation = person
        incident_form.save()

        return super().form_valid(form)


class IncidentDetailView(generic.DetailView):
    model = Incident
    template_name = 'incident_detail.html'
    context_object_name = 'incident'


class IncidentDeleteView(generic.DeleteView):
    model = Incident

    def get_success_url(self):
        return reverse_lazy(
            "person-detail", kwargs={"pk": self.object.person_relation.id}
        )


class IncidentUpdateView(generic.UpdateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'update_incident.html'
    context_object_name = 'incident'

    def get_success_url(self):
        return reverse_lazy(
            "person-detail", kwargs={"pk": self.object.person_relation.id}
        )
