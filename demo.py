#! /usr/bin/env python
# demo.py

"""Demonstration of the PySci editor and configuration window.
"""

import sys
from pysci.editor import PySci
from pysci.config import EditorSettings
from PyQt4 import QtGui, QtCore

class Demo (QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle("PySci demo")

        self.editor = PySci(self)

        self._create_menubar()


    def _create_menubar(self):
        """Create the application menu bar.
        """
        menubar = self.menuBar()
        quit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Quit', self)
        quit.setShortcut('Ctrl+Q')
        self.connect(quit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        menubar.addAction(quit)
        menubar.addAction('&Configure', self.configure)

        self.setCentralWidget(self.editor)


    def configure(self):
        """Display the editor configuration window.
        """
        settings = EditorSettings(self.editor)
        settings.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Demo()
    win.show()
    sys.exit(app.exec_())


