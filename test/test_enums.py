from pysci.enums import enum_value, enum_help, BadEnum
from unittest import TestCase
from PyQt4 import Qsci

class EnumTest (TestCase):
    def test_enum_value(self):
        QS = Qsci.QsciScintilla
        self.assertEqual(enum_value('WsInvisible'), QS.WsInvisible)
        self.assertEqual(enum_value('TextMargin'), QS.TextMargin)


    def test_bad_enum_value(self):
        self.assertRaises(BadEnum, enum_value, 'NoSuchEnum')
        self.assertRaises(BadEnum, enum_value, '')


    def test_enum_help(self):
        self.assertEqual(
            enum_help('AiMaintain'),
            "A line is automatically indented to match the previous line.")
        self.assertEqual(
            enum_help('AnnotationHidden'),
            "Annotations are not displayed.")


    def test_bad_enum_help(self):
        self.assertRaises(BadEnum, enum_help, 'NoSuchEnum')
        self.assertRaises(BadEnum, enum_help, '')

