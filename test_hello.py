# Importamos a biblioteca de testes
import unittest


from hello import app


class TestHello(unittest.TestCase):
    """Testes para hello.py"""

    def setUp(self):
        app = app.test_client()
        self.response = app.get('/')

   # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # Testamos se a nossa home retorna a string "Test TDD"
    def test_html_string_response(self):
        self.assertEqual("Test TDD", self.response.data.decode('utf-8'))

    # Testamos se o content_type da resposta da home esta correto
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)        