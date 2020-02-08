# Importamos a biblioteca de testes
import unittest


from hello import app


class TestHello(unittest.TestCase):
    """Testes para hello.py"""

    def setUp(self):
        tdd = app.test_client()
        self.response = tdd.get('/debian')

   # Testamos se a resposta e 302 ("redirecionamento")
    def test_get(self):
        self.assertEqual(302, self.response.status_code)