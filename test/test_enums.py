from pysci.enums import enum_value, BadEnum
from unittest import TestCase
from PyQt4 import Qsci

class EnumTest (TestCase):
    def test_valid_enums(self):
        QS = Qsci.QsciScintilla
        self.assertEqual(enum_value('WsInvisible'), QS.WsInvisible)
        self.assertEqual(enum_value('TextMargin'), QS.TextMargin)

    def test_bad_enums(self):
        self.assertRaises(BadEnum, enum_value, 'NoSuchEnum')
        self.assertRaises(BadEnum, enum_value, '')

