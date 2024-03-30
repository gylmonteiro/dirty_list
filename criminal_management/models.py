from django.db import models
from persons.models import Person
from .constants_choices import INCIDENT_TYPES


class Faction(models.Model):
    name = models.CharField(max_length=255, unique=True)
    member = models.ManyToManyField(Person, related_name='members', blank=True)
    leaders = models.ManyToManyField(Person, blank=True, related_name='leaders')
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Incident(models.Model):
    type_incident = models.CharField(max_length=100, choices=INCIDENT_TYPES, blank=True, null=True, verbose_name='Tipo de ocorrência')
    title = models.CharField(max_length=255, verbose_name='Título')
    location = models.CharField(max_length=100, verbose_name='Local')
    reported_at = models.DateField(blank=True, null=True, verbose_name='Data da ocorrência')
    person_relation = models.ForeignKey(Person, blank=True, null=True, related_name='incident', on_delete=models.SET_NULL)
    involved = models.ManyToManyField(Person, blank=True, related_name="involved_persons", verbose_name='Pessoas envolvidas')
    details = models.TextField(blank=True, null=True, verbose_name='Detalhes da ocorrência')

    def __str__(self):
        return self.title
