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

if __name__ == '__main__':
    app = QtGui.QApplication([])
    editor = Editor()
    editor.show()
    app.exec_()
