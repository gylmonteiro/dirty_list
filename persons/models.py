import uuid
from django.db import models
from .persons_validator import validator_cpf
from .constants_choices import CHOICE_STATE, CHOICE_RELATION


class Address(models.Model):
    state = models.CharField(max_length=2, choices=CHOICE_STATE)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    distric = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.state} | {self.city} | {self.street}'

    class Meta:
        ordering = ['city']


class Person(models.Model):
    name = models.CharField(max_length=255)
    number_register = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    cpf = models.CharField(max_length=11, blank=True, null=True, validators=[validator_cpf], default='')
    address = models.ForeignKey(Address, null=True, blank=True, related_name='persons', on_delete=models.SET_NULL)
    person_relations = models.ManyToManyField(
        "Relationship", related_name="person_relationships", blank=True
    )

    def __str__(self):
        return f'{self.name} - id: {self.number_register.hex}'

    class Meta:
        ordering = ['name']


class Relationship(models.Model):
    type_relation = models.CharField(max_length=30, choices=CHOICE_RELATION)
    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        related_name="person_relation",
    )
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.person} é {self.type_relation}'
