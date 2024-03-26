from django.views import generic
from .models import Faction
from .forms import FactionForm
# Create your views here.

class FactionCreateView(generic.CreateView):
    model = Faction
    form_class = FactionForm
    template_name = 'create_faction.html'
    success_url = '/persons/'
