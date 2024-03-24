from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person-list'),
    path('create/', views.PersonCreateView.as_view(), name='person-create')
]
