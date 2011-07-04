# enms.py

"""Wrapper for Qsci.QsciScintilla enumerations.
"""

from PyQt4 import Qsci

class BadEnum (Exception):
    """Bad (unknown or failed) enumeration name.
    """
    def __init__(self, name):
        super(BadEnum, self).__init__("Enumeration name unknown: '%s'" % name)


def enum_value(name):
    """Return the Qsci.QsciScintilla value for the given enumeration name.
    """
    if name not in _enums:
        raise BadEnum(name)
    else:
        # Some officially documented enums don't work; catch them
        # and raise BadEnum instead of KeyError
        try:
            return Qsci.QsciScintilla.__dict__[name]
        except KeyError:
            raise BadEnum(name)


def enum_help(name):
    """Return help text on the given enumeration name.
    """
    try:
        return _enums[name]
    except KeyError:
        raise BadEnum(name)


# Enumerations
_enums = {
    # auto-indentation styles
    'AiMaintain':
        """A line is automatically indented to match the previous line.""",

    'AiOpening':
        """If the language supported by the current lexer has a specific start
        of block character (e.g. { in C++), then a line that begins with that
        character is indented as well as the lines that make up the block. It
        may be logically ored with AiClosing.""", 'AiClosing': """If the
        language supported by the current lexer has a specific end of block
        character (e.g. } in C++), then a line that begins with that character
        is indented as well as the lines that make up the block. It may be
        logically ored with AiOpening.""",

    # gcAnnotationDisplay
    # annotation display styles
    'AnnotationHidden':
        """Annotations are not displayed.""",

    'AnnotationStandard':
        """Annotations are drawn left justified with no adornment.""",

    'AnnotationBoxed':
        """Annotations are surrounded by a box.""",

    # gcAutoCompletionUseSingle
    # behavior if an auto-completion list contains a single entry.
    'AcusNever':
        """The single entry is not used automatically and the auto-completion list
        is displayed.""",

    'AcusExplicit':
        """The single entry is used automatically when auto-completion is
        explicitly requested (using autoCompleteFromAPIs() or
        autoCompleteFromDocument()) but not when auto-completion is
        triggered as the user types.""",

    'AcusAlways':
        """The single entry is used automatically and the auto-completion list
        is not displayed.""",

    # gcAutoCompletionSource
    # sources for auto-completion lists.
    'AcsNone':
        """No sources are used, ie. automatic auto-completion is disabled.""",

    'AcsAll':
        """The source is all available sources.""",

    'AcsDocument':
        """The source is the current document.""",

    'AcsAPIs':
        """The source is any installed APIs.""",

    # gcBraceMatch
    # brace matching modes. The character pairs {}, [] and () are treated as braces. The Python lexer will also match a : with the end of the corresponding indented block.
    'NoBraceMatch':
        """Brace matching is disabled.""",

    'StrictBraceMatch':
        """Brace matching is enabled for a brace immediately before
        the current position.""",

    'SloppyBraceMatch':
        """Brace matching is enabled for a brace immediately before
        or after the current position.""",

    # gcCallTipsStyle
    # call tip styles
    'CallTipsNone':
        """Call tips are disabled.""",

    'CallTipsNoContext':
        """Call tips are displayed without a context. A context is any scope
        (e.g. a C++ namespace or a Python module) prior to the function
        name.""",

    'CallTipsNoAutoCompletionContext':
        """Call tips are displayed with a context only if the user hasn't
        already implicitly identified the context using autocompletion. Note
        that this style may not always be able to align the call tip with the
        text being entered.""",

    'CallTipsContext':
        """Call tips are displayed with a context. Note that this style may not
        always be able to align the call tip with the text being entered.""",

    # gcEdgeMode
    # edge modes for long lines
    'EdgeNone':
        """Long lines are not marked.""",
    'EdgeLine':
        """A vertical line is drawn at the column set by setEdgeColumn(). This is
        recommended for monospace fonts.""",

    'EdgeBackground':
        """The background color of characters after the column limit is changed
        to the color set by setEdgeColor(). This is recommended for
        proportional fonts.""",

    # gcEolMode
    # end-of-line modes
    'EolWindows':
        """A carriage return/line feed as used on Windows systems.""",

    'EolUnix':
        """A line feed as used on Unix systems.""",

    'EolMac':
        """A carriage return as used on Mac systems.""",

    # gcFoldStyle
    # styles for the folding margin
    'NoFoldStyle':
        """Folding is disabled.""",

    'PlainFoldStyle':
        """Plain folding style using plus and minus symbols.""",

    'CircledFoldStyle':
        """Circled folding style using circled plus and minus symbols.""",

    'BoxedFoldStyle':
        """Boxed folding style using boxed plus and minus symbols.""",

    'CircledTreeFoldStyle':
        """Circled tree style using a flattened tree with circled plus and
        minus symbols and rounded corners.""",

    'BoxedTreeFoldStyle':
        """Boxed tree style using a flattened tree with boxed plus and minus
        symbols and right-angled corners.""",

    # gcMarginType
    # margin types
    'SymbolMargin':
        """The margin contains symbols, including those used for folding.""",

    'SymbolMarginDefaultForegroundColor':
        """The margin contains symbols and uses the default foreground color
        as its background color.""",

    'SymbolMarginDefaultBackgroundColor':
        """The margin contains symbols and uses the default background color
        as its background color.""",

    'NumberMargin':
        """The margin contains line numbers.""",

    'TextMargin':
        """The margin contains styled text.""",

    'TextMarginRightJustified':
        """The margin contains right justified styled text.""",

    # gcMarkerSymbol
    # pre-defined marker symbols
    'Circle':
        """A circle.""",

    'Rectangle':
        """A rectangle.""",

    'RightTriangle':
        """A triangle pointing to the right.""",

    'SmallRectangle':
        """A smaller rectangle.""",

    'RightArrow':
        """An arrow pointing to the right.""",

    'Invisible':
        """An invisible marker that allows code to track the movement of
        lines.""",

    'DownTriangle':
        """A triangle pointing down.""",

    'Minus':
        """A drawn minus sign.""",

    'Plus':
        """A drawn plus sign.""",

    'VerticalLine':
        """A vertical line drawn in the background colour.""",

    'BottomLeftCorner':
        """A bottom left corner drawn in the background colour.""",

    'LeftSideSplitter':
        """A vertical line with a centre right horizontal line drawn in the
        background colour.""",

    'BoxedPlus':
        """A drawn plus sign in a box.""",

    'BoxedPlusConnected':
        """A drawn plus sign in a connected box.""",

    'BoxedMinus':
        """A drawn minus sign in a box.""",

    'BoxedMinusConnected':
        """A drawn minus sign in a connected box.""",

    'RoundedBottomLeftCorner':
        """A rounded bottom left corner drawn in the background colour.""",

    'LeftSideRoundedSplitter':
        """A vertical line with a centre right curved line drawn in the
        background colour.""",

    'CircledPlus':
        """A drawn plus sign in a circle.""",

    'CircledPlusConnected':
        """A drawn plus sign in a connected box.""",

    'CircledMinus':
        """A drawn minus sign in a circle.""",

    'CircledMinusConnected':
        """A drawn minus sign in a connected circle.""",

    'Background':
        """No symbol is drawn but the line is drawn with the same background
        color as the marker's.""",

    'ThreeDots':
        """Three drawn dots.""",

    'ThreeRightArrows':
        """Three drawn arrows pointing right.""",

    'FullRectangle':
        """A full rectangle (ie. the margin background) using the marker's
        background color.""",

    'LeftRectangle':
        """A left rectangle (ie. the left part of the margin background) using
        the marker's background color.""",

    'Underline':
        """No symbol is drawn but the line is drawn underlined using the
        marker's background color.""",

    # gcWhitespaceVisibility
    # whitespace visibility modes. When whitespace is visible spaces are
    # displayed as small centred dots and tabs are displayed as light arrows
    # pointing to the right.
    'WsInvisible':
        """Whitespace is invisible.""",

    'WsVisible':
        """Whitespace is always visible.""",

    'WsVisibleAfterIndent':
        """Whitespace is visible after the whitespace used for indentation.""",

    # gcWrapMode
    # line wrap modes
    'WrapNone':
        """Lines are not wrapped.""",

    'WrapWord':
        """Lines are wrapped at word boundaries.""",

    'WrapCharacter':
        """Lines are wrapped at character boundaries.""",

    # gcWrapVisualFlag
    # line wrap visual flags
    'WrapFlagNone':
        """No wrap flag is displayed.""",

    'WrapFlagByText':
        """A wrap flag is displayed by the text.""",

    'WrapFlagByBorder':
        """A wrap flag is displayed by the border.""",

    # gcWrapIndentMode
    # line wrap indentation modes
    'WrapIndentFixed':
        """Wrapped sub-lines are indented by the amount set by
        setWrapVisualFlags().""",

    'WrapIndentSame':
        """Wrapped sub-lines are indented by the same amount as the first
        sub-line.""",

    'WrapIndentIndented':
        """ Wrapped sub-lines are indented by the same amount as the first
        sub-line plus one more level of indentation.""",
}


