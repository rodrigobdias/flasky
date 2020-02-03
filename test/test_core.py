# Importamos a biblioteca de testes
import unittest


from src.hello_test import get_format_name


class NamesTestCase(unittest.TestCase):
    """Testes para hello_test.py"""

    def test_first_last_name(self):
        """Nome como 'Janis Joplin' funcionam?"""
        formated_name = get_format_name('janis', 'joplin')
        self.assertEqual(formated_name, 'Janis Joplin')

    unittest.main()