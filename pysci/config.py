# config.py

__all__ = [
    'EditorSettings',
]

from PyQt4 import QtCore, QtGui

class EditorSettings (QtGui.QDialog):
    """A dialog window for configuring a QsciScintilla editor.
    """
    def __init__(self, editor):
        QtGui.QDialog.__init__(self, editor)
        self.editor = editor

        self.setWindowTitle('Noodle settings')

        layout = QtGui.QVBoxLayout()

        # Checkboxes for each boolean setting
        for setting in self._bool_settings:
            layout.addWidget(self._create_checkbox(setting))

        # OK button
        ok = QtGui.QPushButton('OK', self)
        self.connect(ok, QtCore.SIGNAL('clicked()'), self.accept)
        layout.addWidget(ok)

        self.setLayout(layout)


    def _create_checkbox(self, setting):
        """Return a ``QCheckBox`` for the given setting,
        with the event handler already connected.
        """
        # Getter and setter methods for this setting
        _get = getattr(self.editor, setting['get'])
        _set = getattr(self.editor, setting['set'])

        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == QtCore.Qt.Checked:
                _set(setting['on'])
            elif state == QtCore.Qt.Unchecked:
                _set(setting['off'])

        # Create the checkbox and connect the event handler
        checkbox = QtGui.QCheckBox(setting['label'], self)
        self.connect(checkbox,
            QtCore.SIGNAL('stateChanged(int)'),
            checkbox_changed)

        # Set the initial checkbox state based on current value
        if _get() == setting['on']:
            checkbox.setCheckState(QtCore.Qt.Checked)
        elif _get() == setting['off']:
            checkbox.setCheckState(QtCore.Qt.Unchecked)

        return checkbox


