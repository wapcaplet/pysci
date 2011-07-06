# settings.py

"""Configuration settings for QSciScintilla widgets.
"""

from PyQt4 import Qsci, QtGui

_default_config = {
    # Flags and numeric values
    'tabIndents': True,
    'tabWidth': 4,
    'indentationsUseTabs': False,
    'backspaceUnindents': True,
    'autoIndent': False,
    'indentationGuides': False,
    'eolVisibility': False,
    'edgeColumn': 80,
    'caretLineVisible': True,
    'marginLineNumbers': (0, True),

    # Fonts
    'font': QtGui.QFont('Courier New', 10),
    'marginsFont': QtGui.QFont('Courier New', 10),

    # Colors
    'edgeColor': QtGui.QColor('#FF0000'),
    'caretLineBackgroundColor': QtGui.QColor('#F0F0F0'),
    'marginsBackgroundColor': QtGui.QColor('#C0C0C0'),
    'marginsForegroundColor': QtGui.QColor('#000000'),
    'foldMarginColors': (QtGui.QColor('#AAAAFF'), QtGui.QColor('#333300')),

    # Whitespace: Ws(Invisible|Visible|VisibleAfterIndent)
    'whitespaceVisibility': Qsci.QsciScintilla.WsInvisible,
    # Edge mode: Edge(None|Line|Background)
    'edgeMode': Qsci.QsciScintilla.EdgeNone,
    # Brace matching: (No|Strict|Sloppy)BraceMatch
    'braceMatching': Qsci.QsciScintilla.SloppyBraceMatch,
    # Folding: (No|Plain|Circled|Boxed|CircledTree|BoxedTree)FoldStyle
    'folding': Qsci.QsciScintilla.NoFoldStyle,
    # Wrap mode: Wrap(None|Word|Character)
    'wrapMode': Qsci.QsciScintilla.WrapWord,
}

# Custom boolean settings, shown as checkboxes
_bool_settings = (
    # Indentation
    {
        'label': 'Tab indents',
        'name': 'tabIndents',
        'on': True,
        'off': False,
    },
    {
        'label': 'Backspace unindents',
        'name': 'backspaceUnindents',
        'on': True,
        'off': False,
    },
    {
        'label': 'Auto-indent',
        'name': 'autoIndent',
        'on': True,
        'off': False,
    },
    {
        'label': 'Show indentation guides',
        'name': 'indentationGuides',
        'on': True,
        'off': False,
    },
    {
        'label': 'Use tab character',
        'name': 'indentationsUseTabs',
        'on': True,
        'off': False,
    },
    {
        'label': 'Visible line endings',
        'name': 'eolVisibility',
        'on': True,
        'off': False,
    },
    # FIXME: This requires an integer 'margin' argument
    #{
        #'label': 'Show line numbers',
        #'get': 'marginLineNumbers',
        #'set': 'setMarginLineNumbers',
        #'on': True,
        #'off': False,
    #},
)

# Multiple-selection settings
_combo_settings = (
    {
        'label': 'Annotation Display',
        'name': 'annotationDisplay',
        'values': (
            ('Hidden', 'AnnotationHidden'),
            ('Standard', 'AnnotationStandard'),
            ('Boxed', 'AnnotationBoxed'),
        ),
    },
    {
        'label': 'Auto Completion Source',
        'name': 'autoCompletionSource',
        'values': (
            ('None', 'AcsNone'),
            ('All', 'AcsAll'),
            ('Document', 'AcsDocument'),
            ('APIs', 'AcsAPIs'),
        ),
    },
    {
        'label': 'Brace Matching',
        'name': 'braceMatching',
        'values': (
            ('None', 'NoBraceMatch'),
            ('Strict', 'StrictBraceMatch'),
            ('Sloppy', 'SloppyBraceMatch'),
        ),
    },
    {
        'label': 'Call Tips Style',
        'name': 'callTipsStyle',
        'values': (
            ('None', 'CallTipsNone'),
            ('No Context', 'CallTipsNoContext'),
            ('No Auto-completion Context', 'CallTipsNoAutoCompletionContext'),
            ('Context', 'CallTipsContext'),
        ),
    },
    {
        'label': 'Edge Mode',
        'name': 'edgeMode',
        'values': (
            ('None', 'EdgeNone'),
            ('Line', 'EdgeLine'),
            ('Background', 'EdgeBackground'),
        ),
    },
    {
        'label': 'Line Endings',
        'name': 'eolMode',
        'values': (
            ('Windows', 'EolWindows'),
            ('Unix', 'EolUnix'),
            ('Mac', 'EolMac'),
        ),
    },
    {
        'label': 'Folding',
        'name': 'folding',
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
        'values': (
            ('Invisible', 'WsInvisible'),
            ('Visible', 'WsVisible'),
            ('Visible After Indent', 'WsVisibleAfterIndent'),
        ),
    },
    {
        'label': 'Wrap Mode',
        'name': 'wrapMode',
        'values': (
            ('None', 'WrapNone'),
            ('Word', 'WrapWord'),
            ('Character', 'WrapCharacter'),
        ),
    },
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
        'label': 'Text width (characters)',
        'name': 'edgeColumn',
    },
    {
        'label': 'Indentation width (characters)',
        'name': 'indentationWidth',
    },
    {
        'label': 'Tab width (characters)',
        'name': 'tabWidth',
    },
)

# Other settings
#
# Numeric:
#
#     Indent width
#     Wrap at column
#
# Choice / selection:
#
#     Language
#     Font
#     Font color
#     Syntax highlighting colors
#

