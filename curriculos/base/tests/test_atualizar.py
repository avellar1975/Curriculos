import pytest
from django.urls import reverse
from curriculos.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:alterar'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_alterar_link(resp):
    assert_contains(resp, f'href="{reverse("base:alterar")}">Atualizar</a>')
