from unittest import TestCase
from pysci.language import guess_language

class LanguageTest (TestCase):
    def test_guess_language(self):
        """Language is correctly inferred from filename extension.
        """
        self.assertEqual(guess_language('foo.py'), 'Python')
        self.assertEqual(guess_language('foo.rb'), 'Ruby')
        self.assertEqual(guess_language('foo.yaml'), 'YAML')
        self.assertEqual(guess_language('foo.css'), 'CSS')
        self.assertEqual(guess_language('foo.cpp'), 'CPP')
        self.assertEqual(guess_language('foo.h'), 'CPP')

        self.assertEqual(guess_language('foo.txt'), 'None')
        self.assertEqual(guess_language('foo.unknown'), 'None')

