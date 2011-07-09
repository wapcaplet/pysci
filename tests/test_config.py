from pysci.editor import PySci
from pysci.config import EditorSettings
from unittest import TestCase
from PyQt4 import QtGui

class EditorSettingsTest (TestCase):
    """Test the EditorSettings widget.
    """
    def test_instantiation(self):
        """Instantiate an EditorSettings widget.
        """
        self.app = QtGui.QApplication(['-nograb', '-sync'])
        self.editor = PySci()
        self.config = EditorSettings(self.editor)
        self.app.quit()

