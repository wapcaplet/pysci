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


    def assertColorsEqual(self, color_a, color_b):
        self.assertEqual(
            str(color_a.name()),
            str(color_b.name()),
        )


    def test_color_configuration(self):
        """Color configuration is correctly applied.
        """

        red = QtGui.QColor('#FF0000')
        green = QtGui.QColor('#00FF00')
        blue = QtGui.QColor('#0000FF')
        black = QtGui.QColor('#000000')
        grey = QtGui.QColor('#808080')
        white = QtGui.QColor('#FFFFFF')

        self.editor.configure(
            # Main foreground/background
            color = red,
            paper = white,
            # Margins
            marginsBackgroundColor = grey,
            marginsForegroundColor = black,
            # Call tips
            callTipsBackgroundColor = blue,
            callTipsForegroundColor = red,
            callTipsHighlightColor = grey,
            # Braces
            matchedBraceBackgroundColor = grey,
            matchedBraceForegroundColor = green,
            unmatchedBraceBackgroundColor = black,
            unmatchedBraceForegroundColor = red,
            # Indentation guides
            indentationGuidesBackgroundColor = red,
            indentationGuidesForegroundColor = green,
            # Selection
            selectionBackgroundColor = blue,
            selectionForegroundColor = white,
            # Misc
            edgeColor = green,
            caretLineBackgroundColor = white,

            # Tuple settings
            foldMarginColors = (red, white),

            # Whitespace (deprecated?)
            #whitespaceForegroundColor = blue,
            #whitespaceBackgroundColor = grey,
        )
        self.assertColorsEqual(self.editor.color(), red)
        self.assertColorsEqual(self.editor.paper(), white)

        # FIXME: Write getters for these - QsciScintilla doesn't provide them
        #self.assertEqual(self.editor.marginsBackgroundColor(), grey)
        #self.assertEqual(self.editor.marginsForegroundColor(), black)
        #self.assertEqual(self.editor.caretLineBackgroundColor(), white)
        #self.assertEqual(self.editor.foldMarginColors(), (red, white))

        # FIXME: Setting edge color always results in black, except when
        # setting it to the default red. Why? edgeColumn and edgeMode seem to
        # have no effect.
        #self.editor.setEdgeColumn(80)
        #self.editor.setEdgeMode(self.editor.EdgeBackground)
        #self.assertColorsEqual(self.editor.edgeColor(), green)

        # Modify colors and confirm that changes took effect
        self.editor.configure(
            color = green,
            paper = grey,
        )
        self.assertColorsEqual(self.editor.color(), green)
        self.assertColorsEqual(self.editor.paper(), grey)


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

