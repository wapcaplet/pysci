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

If you'd like to make use of the configuration settings widget, connect an event
handler to a button or menu entry, then instantiate ``PySciSettings``, passing
it your ``PySci`` editor instance::

    from pysci import PySciSettings
    settings = PySciSettings(editor)

Here's an example of what it looks like:

.. image:: /images/pysci_settings.png

All changes to configuration settings in this widget take effect in realtime in
your editor window.

