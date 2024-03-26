from django.db import models
from persons.models import Person


class Faction(models.Model):
    name = models.CharField(max_length=255, unique=True)
    member = models.ManyToManyField(Person, related_name='members', blank=True)
    leaders = models.ManyToManyField(Person, blank=True, related_name='leaders')
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
