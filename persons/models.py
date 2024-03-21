import uuid
from django.db import models
from .persons_validator import validator_cpf
from .constants_choices import CHOICE_STATE


class Address(models.Model):
    state = models.CharField(max_length=2, choices=CHOICE_STATE)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    distric = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.state} | {self.city} | {self.street}'

    class Meta:
        ordering = ['city']


class Person(models.Model):
    name = models.CharField(max_length=255)
    number_register = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    cpf = models.CharField(max_length=11, blank=True, null=True, validators=[validator_cpf], default='')
    address = models.ForeignKey(Address, null=True, blank=True, related_name='persons', on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} - id: {self.number_register.hex}'

    class Meta:
        ordering = ['name']
