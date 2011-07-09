Usage
=================================

Here's a very simple PyQt4 application using the PySci editor widget::

    from PyQt4 import QtGui
    from pysci import PySci

    if __name__ == '__main__':
        app = QtGui.QApplication([])
        editor = PySci()
        editor.show()
        app.exec_()

The ``PySci`` widget is a subclass of QsciScintilla_, so you can use it in
all the same ways you would normally use that widget. For some of the additional
features it provides, read on.

.. _QsciScintilla: http://www.riverbankcomputing.co.uk/static/Docs/QScintilla2/classQsciScintilla.html


Configuration
-----------------------------

QsciScintilla makes heavy use of enumerated types with individual getters and
setters for configuration settings. ``PySci`` borrows a more Pythonic approach
from Tkinter_, with the following features:

- Arbitrary configuration settings are accepted by the widget constructor
- Multiple settings can be configured with a single method call
- Plain strings can be used instead of enumerated types

For example, with QSciScintilla alone you might need six lines of code to create
an editor widget and configure it the way you want::

    editor = QsciScintilla()
    editor.setWhitespaceVisibility(QsciScintilla.WsInvisible)
    editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
    editor.setWrapMode(QsciScintilla.WrapWord)
    editor.setTabIndents(True)
    editor.setTabWidth(4)

With ``PySci``, this can be condensed into a single constructor call::

    editor = PySci(
        whitespaceVisibility = 'WsInvisible',
        braceMatching = 'SloppyBraceMatch',
        wrapMode = 'WrapWord',
        tabIndents = True,
        tabWidth = 4)

Additional configuration changes can be made via the ``configure`` method::

    editor.configure(
        indentationGuides = True,
        eolVisibility = True,
        edgeColumn = 72)

You can also get or set individual configurations by passing their name as a
string to the ``get_config`` or ``set_config`` methods::

    eol_mode = editor.get_config('eolMode')
    editor.set_config('eolMode', 'EolMac')

This can be useful if you have setting names in variables.

.. _Tkinter: http://www.pythonware.com/library/tkinter/introduction/widget-configuration.htm


Settings Widget
-----------------------------

Considering the enormous number of methods in QsciScintilla for dealing with
configuration settings, it's a little surprising that a dedicated configuration
widget is not provided. If you've worked with QsciScintilla with any seriousness,
you've probably build an ad-hoc configuration widget yourself (and so has
everyone else). That's a shameful duplication of programming effort. PySci
provides a ready-made one called ``PySciSettings`` to save you the trouble.

Here's an example of what it looks like:

.. image:: /images/pysci_settings.png

To use it, connect an event handler to a button or menu entry, then instantiate
``PySciSettings``, passing it your ``PySci`` editor instance::

    from pysci import PySciSettings
    settings = PySciSettings(editor)

All changes to configuration settings in this widget take effect in realtime in
the associated ``PySci`` widget.

