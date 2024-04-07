from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("persons/", views.PersonListView.as_view(), name="person-list"),
    path("persons/update/<int:pk>/", views.PersonUpdateView.as_view(), name="person-update"),
    path("persons/create/", views.PersonCreateView.as_view(), name="person-create"),
    path("persons/delete/<int:pk>", views.PersonDeleteView.as_view(), name='person-delete'),
    path("persons/<int:pk>/", views.PersonDetailView.as_view(), name="person-detail"),
    path(
        "persons/relation/",
        views.RelationPersonCreateView.as_view(),
        name="relation-persons-create",
    ),
    path("persons/address/", views.AddressCreateView.as_view(), name="address-create"),
]
