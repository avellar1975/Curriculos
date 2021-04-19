"""test_cadastro.py."""
from curriculos.django_assertions import assert_contains
import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_consultar_link(resp):
    assert_contains(resp, f'href="{reverse("base:consultar")}">Consultar</a>')


def test_cadastrar_link(resp):
    assert_contains(resp, f'href="{reverse("base:cadastrar")}">Cadastrar</a>')


def test_alterar_link(resp):
    assert_contains(resp, f'href="{reverse("base:alterar")}">Atualizar</a>')
