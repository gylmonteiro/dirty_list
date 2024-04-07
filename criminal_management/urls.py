from django.urls import path
from . import views


urlpatterns = [
    path('factions/', views.FactionListView.as_view(), name='faction-list'),
    path('factions/<int:pk>', views.FactionDetailView.as_view(), name='faction-detail'),
    path('create/', views.FactionCreateView.as_view(), name='faction-create'),
    path('select/', views.FactionSelectView.as_view(), name='select-faction'),
    path('add_member/', views.FactionSelectView.as_view(), name='add-member'),
    path('registration_incident/', views.RegisterIncident.as_view(), name='registration-incident'),
    path('detail_incident/<int:pk>', views.IncidentDetailView.as_view(), name='detail-incident'),
    path('delete_incident/<int:pk>', views.IncidentDeleteView.as_view(), name='delete-incident'),
    path('update_incident/<int:pk>', views.IncidentUpdateView.as_view(), name='update-incident')
]
