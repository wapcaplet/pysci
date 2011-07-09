PySci
=================================

This module attempts to provide a more Pythonic interface to the QsciScintilla_
editor widget.

.. _QsciScintilla: http://www.riverbankcomputing.co.uk/static/Docs/QScintilla2/classQsciScintilla.html


Installation
-----------------------

To install::

    $ python setup.py install

or::

    $ pip install .

Usage
-----------------------

Here's a very simple PyQt4 application using the PySci editor widget::

    from PyQt4 import QtGui
    from pysci import PySci

    if __name__ == '__main__':
        app = QtGui.QApplication([])
        editor = PySci()
        editor.show()
        app.exec_()

See the ``demo.py`` file in the root of the repository for a more complete
example, including the use of the ``PySciSettings`` configuration widget.


Contents
-----------------------

.. toctree::
    :maxdepth: 2

    motivation
    api/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

