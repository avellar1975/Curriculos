from django.db import models


class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
