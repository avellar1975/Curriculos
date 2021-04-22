from django.contrib.admin import ModelAdmin, register
from curriculos.cadastro.models import Pessoa, Formacao


@register(Pessoa)
class PessoaAdmin(ModelAdmin):
    list_display = ('nome', 'creation')
    ordering = ('nome',)


@register(Formacao)
class FormacaoAdmin(ModelAdmin):
    list_display = ('cod', 'nome')
    ordering = ('cod',)
