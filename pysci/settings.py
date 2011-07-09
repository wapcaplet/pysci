# settings.py

"""PySci settings widget for configuring preferences.
"""

__all__ = [
    'PySciSettings',
]

try:
    from PyQt4 import QtCore, QtGui
except ImportError:
    print("Please insteall PyQt4.")

# Custom boolean settings, shown as checkboxes
_bool_settings = (
    # Indentation
    {
        'label': 'Tab indents',
        'name': 'tabIndents',
        'help': 'Use the tab key to indent text',
    },
    {
        'label': 'Backspace unindents',
        'name': 'backspaceUnindents',
        'help': 'Backspace will unindent a line instead of just deleting a character',
    },
    {
        'label': 'Auto-indent',
        'name': 'autoIndent',
        'help': 'Automatically indent text to match the preceding line',
    },
    {
        'label': 'Show indentation guides',
        'name': 'indentationGuides',
        'help': 'Display visible guidelines to help keep indentation consistent',
    },
    {
        'label': 'Use tab character',
        'name': 'indentationsUseTabs',
        'help': 'Tab key inserts an actual tab character instead of spaces',
    },
    {
        'label': 'Visible line endings',
        'name': 'eolVisibility',
        'help': 'Display a visible icon for carriage return and line feeds',
    },
)

# Multiple-selection settings
_combo_settings = (
    {
        'label': 'Brace Matching',
        'name': 'braceMatching',
        'help': 'Whether and how to highlight matching {} [] () braces',
        'values': (
            ('None', 'NoBraceMatch'),
            ('Strict', 'StrictBraceMatch'),
            ('Sloppy', 'SloppyBraceMatch'),
        ),
    },
    {
        'label': 'Edge Mode',
        'name': 'edgeMode',
        'help': 'How the edge of the text width is indicated',
        'values': (
            ('None', 'EdgeNone'),
            ('Line', 'EdgeLine'),
            ('Background', 'EdgeBackground'),
        ),
    },
    {
        'label': 'Line Endings',
        'name': 'eolMode',
        'help': 'End lines with carriage return and/or line feed',
        'values': (
            ('Windows (CR/LF)', 'EolWindows'),
            ('Unix (LF)', 'EolUnix'),
            ('Mac (CR)', 'EolMac'),
        ),
    },
    {
        'label': 'Folding',
        'name': 'folding',
        'help': 'What kind of icons to display for code-folding',
        'values': (
            ('None', 'NoFoldStyle'),
            ('Plain','PlainFoldStyle'),
            ('Circled', 'CircledFoldStyle'),
            ('Boxed', 'BoxedFoldStyle'),
            ('Circled Tree', 'CircledTreeFoldStyle'),
            ('Boxed Tree', 'BoxedTreeFoldStyle'),
        ),
    },
    {
        'label': 'Whitespace Visibility',
        'name': 'whitespaceVisibility',
        'help': 'Whether whitespace is indicated with visible markers',
        'values': (
            ('Invisible', 'WsInvisible'),
            ('Visible', 'WsVisible'),
            ('Visible After Indent', 'WsVisibleAfterIndent'),
        ),
    },
    {
        'label': 'Wrap Mode',
        'name': 'wrapMode',
        'help': 'How to wrap text when it reaches the text width',
        'values': (
            ('None', 'WrapNone'),
            ('Word', 'WrapWord'),
            ('Character', 'WrapCharacter'),
        ),
    },
    # Stuff the user probably doesn't care about configuring
    # (or do you?)
    #{
        #'label': 'Annotation Display',
        #'name': 'annotationDisplay',
        #'values': (
            #('Hidden', 'AnnotationHidden'),
            #('Standard', 'AnnotationStandard'),
            #('Boxed', 'AnnotationBoxed'),
        #),
    #},
    #{
        #'label': 'Auto Completion Source',
        #'name': 'autoCompletionSource',
        #'values': (
            #('None', 'AcsNone'),
            #('All', 'AcsAll'),
            #('Document', 'AcsDocument'),
            #('APIs', 'AcsAPIs'),
        #),
    #},
    #{
        #'label': 'Call Tips Style',
        #'name': 'callTipsStyle',
        #'values': (
            #('None', 'CallTipsNone'),
            #('No Context', 'CallTipsNoContext'),
            #('No Auto-completion Context', 'CallTipsNoAutoCompletionContext'),
            #('Context', 'CallTipsContext'),
        #),
    #},
)

# Custom foreground and background colors
_color_settings = (
    # Basic editor colors (no effect with lexer on)
    {
        'label': 'Text color',
        'name': 'color',
    },
    {
        'label': 'Paper color',
        'name': 'paper',
    },
)
_other_color_settings = (
    # Selection
    {
        'label': 'Selection foreground color',
        'set': 'setSelectionForegroundColor',
    },
    {
        'label': 'Selection background color',
        'set': 'setSelectionBackgroundColor',
    },
    # Caret (current line)
    {
        'label': 'Caret foreground color',
        'set': 'setCaretForegroundColor',
    },
    {
        'label': 'Caret background color',
        'set': 'setCaretLineBackgroundColor',
    },
    # Edge marker
    {
        'label': 'Edge marker color',
        'get': 'edgeColor',
        'set': 'setEdgeColor',
    },
    # Indentation guides
    {
        'label': '',
        'set': 'setIndentationGuidesForegroundColor',
    },
    {
        'label': '',
        'set': 'setIndentationGuidesBackgroundColor',
    },
    # Brace matching
    {
        'label': '',
        'set': 'setMatchedBraceForegroundColor',
    },
    {
        'label': '',
        'set': 'setMatchedBraceBackgroundColor',
    },
    {
        'label': '',
        'set': 'setUnmatchedBraceForegroundColor',
    },
    {
        'label': '',
        'set': 'setUnmatchedBraceBackgroundColor',
    },
    # Marker colors
    {
        'label': '',
        'set': 'setMarkerForegroundColor',
    },
    {
        'label': '',
        'set': 'setMarkerBackgroundColor',
    },
    # Margins
    {
        'label': '',
        'set': 'setMarginsForegroundColor',
    },
    {
        'label': '',
        'set': 'setMarginsBackgroundColor',
    },
    # CallTips
    {
        'label': '',
        'set': 'setCallTipsForegroundColor',
    },
    {
        'label': '',
        'set': 'setCallTipsBackgroundColor',
    },
    {
        'label': '',
        'set': 'setCallTipsHighlightColor',
    },
)

_numeric_settings = (
    # TODO: Need a getter for this
    #{
        #'label': 'Caret width (pixels)',
        #'name': 'caretWidth',
    #},
    {
        'label': 'Text width',
        'name': 'edgeColumn',
        'help': 'Number of characters per line before wrapping occurs',
    },
    {
        'label': 'Tab width',
        'name': 'tabWidth',
        'help': 'Width of tabs in characters, or the number of'
            ' spaces to insert when tab is pressed',
    },
)


class PySciSettings (QtGui.QDialog):
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
        for bool_setting in _bool_settings:
            layout.addWidget(self._create_checkbox(bool_setting))

        # Comboboxes for each multi-select setting
        for combo_setting in _combo_settings:
            layout.addLayout(self._create_combobox(combo_setting))

        # Color pickers for each color setting
        for color_setting in _color_settings:
            layout.addLayout(self._create_color_picker(color_setting))

        # Spinboxes for each numeric setting
        for num_setting in _numeric_settings:
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

