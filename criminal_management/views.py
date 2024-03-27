from django.shortcuts import redirect
from django.views import generic
from .models import Faction, Incident
from persons.models import Person
from .forms import FactionForm, IncidentForm
# Create your views here.


class FactionCreateView(generic.CreateView):
    model = Faction
    form_class = FactionForm
    template_name = 'create_faction.html'
    success_url = '/persons/'


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
        # if request.POST.get('leader or member') -> criar a lógica internamente para saber se é um leader ou somente um member

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


'''
class FactionUpdateView(generic.View):

    def post(self,request, *args, **kwargs):
        faction_id = request.POST.get('faction')
        person_id = request.POST.get('person')
        faction = Faction.objects.get(pk=faction_id)
        person = Person.objects.get(pk=person_id)
        faction.member.add(person)
        return redirect("person-list")
'''
