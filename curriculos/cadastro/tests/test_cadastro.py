# Core Django imports
from django.test import TestCase

# Third-party app imports
from model_bakery import baker

from curriculos.cadastro.models import Pessoa, Formacao


class PessoasTestModel(TestCase):
    """
    Class to test the model Customer
    """

    def setUp(self):
        """Set up test class."""
        self.pessoa = baker.make(Pessoa)
        self.formacao = baker.make(Formacao)

    def test_using_customer(self):
        """Test function using baked model."""
        self.assertIsInstance(self.pessoa, Pessoa)
        self.assertIsInstance(self.formacao, Formacao)
