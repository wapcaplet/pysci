# config.py

__all__ = [
    'EditorSettings',
]

from PyQt4 import QtCore, QtGui
import settings
from enums import enum_value

class EditorSettings (QtGui.QDialog):
    """A dialog window for configuring a QsciScintilla editor.
    """
    def __init__(self, editor):
        QtGui.QDialog.__init__(self, editor)
        self.editor = editor

        self.setWindowTitle('Noodle settings')
        layout = self._create_layout()
        self.setLayout(layout)


    def _create_layout(self):
        """Create and return the main layout for the dialog widget.
        """
        layout = QtGui.QVBoxLayout()

        # Checkboxes for each boolean setting
        for bool_setting in settings._bool_settings:
            layout.addWidget(self._create_checkbox(bool_setting))

        # Comboboxes for each multi-select setting
        for combo_setting in settings._combo_settings:
            hbox = QtGui.QHBoxLayout()
            hbox.addWidget(QtGui.QLabel(combo_setting['label']))
            hbox.addWidget(self._create_combobox(combo_setting))
            layout.addLayout(hbox)

        for color_setting in settings._color_settings:
            layout.addWidget(self._create_color_picker(color_setting))

        # OK button
        ok = QtGui.QPushButton('OK', self)
        self.connect(ok, QtCore.SIGNAL('clicked()'), self.accept)
        layout.addWidget(ok)

        return layout


    def _create_checkbox(self, setting):
        """Return a ``QCheckBox`` for the given setting,
        with the event handler already connected.
        """
        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == QtCore.Qt.Checked:
                self.editor.set_config(setting['name'], True)
            elif state == QtCore.Qt.Unchecked:
                self.editor.set_config(setting['name'], False)

        # Create the checkbox and connect the event handler
        checkbox = QtGui.QCheckBox(setting['label'], self)
        self.connect(checkbox,
            QtCore.SIGNAL('stateChanged(int)'),
            checkbox_changed)

        # Set the initial checkbox state based on current value
        if self.editor.get_config(setting['name']):
            checkbox.setCheckState(QtCore.Qt.Checked)
        else:
            checkbox.setCheckState(QtCore.Qt.Unchecked)

        return checkbox


    def _create_combobox(self, setting):
        """Return a ``QComboBox`` for the given setting,
        with the event handler already connected.
        """
        # Create the combobox and populate it
        combo = QtGui.QComboBox(self)
        for label, value in setting['values']:
            data = QtCore.QVariant(value)
            combo.addItem(label, data)

        # TODO: Set the initial value, if any
        # (This approach doesn't work due to string vs. int issues)
        #current = self.editor.get_config(setting['name'])
        #index = combo.findData(current)
        #combo.setCurrentIndex(index)

        # Ugly event handler!
        def combo_changed(index):
            data = combo.itemData(index)
            value = str(data.toString())
            self.editor.set_config(setting['name'], value)

        # Connect event handler
        self.connect(combo,
            QtCore.SIGNAL('currentIndexChanged(int)'),
            combo_changed)

        return combo


    def _create_color_picker(self, setting):
        """Return a button for picking a color.
        """
        button = QtGui.QPushButton(setting['label'])

        def button_pressed():
            current_color = self.editor.get_config(setting['name'])
            color = QtGui.QColorDialog.getColor(current_color)
            self.editor.set_config(setting['name'], color)

        self.connect(button,
            QtCore.SIGNAL('pressed()'),
            button_pressed)

        return button


