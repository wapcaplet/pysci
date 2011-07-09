from pysci.editor import PySci
from pysci.settings import PySciSettings
from unittest import TestCase
from PyQt4 import QtGui

class PySciSettingsTest (TestCase):
    """Test the PySciSettings widget.
    """
    def test_instantiation(self):
        """Instantiate an PySciSettings widget.
        """
        self.app = QtGui.QApplication(['-nograb', '-sync'])
        self.editor = PySci()
        self.config = PySciSettings(self.editor)
        self.app.quit()

