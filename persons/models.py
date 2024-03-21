import uuid
from django.db import models
from .persons_validator import validator_cpf



class Person(models.Model):
    name = models.CharField(max_length=255)
    number_register = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    cpf = models.CharField(max_length=11, blank=True, null=True, validators=[validator_cpf], default='')

    def __str__(self):
        return f'{self.name} - id: {self.number_register.hex}'

    class Meta:
        ordering = ['name']
