from django.urls import path
from . import views


urlpatterns = [
    path('', views.FactionCreateView.as_view(), name='faction-create'),
    path('select/', views.FactionSelectView.as_view(), name='select-faction'),
    path('add_member/', views.FactionSelectView.as_view(), name='add-member'),
    path('registration_incident/', views.RegisterIncident.as_view(), name='registration-incident'),
]
