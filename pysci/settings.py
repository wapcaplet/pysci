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
        'get': 'tabIndents',
        'set': 'setTabIndents',
        'on': True,
        'off': False,
    },
    {
        'label': 'Backspace unindents',
        'get': 'backspaceUnindents',
        'set': 'setBackspaceUnindents',
        'on': True,
        'off': False,
    },
    {
        'label': 'Auto-indent',
        'get': 'autoIndent',
        'set': 'setAutoIndent',
        'on': True,
        'off': False,
    },
    {
        'label': 'Show indentation guides',
        'get': 'indentationGuides',
        'set': 'setIndentationGuides',
        'on': True,
        'off': False,
    },
    {
        'label': 'Use tab character',
        'get': 'indentationsUseTabs',
        'set': 'setIndentationsUseTabs',
        'on': True,
        'off': False,
    },
    # Visibility
    {
        'label': 'Visible whitespace',
        'get': 'whitespaceVisibility',
        'set': 'setWhitespaceVisibility',
        'on': Qsci.QsciScintilla.WsVisible,
        'off': Qsci.QsciScintilla.WsInvisible,
    },
    {
        'label': 'Visible line endings',
        'get': 'eolVisibility',
        'set': 'setEolVisibility',
        'on': True,
        'off': False,
    },
    # Other
    {
        'label': 'Edge marker',
        'get': 'edgeMode',
        'set': 'setEdgeMode',
        'on': Qsci.QsciScintilla.EdgeLine,
        'off': Qsci.QsciScintilla.EdgeNone,
    },
    {
        'label': 'Brace matching',
        'get': 'braceMatching',
        'set': 'setBraceMatching',
        'on': Qsci.QsciScintilla.SloppyBraceMatch,
        'off': Qsci.QsciScintilla.NoBraceMatch,
    },
    {
        'label': 'Code folding',
        'get': 'folding',
        'set': 'setFolding',
        'on': Qsci.QsciScintilla.BoxedTreeFoldStyle,
        'off': Qsci.QsciScintilla.NoFoldStyle,
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

# Custom foreground and background colors
_color_settings = (
    # Basic editor colors (no effect with lexer on)
    {
        'label': 'Text color',
        'get': 'color',
        'set': 'setColor',
    },
    {
        'label': 'Paper color',
        'get': 'paper',
        'set': 'setPaper',
    },
    # Selection
    {
        'label': '',
        'set': 'setSelectionForegroundColor',
    },
    {
        'label': '',
        'set': 'setSelectionBackgroundColor',
    },
    # Caret (current line)
    {
        'label': '',
        'set': 'setCaretForegroundColor',
    },
    {
        'label': '',
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
# Misc:
#
#     EolWindows / EolUnix / EolMac
#     WrapNone / WrapWord / WrapCharacter
#
#

