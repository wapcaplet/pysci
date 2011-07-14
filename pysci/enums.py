# enums.py

"""Wrapper for Qsci.QsciScintilla enumerations.
"""

try:
    from PyQt4 import Qsci
except ImportError:
    print("Please install PyQt4.")

QS = Qsci.QsciScintilla
enum_types = {
    # annotation display styles
    QS.AnnotationDisplay: (
        ('AnnotationHidden', QS.AnnotationHidden),
        ('AnnotationStandard', QS.AnnotationStandard),
        ('AnnotationBoxed', QS.AnnotationBoxed),
    ),

    # sources for auto-completion lists.
    QS.AutoCompletionSource: (
        ('AcsNone', QS.AcsNone),
        ('AcsAll', QS.AcsAll),
        ('AcsDocument', QS.AcsDocument),
        ('AcsAPIs', QS.AcsAPIs),
    ),

    # brace matching modes. The character pairs (), [] and () are treated as
    # braces. The Python lexer will also match a : with the end of the
    # corresponding indented block.
    QS.BraceMatch: (
        ('NoBraceMatch', QS.NoBraceMatch),
        ('StrictBraceMatch', QS.StrictBraceMatch),
        ('SloppyBraceMatch', QS.SloppyBraceMatch),
    ),

    # call tip styles
    QS.CallTipsStyle: (
        ('CallTipsNone', QS.CallTipsNone),
        ('CallTipsNoContext', QS.CallTipsNoContext),
        ('CallTipsNoAutoCompletionContext', QS.CallTipsNoAutoCompletionContext),
        ('CallTipsContext', QS.CallTipsContext),
    ),

    # edge modes for long lines
    QS.EdgeMode: (
        ('EdgeNone', QS.EdgeNone),
        ('EdgeLine', QS.EdgeLine),
        ('EdgeBackground', QS.EdgeBackground),
    ),

    # end-of-line modes
    QS.EolMode: (
        ('EolWindows', QS.EolWindows),
        ('EolUnix', QS.EolUnix),
        ('EolMac', QS.EolMac),
    ),

    # styles for the folding margin
    QS.FoldStyle: (
        ('NoFoldStyle', QS.NoFoldStyle),
        ('PlainFoldStyle', QS.PlainFoldStyle),
        ('CircledFoldStyle', QS.CircledFoldStyle),
        ('BoxedFoldStyle', QS.BoxedFoldStyle),
        ('CircledTreeFoldStyle', QS.CircledTreeFoldStyle),
        ('BoxedTreeFoldStyle', QS.BoxedTreeFoldStyle),
    ),

    # margin types
    QS.MarginType: (
        ('SymbolMargin', QS.SymbolMargin),
        ('SymbolMarginDefaultForegroundColor', QS.SymbolMarginDefaultForegroundColor),
        ('SymbolMarginDefaultBackgroundColor', QS.SymbolMarginDefaultBackgroundColor),
        ('NumberMargin', QS.NumberMargin),
        ('TextMargin', QS.TextMargin),
        ('TextMarginRightJustified', QS.TextMarginRightJustified),
    ),

    # pre-defined marker symbols
    QS.MarkerSymbol: (
        ('Circle', QS.Circle),
        ('Rectangle', QS.Rectangle),
        ('RightTriangle', QS.RightTriangle),
        ('SmallRectangle', QS.SmallRectangle),
        ('RightArrow', QS.RightArrow),
        ('Invisible', QS.Invisible),
        ('DownTriangle', QS.DownTriangle),
        ('Minus', QS.Minus),
        ('Plus', QS.Plus),
        ('VerticalLine', QS.VerticalLine),
        ('BottomLeftCorner', QS.BottomLeftCorner),
        ('LeftSideSplitter', QS.LeftSideSplitter),
        ('BoxedPlus', QS.BoxedPlus),
        ('BoxedPlusConnected', QS.BoxedPlusConnected),
        ('BoxedMinus', QS.BoxedMinus),
        ('BoxedMinusConnected', QS.BoxedMinusConnected),
        ('RoundedBottomLeftCorner', QS.RoundedBottomLeftCorner),
        ('LeftSideRoundedSplitter', QS.LeftSideRoundedSplitter),
        ('CircledPlus', QS.CircledPlus),
        ('CircledPlusConnected', QS.CircledPlusConnected),
        ('CircledMinus', QS.CircledMinus),
        ('CircledMinusConnected', QS.CircledMinusConnected),
        ('Background', QS.Background),
        ('ThreeDots', QS.ThreeDots),
        ('ThreeRightArrows', QS.ThreeRightArrows),
        #('FullRectangle', QS.FullRectangle),
        #('LeftRectangle', QS.LeftRectangle),
        #('Underline', QS.Underline),
    ),

    # whitespace visibility modes. When whitespace is visible spaces are
    # displayed as small centred dots and tabs are displayed as light arrows
    # pointing to the right.
    QS.WhitespaceVisibility: (
        ('WsInvisible', QS.WsInvisible),
        ('WsVisible', QS.WsVisible),
        ('WsVisibleAfterIndent', QS.WsVisibleAfterIndent),
    ),

    # line wrap modes
    QS.WrapMode: (
        ('WrapNone', QS.WrapNone),
        ('WrapWord', QS.WrapWord),
        ('WrapCharacter', QS.WrapCharacter),
    ),

    # line wrap visual flags
    QS.WrapVisualFlag: (
        ('WrapFlagNone', QS.WrapFlagNone),
        ('WrapFlagByText', QS.WrapFlagByText),
        ('WrapFlagByBorder', QS.WrapFlagByBorder),
    ),
}

# Just the enumeration names (strings)
enum_names = [
    name
    for name_values in enum_types.values()
    for (name, value) in name_values
]

class BadEnum (Exception):
    """Bad (unknown or failed) enumeration name.
    """
    def __init__(self, name):
        super(BadEnum, self).__init__("Enumeration unknown: '%s'" % name)


def enum_value(enum_name):
    """Return the Qsci.QsciScintilla value for the given enumeration name.
    """
    if enum_name not in enum_names:
        raise BadEnum(name)

    # Some officially documented enums don't work; catch them
    # and raise BadEnum instead of KeyError
    try:
        return Qsci.QsciScintilla.__dict__[enum_name]
    except KeyError:
        raise BadEnum(name)


def enum_string(enum_value):
    """Return the string version of the given enumeration value,
    or raise `BadEnum` if there's no such enumeration value.
    """
    enum_type = type(enum_value)

    # Invalid enum type?
    if enum_type not in enum_types:
        raise BadEnum(enum_value)

    # Construct a lookup table indexed by enumeration value
    lookup = dict((value, name) for (name, value) in enum_types[enum_type])

    # Invalid enum value?
    if enum_value not in lookup:
        raise BadEnum(enum_value)

    return lookup[enum_value]


