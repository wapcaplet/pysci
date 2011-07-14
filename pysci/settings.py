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

from language import language_extensions

_settings = {
    # Boolean settings
    'tabIndents': {
        'label': 'Tab indents',
        'type': 'bool',
        'help': 'Use the tab key to indent text',
    },
    'backspaceUnindents': {
        'label': 'Backspace unindents',
        'type': 'bool',
        'help': 'Backspace will unindent a line instead of just deleting a character',
    },
    'autoIndent': {
        'label': 'Auto-indent',
        'type': 'bool',
        'help': 'Automatically indent text to match the preceding line',
    },
    'indentationGuides': {
        'label': 'Indentation guides',
        'type': 'bool',
        'help': 'Display visible guidelines to help keep indentation consistent',
    },
    'indentationsUseTabs': {
        'label': 'Use tab character',
        'type': 'bool',
        'help': 'Tab key inserts an actual tab character instead of spaces',
    },
    'eolVisibility': {
        'label': 'Show CR/LF',
        'type': 'bool',
        'help': 'Display a visible icon for carriage return and line feeds',
    },

    # Color settings
    'color': {
        'label': 'Text color',
        'type': 'color',
    },
    'paper': {
        'label': 'Paper color',
        'type': 'color',
    },

    # Numeric settings
    'edgeColumn': {
        'label': 'Text width',
        'type': 'number',
        'help': 'Number of characters per line before wrapping occurs',
    },
    'tabWidth': {
        'label': 'Tab width',
        'type': 'number',
        'help': 'Width of tabs in characters, or the number of'
            ' spaces to insert when tab is pressed',
    },

    # Multiple-selection settings
    'braceMatching': {
        'label': 'Brace Matching',
        'type': 'combo',
        'help': 'Whether and how to highlight matching {} [] () braces',
        'values': (
            ('None', 'NoBraceMatch'),
            ('Strict', 'StrictBraceMatch'),
            ('Sloppy', 'SloppyBraceMatch'),
        ),
    },
    'edgeMode': {
        'label': 'Edge Mode',
        'type': 'combo',
        'help': 'How the edge of the text width is indicated',
        'values': (
            ('None', 'EdgeNone'),
            ('Line', 'EdgeLine'),
            ('Background', 'EdgeBackground'),
        ),
    },
    'eolMode': {
        'label': 'Line Endings',
        'type': 'combo',
        'help': 'End lines with carriage return and/or line feed',
        'values': (
            ('Windows', 'EolWindows'),
            ('Unix', 'EolUnix'),
            ('Mac', 'EolMac'),
        ),
    },
    'folding': {
        'label': 'Folding',
        'type': 'combo',
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
    'whitespaceVisibility': {
        'label': 'Whitespace',
        'type': 'combo',
        'help': 'Whether whitespace is indicated with visible markers',
        'values': (
            ('Invisible', 'WsInvisible'),
            ('Visible', 'WsVisible'),
            ('Visible After Indent', 'WsVisibleAfterIndent'),
        ),
    },
    'wrapMode': {
        'label': 'Wrap Mode',
        'type': 'combo',
        'help': 'How to wrap text when it reaches the text width',
        'values': (
            ('None', 'WrapNone'),
            ('Word', 'WrapWord'),
            ('Character', 'WrapCharacter'),
        ),
    },
    'language': {
        'label': 'Language',
        'type': 'combo',
        'help': 'Syntax highlighting language',
        'values': [
            (lang, lang) for (lang, ext) in language_extensions
        ],
    },

    # TODO: Need a getter for this
    # 'caretWidth': {
        #'label': 'Caret width (pixels)',
    #},

    # Stuff the user probably doesn't care about configuring
    # (or do you?)
    # 'annotationDisplay': {
        #'label': 'Annotation Display',
        #'type': 'combo',
        #'values': (
            #('Hidden', 'AnnotationHidden'),
            #('Standard', 'AnnotationStandard'),
            #('Boxed', 'AnnotationBoxed'),
        #),
    #},
    # 'autoCompletionSource': {
        #'label': 'Auto Completion Source',
        #'type': 'combo',
        #'values': (
            #('None', 'AcsNone'),
            #('All', 'AcsAll'),
            #('Document', 'AcsDocument'),
            #('APIs', 'AcsAPIs'),
        #),
    #},
    # 'callTipsStyle': {
        #'label': 'Call Tips Style',
        #'type': 'combo',
        #'values': (
            #('None', 'CallTipsNone'),
            #('No Context', 'CallTipsNoContext'),
            #('No Auto-completion Context', 'CallTipsNoAutoCompletionContext'),
            #('Context', 'CallTipsContext'),
        #),
    #},

}

# Setting groups
_setting_groups = (
    ('Colors',
        (
            'color',
            'paper',
        )
    ),

    ('Indentation',
        (
            'tabWidth',
            'tabIndents',
            'backspaceUnindents',
            'autoIndent',
            'indentationGuides',
            'indentationsUseTabs',
        )
    ),

    ('Wrapping',
        (
            'edgeMode',
            'wrapMode',
            'edgeColumn',
        )
    ),

    ('Formatting',
        (
            'whitespaceVisibility',
            'eolMode',
            'eolVisibility',
        )
    ),

    ('Coding aids',
        (
            'language',
            'folding',
            'braceMatching',
        )
    ),
)


# Write-only color settings.
# FIXME: Can't effectively include these until getters are written.
_other_color_settings = (
    # Selection
    'selectionForegroundColor',
    'selectionBackgroundColor',
    # Caret (current line)
    'caretForegroundColor',
    'caretLineBackgroundColor',
    # Edge marker
    'edgeColor',
    # Indentation guides
    'indentationGuidesForegroundColor',
    'indentationGuidesBackgroundColor',
    # Brace matching
    'matchedBraceForegroundColor',
    'matchedBraceBackgroundColor',
    'unmatchedBraceForegroundColor',
    'unmatchedBraceBackgroundColor',
    # Marker colors
    'markerForegroundColor',
    'markerBackgroundColor',
    # Margins
    'marginsForegroundColor',
    'marginsBackgroundColor',
    # CallTips
    'callTipsForegroundColor',
    'callTipsBackgroundColor',
    'callTipsHighlightColor',
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
        # Indexed group boxes, for easier rearrangement
        groups = {}

        # Create and populate each group
        for label, names in _setting_groups:
            groups[label] = QtGui.QGroupBox(label)
            group_layout = QtGui.QVBoxLayout()
            for name in names:
                group_layout.addLayout(self._create_widget(name))
            groups[label].setLayout(group_layout)
            groups[label].setFlat(False)

        # Create two columns
        left_column = QtGui.QVBoxLayout()
        left_column.addWidget(groups['Indentation'])
        left_column.addWidget(groups['Wrapping'])
        left_column.addStretch(1)
        right_column = QtGui.QVBoxLayout()
        right_column.addWidget(groups['Formatting'])
        right_column.addWidget(groups['Colors'])
        right_column.addWidget(groups['Coding aids'])
        right_column.addStretch(1)

        # Arrange both columns side-by-side in the middle
        columns_layout = QtGui.QHBoxLayout()
        columns_layout.addLayout(left_column)
        columns_layout.addLayout(right_column)

        # Layout columns section and OK button vertically
        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(columns_layout)

        # OK button at the bottom
        ok = QtGui.QPushButton('OK', self)
        self.connect(ok, QtCore.SIGNAL('clicked()'), self.accept)
        main_layout.addWidget(ok)

        return main_layout


    def _create_widget(self, name):
        """Return an appropriate widget for the given configuration setting.
        """
        setting = _settings[name]
        type_ = setting['type']

        # Get the appropriate widget type
        if type_ == 'bool':
            widget = self._create_checkbox(name)
        elif type_ == 'number':
            widget = self._create_number_box(name)
        elif type_ == 'combo':
            widget = self._create_combobox(name)
        elif type_ == 'color':
            widget = self._create_color_picker(name)


        # Label with possible tooltip
        label = QtGui.QLabel(setting['label'])

        # Add tooltip to widget
        if 'help' in setting:
            widget.setToolTip(setting['help'])

        # Add label and widget
        layout = QtGui.QHBoxLayout()
        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(widget)

        return layout


    def _create_checkbox(self, name):
        """Return a ``QCheckBox`` for the given setting.
        """
        checkbox = QtGui.QCheckBox(self)

        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == QtCore.Qt.Checked:
                self.editor.set_config(name, True)
            elif state == QtCore.Qt.Unchecked:
                self.editor.set_config(name, False)

        self.connect(checkbox,
            QtCore.SIGNAL('stateChanged(int)'),
            checkbox_changed)

        # Set the initial checkbox state based on current value
        if self.editor.get_config(name):
            checkbox.setCheckState(QtCore.Qt.Checked)
        else:
            checkbox.setCheckState(QtCore.Qt.Unchecked)

        return checkbox


    def _create_combobox(self, name):
        """Return a combobox for modifying a multiple-value setting.
        """
        setting = _settings[name]
        # Create the combobox and populate it
        combo = QtGui.QComboBox(self)
        for label, value in setting['values']:
            data = QtCore.QVariant(value)
            combo.addItem(label, data)

        print("%s:" % name)
        print(self.editor.get_config(name).__class__.__name__)

        # TODO: Set the initial value, if any
        # (This approach doesn't work due to string vs. int issues)
        #current = self.editor.get_config(setting['name'])
        #index = combo.findData(current)
        #combo.setCurrentIndex(index)

        # Ugly event handler!
        def combo_changed(index):
            data = combo.itemData(index)
            value = str(data.toString())
            self.editor.set_config(name, value)

        # Connect event handler
        self.connect(combo,
            QtCore.SIGNAL('currentIndexChanged(int)'),
            combo_changed)

        return combo


    def _create_color_picker(self, name):
        """Return a color-picker widget for a color-based setting.
        """
        # Button with colored background
        button = QtGui.QPushButton()

        # Event handler
        def button_pressed():
            current_color = self.editor.get_config(name)
            color = QtGui.QColorDialog.getColor(current_color)
            button.setStyleSheet("background-color: %s" % color.name())
            self.editor.set_config(name, color)

        # Connect event handler
        self.connect(button,
            QtCore.SIGNAL('pressed()'),
            button_pressed)

        # Set default background color
        color = self.editor.get_config(name)
        button.setStyleSheet("background-color: %s" % color.name())

        return button


    def _create_number_box(self, name):
        """Return a numeric entry widget for a numeric setting.
        """
        spinbox = QtGui.QSpinBox()

        # Set initial value
        spinbox.setValue(self.editor.get_config(name))

        def spinbox_changed(value):
            self.editor.set_config(name, value)

        # Connect event handler
        self.connect(spinbox,
            QtCore.SIGNAL('valueChanged(int)'),
            spinbox_changed)

        return spinbox


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

