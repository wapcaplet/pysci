# editor.py

"""Defines a QsciScintilla wrapper called `Editor`.

Desirable features:

    - Directly get/set attributes instead of using getters/setters
      (in some cases, not even getters exist, for example 'marginsFont')
      ex.: editor.font = ('Courier New', 10)

Could use Qsci.QsciScintilla.SendScintilla() with predefined signals for things
that aren't already implemented:

    http://www.scintilla.org/ScintillaDoc.html

"""

__all__ = [
    'Editor',
]

from PyQt4 import QtGui, Qsci
from settings import _default_config
from enums import enum_value

class Editor (Qsci.QsciScintilla):
    """Wrapper for ``QsciScintilla``.
    """
    def __init__(self, parent=None, **config):
        super(Editor, self).__init__(parent)
        self.configure(**_default_config)
        self.configure(**config)


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
            elif isinstance(args, (str, unicode)):
                setter(enum_value(args))

            # Single-argument setting
            else:
                setter(args)

        # Adjust margin if line numbers are on
        if 'marginLineNumbers' in config and config['marginLineNumbers'] == (0, True):
            font_metrics = QtGui.QFontMetrics(self.font())
            self.setMarginWidth(0, font_metrics.width('00000') + 5)


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


    def markerDefine(self, marker, markerNumber=-1):
        """Define a type of marker using the symbol sym with the marker number
        markerNumber. If markerNumber is -1 then the marker number is
        automatically allocated. The marker number is returned or -1 if too
        many types of marker have been defined.

        Markers are small geometric symbols and characters used, for example,
        to indicate the current line or, in debuggers, to indicate breakpoints.
        If a margin has a width of 0 then its markers are not drawn, but their
        background colours affect the background colour of the corresponding
        line of text.

        There may be up to 32 types of marker defined at a time and each line
        of text has a set of marker instances associated with it. Markers are
        drawn according to their numerical identifier. Markers try to move with
        their text by tracking where the start of their line moves to. For
        example, when a line is deleted its markers are added to previous
        line's markers.

        Each marker type is identified by a marker number. Each instance of a
        marker is identified by a marker handle.
        """
        pass


if __name__ == '__main__':
    app = QtGui.QApplication([])
    editor = Editor()
    editor.show()
    app.exec_()

