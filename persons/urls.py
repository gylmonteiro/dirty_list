from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person-list'),
    path('create/', views.PersonCreateView.as_view(), name='person-create'),
    path('<int:pk>/', views.PersonDetailView.as_view(), name='person-detail'),
    path('relation/', views.RelationPersonCreateView.as_view(), name='relation-persons-create'),
    path('address/', views.AddressCreateView.as_view(), name='address-create'),
]
