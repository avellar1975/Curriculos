from curriculos.django_assertions import assert_contains
import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp):
    assert_contains(resp, '<title>Currículos</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Currículos</a>')
