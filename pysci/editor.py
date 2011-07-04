# editor.py

__all__ = [
    'Editor',
]

from PyQt4 import QtGui, Qsci
from PyQt4.QtCore import SIGNAL

class Editor (Qsci.QsciScintilla):
    """Wrapper for ``QsciScintilla``.
    """
    # Marker identifiers
    ARROW = 8

    def __init__(self, parent, **config):
        Qsci.QsciScintilla.__init__(self, parent)
        self.configure(**Editor._default_config)
        self.configure(**config)
        self._connect_event_handlers()


    def configure(self, **config):
        """Configure the editor with the given settings.
        """
        for name, args in config.items():
            # Get the setter method ('setWhatEver')
            setter = getattr(self, 'set' + name[0].upper() + name[1:])
            # Multi-argument setting
            if isinstance(args, (tuple, list)):
                setter(*args)
            # Single-argument setting
            else:
                setter(args)

        # Adjust margin if line numbers are on
        if 'marginLineNumbers' in config and config['marginLineNumbers'] == (0, True):
            font_metrics = QtGui.QFontMetrics(self.font())
            self.setMarginWidth(0, font_metrics.width('00000') + 5)


    def _connect_event_handlers(self):
        """Connect event handler methods for the editor widget.
        """
        # Make margin 1 sensitive to clicks
        self.setMarginSensitivity(1, True)

        # Define markers
        self.markerDefine(Qsci.QsciScintilla.RightArrow, self.ARROW)

        # Connect signals
        self.connect(
            self,
            SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'),
            self.on_margin_clicked)
        self.connect(
            self,
            SIGNAL('linesChanged()'),
            self.on_lines_changed)
        self.connect(
            self,
            SIGNAL('cursorPositionChanged(int, int)'),
            self.on_cursor_position_changed)
        self.connect(
            self,
            SIGNAL('indicatorClicked(int, int, Qt::KeyboardModifiers)'),
            self.on_indicator_clicked)


    # Event handlers
    #
    def on_margin_clicked(self, margin, line, state):
        if self.markersAtLine(line) != 0:
            self.markerDelete(line, self.ARROW)
        else:
            self.markerAdd(line, self.ARROW)
        print("margin_clicked(%s, %s, %s)" % (margin, line, state))

    def on_lines_changed(self):
        print("lines_changed")

    def on_cursor_position_changed(self, line, index):
        print("cursor_position_changed(%s, %s)" % (line, index))
        #height = self.textHeight(line)
        #print("  height: %d" % height)
        #rect = self.childrenRect()
        #print("  rect: (%d, %d), (%d, %d)" % (rect.x(), rect.y(), rect.width(), rect.height()))

    def on_indicator_clicked(self, line, index, state):
        print("indicator_clicked(%s, %s, %s)" % (line, index, state))


