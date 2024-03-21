from django.core.exceptions import ValidationError
from validate_docbr import CPF

cpf = CPF()


def validator_cpf(value):
    print(value)
    if not cpf.validate(value):
        raise ValidationError('CPF é inválido')
