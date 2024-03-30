import uuid
from datetime import date
from django.db import models
from .persons_validator import validator_cpf
from .constants_choices import CHOICE_STATE, CHOICE_RELATION


class Address(models.Model):
    state = models.CharField(max_length=2, choices=CHOICE_STATE, verbose_name="Estado")
    city = models.CharField(max_length=255, verbose_name="Cidade")
    street = models.CharField(max_length=255, verbose_name="Rua")
    number = models.CharField(max_length=100, verbose_name="Número")
    district = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bairro")
    zip_code = models.CharField(max_length=100, blank=True, null=True, verbose_name="CEP")
    reference_point = models.TextField(null=True, blank=True, verbose_name="Ponto de Referência")

    def __str__(self):
        return f'{self.state} | {self.city} | {self.street}'

    class Meta:
        ordering = ['city']


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome Completo")
    nickname = models.CharField(max_length=255, verbose_name="Alcunha | Apelido", null=True, blank=True)
    number_register = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    cpf = models.CharField(max_length=11, blank=True, null=True, validators=[validator_cpf], default='')
    date_birthday = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    address = models.ForeignKey(Address, null=True, blank=True, related_name='persons', on_delete=models.SET_NULL, verbose_name="Endereço")
    person_relations = models.ManyToManyField(
        "Relationship", related_name="person_relationships", blank=True
    )
    comments = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def age(self):
        if self.date_birthday:
            today = date.today()
            age_now = today.year - self.date_birthday.year - ((today.month, today.day) < (self.date_birthday.month, self.date_birthday.day))
            return age_now
        else:
            return None


class Relationship(models.Model):
    type_relation = models.CharField(max_length=30, choices=CHOICE_RELATION, verbose_name="Tipo da relação")
    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        related_name="person_relation",
        verbose_name="Pessoa"
    )
    observation = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return f'{self.person} é {self.type_relation}'
