# settings.py

"""Configuration settings for QSciScintilla widgets.
"""

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

