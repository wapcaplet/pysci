from pysci.editor import Editor
from unittest import TestCase
from PyQt4 import QtGui, Qsci

class EditorTest (TestCase):
    """Test the Editor widget.
    """
    def setUp(self):
        self.app = QtGui.QApplication(['-sync'])
        self.editor = Editor()
        #self.editor.show()


    def test_boolean_configuration(self):
        """Basic configuration settings are applied.
        """
        self.editor.configure(
            tabIndents = True,
            indentationsUseTabs = False,
            backspaceUnindents = True,
            autoIndent = False,
            indentationGuides = False,
            eolVisibility = True,
            caretLineVisible = True,
            autoCompletionCaseSensitivity = False,
            autoCompletionReplaceWord = True,
        )
        self.assertEqual(self.editor.tabIndents(), True)
        self.assertEqual(self.editor.indentationsUseTabs(), False)
        self.assertEqual(self.editor.backspaceUnindents(), True)
        self.assertEqual(self.editor.autoIndent(), False)
        self.assertEqual(self.editor.indentationGuides(), False)
        self.assertEqual(self.editor.eolVisibility(), True)
        self.assertEqual(self.editor.autoCompletionCaseSensitivity(), False)
        self.assertEqual(self.editor.autoCompletionReplaceWord(), True)

        # FIXME: Write getters for these - QsciScintilla doesn't provide them
        #self.assertEqual(self.editor.caretLineVisible(), True)


    def test_numeric_configuration(self):
        """Numeric configuration values are correctly applied.
        """
        self.editor.configure(
            tabWidth = 4,
            edgeColumn = 72,
        )
        self.assertEqual(self.editor.tabWidth(), 4)
        self.assertEqual(self.editor.edgeColumn(), 72)


    def test_tuple_configuration(self):
        """Tuple-based configuration values are correctly applied.
        """
        self.editor.configure(
            marginLineNumbers = (0, True),
        )
        self.assertEqual(self.editor.marginLineNumbers(0), True)


    def test_font_configuration(self):
        """Font configuration is correctly applied.
        """
        courier = QtGui.QFont('Courier New', 10)

        self.editor.configure(
            font = courier,
            marginsFont = courier,
        )

        self.assertEqual(self.editor.font(), courier)


    def test_color_configuration(self):
        """Color configuration is correctly applied.
        """
        red = QtGui.QColor('#FF0000')
        grey = QtGui.QColor('#C0C0C0')
        white = QtGui.QColor('#FFFFFF')
        black = QtGui.QColor('#000000')

        self.editor.configure(
            edgeColor = red,
            marginsBackgroundColor = grey,
            marginsForegroundColor = black,
            caretLineBackgroundColor = white,
            foldMarginColors = (red, white),
        )
        self.assertEqual(self.editor.edgeColor(), red)

        # FIXME: Write getters for these - QsciScintilla doesn't provide them
        #self.assertEqual(self.editor.marginsBackgroundColor(), grey)
        #self.assertEqual(self.editor.marginsForegroundColor(), black)
        #self.assertEqual(self.editor.caretLineBackgroundColor(), white)
        #self.assertEqual(self.editor.foldMarginColors(), (red, white))


    def test_color_string_configuration(self):
        """Color string configuration is correctly applied.
        """
        colors = [
            '#FF0000',
            '#C0C0C0',
            '#FFFFFF',
            '#000000',
        ]

        for color in colors:
            self.editor.configure(edgeColor = color)
            expect = str(color).lower()
            actual = str(self.editor.edgeColor().name()).lower()
            self.assertEqual(expect, actual)


    def test_enum_configuration(self):
        """Enumeration-based configuration is correctly applied.
        """
        ENUM = Qsci.QsciScintilla

        self.editor.configure(
            whitespaceVisibility = ENUM.WsInvisible,
            edgeMode = ENUM.EdgeNone,
            braceMatching = ENUM.SloppyBraceMatch,
            folding = ENUM.NoFoldStyle,
            wrapMode = ENUM.WrapWord,
        )

        self.assertEqual(self.editor.whitespaceVisibility(), ENUM.WsInvisible)
        self.assertEqual(self.editor.edgeMode(), ENUM.EdgeNone)
        self.assertEqual(self.editor.braceMatching(), ENUM.SloppyBraceMatch)
        self.assertEqual(self.editor.folding(), ENUM.NoFoldStyle)
        self.assertEqual(self.editor.wrapMode(), ENUM.WrapWord)


    def test_enum_string_configuration(self):
        """Enumeration string-based configuration is correctly applied.
        """
        ENUM = Qsci.QsciScintilla

        self.editor.configure(
            whitespaceVisibility = 'WsInvisible',
            edgeMode = 'EdgeNone',
            braceMatching = 'SloppyBraceMatch',
            folding = 'NoFoldStyle',
            wrapMode = 'WrapWord',
        )

        self.assertEqual(self.editor.whitespaceVisibility(), ENUM.WsInvisible)
        self.assertEqual(self.editor.edgeMode(), ENUM.EdgeNone)
        self.assertEqual(self.editor.braceMatching(), ENUM.SloppyBraceMatch)
        self.assertEqual(self.editor.folding(), ENUM.NoFoldStyle)
        self.assertEqual(self.editor.wrapMode(), ENUM.WrapWord)


    def test_line_rect(self):
        """Line geometry rectangle is correctly calculated.
        """
        self.editor.setText("Hello world")
        rect = self.editor.line_rect(0)
        self.assertEqual(rect, (62, 0, 88, 16))

