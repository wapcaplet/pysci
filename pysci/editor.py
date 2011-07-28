# editor.py

"""Defines a QsciScintilla wrapper called `PySci`.
"""

__all__ = [
    'PySci',
]

try:
    from PyQt4 import QtGui, Qsci
except ImportError:
    print("Please install PyQt4.")

from enums import enum_string, enum_values, BadEnum
from util import bgr_int_to_rgb
from language import guess_language


class PySci (Qsci.QsciScintilla):
    """Wrapper for ``QsciScintilla``.
    """

    def __init__(self, parent=None, **config):
        super(PySci, self).__init__(parent)
        self._set_default_config()
        # Override defaults with any customizations
        self.configure(**config)


    def _set_default_config(self):
        """Set default configuration settings.
        """
        self.configure(
            language = 'None',

            # Flags and numeric values
            tabIndents = True,
            tabWidth = 4,
            indentationsUseTabs = False,
            backspaceUnindents = True,
            autoIndent = False,
            indentationGuides = False,
            eolVisibility = False,
            edgeColumn = 80,
            caretLineVisible = True,
            marginLineNumbers = (0, True),

            # Fonts
            font = QtGui.QFont('Courier New', 10),
            marginsFont = QtGui.QFont('Courier New', 10),

            # Colors
            edgeColor = QtGui.QColor('#FF0000'),
            caretLineBackgroundColor = QtGui.QColor('#F0F0F0'),
            marginsBackgroundColor = QtGui.QColor('#C0C0C0'),
            marginsForegroundColor = QtGui.QColor('#000000'),
            foldMarginColors = (QtGui.QColor('#AAAAFF'), QtGui.QColor('#333300')),

            # Whitespace: Ws(Invisible|Visible|VisibleAfterIndent)
            whitespaceVisibility = 'WsInvisible',
            # Edge mode: Edge(None|Line|Background)
            edgeMode = 'EdgeLine',
            # Brace matching: (No|Strict|Sloppy)BraceMatch
            braceMatching = 'SloppyBraceMatch',
            # Folding: (No|Plain|Circled|Boxed|CircledTree|BoxedTree)FoldStyle
            folding = 'NoFoldStyle',
            # Wrap mode: Wrap(None|Word|Character)
            wrapMode = 'WrapWord',
        )


    ###
    ### Extensions
    ###

    def get_config(self, name, *args):
        """Return the current configuration setting for attribute ``name``.
        If ``name`` refers to an enumerated setting, return the string version
        of that enumeration.
        """
        getter = getattr(self, name)
        value = getter(*args)
        try:
            return enum_string(value)
        except BadEnum:
            return value


    def set_config(self, name, value):
        """Set the current configuration setting for attribute ``name``.
        """
        conf = {name: value}
        self.configure(**conf)


    def configure(self, **config):
        """Configure the editor with the given settings.

        Accepts ``keyword=value`` arguments for any attribute ``foo`` that is
        normally set via a ``setFoo`` method.

        For example, instead of this:

            >>> editor.setEdgeColor(QFont('Courier New', 10))
            >>> editor.setEolVisibility(True)
            >>> editor.setEdgeColumn(80)

        This method allows you to do this:

            >>> editor.configure(
            ...     edgeColor = QFont('Courier New', 10),
            ...     eolVisibility = True,
            ...     edgeColumn = 80)

        """
        for name, args in config.items():
            # Get the setter method ('setWhatEver')
            setter = getattr(self, 'set' + name[0].upper() + name[1:])

            # Handle setters that accept multiple arguments
            # (like marginLineNumbers)
            if isinstance(args, (tuple, list)):
                setter(*args)

            # Convert strings to enum value
            elif args in enum_values:
                setter(enum_values[args])

            # Single-argument setting
            else:
                setter(args)

        # Adjust margin if line numbers are on
        if 'marginLineNumbers' in config:
            if config['marginLineNumbers'] == (0, True):
                font_metrics = QtGui.QFontMetrics(self.font())
                self.setMarginWidth(0, font_metrics.width('00000') + 5)
            else:
                self.setMarginWidth(0, 0)


    def line_rect(self, line_number):
        """Return (x, y, width, height) of the text on ``line_number``.
        """
        pos = self.positionFromLineIndex(line_number, 0)
        x = self.SendScintilla(self.SCI_POINTXFROMPOSITION, 0, pos)
        y = self.SendScintilla(self.SCI_POINTYFROMPOSITION, 0, pos)
        # FIXME: Do we need to use a specific styleNumber here?
        width = self.SendScintilla(self.SCI_TEXTWIDTH, 0, self.text(line_number))
        height = self.textHeight(line_number)

        return (x, y, width, height)


    # Buffer content operations

    def modified(self, set_modified=None):
        """Get or set the modification status of the editor.
        If ``set_modified`` is True or False, set the modification status;
        otherwise, return current modification status (True or False).
        """
        if set_modified in (True, False):
            self.setModified(set_modified)
        else:
            return self.isModified()


    def clear(self):
        """Clear the contents of the editor.
        """
        self.setText('')
        self.modified(False)


    def load(self, filename):
        """Load the given file into the editor.
        """
        infile = open(filename, 'r')
        self.setText(''.join(infile.readlines()))
        self.modified(False)
        self.setLanguage(guess_language(filename))


    def save(self, filename):
        """Save the editor contents to the given filename.
        """
        outfile = open(filename, 'w')
        outfile.write(self.text())
        self.modified(False)

        QtGui.QMessageBox.information(self, 'Success', 'Saved: "%s"' % filename)


    # Language and syntax highlighting
    # Note: These follow the getter/setter pattern of other
    # QsciScintilla settings, to allow `configure` to manipulate them.

    def language(self):
        """Getter for language.
        """
        lexer = self.lexer()
        if lexer:
            return lexer.language()
        else:
            return 'None'


    def setLanguage(self, language):
        """Set syntax highlighting to the given language.
        If ``language`` is ``None``, ``'None'`` or empty, then
        syntax highlighting is disabled.
        """
        if not language or language == 'None':
            print("Disabling syntax highlighting")
            lexer = None
        else:
            print("%s syntax highlighting" % language)
            try:
                lexer = getattr(Qsci, 'QsciLexer%s' % language)(self)
            except AttributeError:
                raise ValueError("Unknown language: '%s'" % language)
            lexer.setFont(self.font())

        self.setLexer(lexer)


    ###
    ### The Missing Getters
    ###

    def caretLineVisible(self):
        """Return the ``caretLineVisible`` attribute (True or False).
        """
        return self.SendScintilla(self.SCI_GETCARETLINEVISIBLE)


    def caretLineBackgroundColor(self):
        """Return the ``caretLineBackgroundColor`` as a QColor.
        """
        # TODO: Support alpha?
        bgr_int = self.SendScintilla(self.SCI_GETCARETLINEBACK)
        r, g, b = bgr_int_to_rgb(bgr_int)
        return QtGui.QColor(r, g, b)

