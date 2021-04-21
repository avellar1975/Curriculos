from django.contrib.admin import ModelAdmin, register
from curriculos.cadastro.models import Pessoa


@register(Pessoa)
class PessoaAdmin(ModelAdmin):
    list_display = ('nome', 'creation')
    ordering = ('nome',)
