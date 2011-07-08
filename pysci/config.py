# config.py

__all__ = [
    'EditorSettings',
]

try:
    from PyQt4 import QtCore, QtGui
except ImportError:
    print("Please insteall PyQt4.")

import settings
#from enums import enum_value

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
        layout.addWidget(self._create_line_number_checkbox())
        for bool_setting in settings._bool_settings:
            layout.addWidget(self._create_checkbox(bool_setting))

        # Comboboxes for each multi-select setting
        for combo_setting in settings._combo_settings:
            layout.addLayout(self._create_combobox(combo_setting))

        # Color pickers for each color setting
        for color_setting in settings._color_settings:
            layout.addLayout(self._create_color_picker(color_setting))

        # Spinboxes for each numeric setting
        for num_setting in settings._numeric_settings:
            layout.addLayout(self._create_number_box(num_setting))

        # OK button
        ok = QtGui.QPushButton('OK', self)
        self.connect(ok, QtCore.SIGNAL('clicked()'), self.accept)
        layout.addWidget(ok)

        return layout


    def _create_checkbox(self, setting):
        """Return a ``QCheckBox`` for the given setting,
        with the event handler already connected.
        """
        checkbox = QtGui.QCheckBox(setting['label'], self)
        if 'help' in setting:
            checkbox.setToolTip(setting['help'])

        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == QtCore.Qt.Checked:
                self.editor.set_config(setting['name'], True)
            elif state == QtCore.Qt.Unchecked:
                self.editor.set_config(setting['name'], False)

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
        """Return a layout with a label and combobox for modifying a
        multiple-value setting.
        """
        # Create the combobox and populate it
        combo = QtGui.QComboBox(self)
        for label, value in setting['values']:
            data = QtCore.QVariant(value)
            combo.addItem(label, data)
        if 'help' in setting:
            combo.setToolTip(setting['help'])

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

        # Layout with label and combobox
        layout = QtGui.QHBoxLayout()
        layout.addWidget(QtGui.QLabel(setting['label']))
        layout.addWidget(combo)

        return layout


    def _create_color_picker(self, setting):
        """Return a color-picker widget for a color-based setting.
        """
        # Button with colored background
        button = QtGui.QPushButton()

        # Event handler
        def button_pressed():
            current_color = self.editor.get_config(setting['name'])
            color = QtGui.QColorDialog.getColor(current_color)
            button.setStyleSheet("background-color: %s" % color.name())
            self.editor.set_config(setting['name'], color)

        # Connect event handler
        self.connect(button,
            QtCore.SIGNAL('pressed()'),
            button_pressed)

        # Set default background color
        color = self.editor.get_config(setting['name'])
        button.setStyleSheet("background-color: %s" % color.name())

        # Layout with label and color button
        layout = QtGui.QHBoxLayout()
        layout.addWidget(QtGui.QLabel(setting['label']))
        layout.addWidget(button)

        return layout


    def _create_number_box(self, setting):
        """Return a numeric entry widget for a numeric setting.
        """
        spinbox = QtGui.QSpinBox()
        if 'help' in setting:
            spinbox.setToolTip(setting['help'])

        # Set initial value
        spinbox.setValue(self.editor.get_config(setting['name']))

        def spinbox_changed(value):
            self.editor.set_config(setting['name'], value)

        # Connect event handler
        self.connect(spinbox,
            QtCore.SIGNAL('valueChanged(int)'),
            spinbox_changed)

        # Layout with label and color button
        layout = QtGui.QHBoxLayout()
        layout.addWidget(QtGui.QLabel(setting['label']))
        layout.addWidget(spinbox)

        return layout


    def _create_line_number_checkbox(self):
        """Return a widget for enabling/disabling line numbers.
        """
        # Line numbers
        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == QtCore.Qt.Checked:
                self.editor.set_config('marginLineNumbers', (0, True))
            elif state == QtCore.Qt.Unchecked:
                self.editor.set_config('marginLineNumbers', (0, False))

        # Create the checkbox and connect the event handler
        checkbox = QtGui.QCheckBox('Line numbers', self)
        self.connect(checkbox,
            QtCore.SIGNAL('stateChanged(int)'),
            checkbox_changed)

        # Set the initial checkbox state based on current value
        if self.editor.get_config('marginLineNumbers', 0):
            checkbox.setCheckState(QtCore.Qt.Checked)
        else:
            checkbox.setCheckState(QtCore.Qt.Unchecked)

        return checkbox

