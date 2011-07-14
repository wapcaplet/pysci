from pysci.enums import enum_value, enum_string, BadEnum
from unittest import TestCase
from PyQt4 import Qsci

class EnumTest (TestCase):
    def test_enum_value(self):
        """Convert enumeration name to correct value.
        """
        QS = Qsci.QsciScintilla
        self.assertEqual(enum_value('WsInvisible'), QS.WsInvisible)
        self.assertEqual(enum_value('TextMargin'), QS.TextMargin)


    def test_enum_string(self):
        """Convert enumeration value to string name.
        """
        QS = Qsci.QsciScintilla
        self.assertEqual(enum_string(QS.WsInvisible), 'WsInvisible')
        self.assertEqual(enum_string(QS.TextMargin), 'TextMargin')


    def test_bad_enum_name(self):
        """Raise exception on bad enumeration name or value.
        """
        self.assertRaises(BadEnum, enum_value, 'NoSuchEnum')
        self.assertRaises(BadEnum, enum_value, '')
        self.assertRaises(BadEnum, enum_string, 0)
        self.assertRaises(BadEnum, enum_string, 1)


