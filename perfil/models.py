from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError


class Perfil(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE)
    idade = models.IntegerField()
    data_cascimento = models.DateField()
    endereco = models.CharField(max_length=55)
    telefone = models.CharField(max_length=15)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    provincia = models.CharField(
        max_length=1,
        default='L',
        choices=[
            ('L', 'Luanda'),
            ('U', 'Uige'),
            ('U', 'Huambo'),
            ('B', 'Benguela'),
            ('C', 'Cabinda'),
        ]
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def clean(self):
        raise ValidationError({
            'idade': 'bla bla bla'
        })