from django.db import models


class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    creation = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=20, default="(00)000-000-000")
    formacao = models.ForeignKey('Formacao',
                                 on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    cod = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
