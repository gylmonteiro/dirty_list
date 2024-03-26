from django.db import models
from persons.models import Person


class Faction(models.Model):
    name = models.CharField(max_length=255, unique=True)
    member = models.ManyToManyField(Person, related_name='members', blank=True)
    leaders = models.ManyToManyField(Person, blank=True, related_name='leaders')
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Incident(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    reported_at = models.DateField(blank=True)
    person_relation = models.ForeignKey(Person, blank=True, null=True, related_name='incident', on_delete=models.SET_NULL)
    involved = models.ManyToManyField(Person, blank=True, related_name="involved_persons")

    def __str__(self):
        return self.title
    