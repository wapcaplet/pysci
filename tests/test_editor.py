from pysci.editor import PySci
from unittest import TestCase
from PyQt4 import QtGui, Qsci

"""
Might be able to glean something from this:
    http://www.commandprompt.com/community/pyqt/x5255

QTestLib manual (C++ oriented):
    http://doc.qt.nokia.com/4.7-snapshot/qtestlib-manual.html

Also, some potential insight here:
    http://nullege.com/codes/show/src%40g%40w%40gws-HEAD%40trunk%40tests%40frame.py/56/PyQt4.QtTest.QTest.keyClick/python
"""

class PySciTest (TestCase):
    def setUp(self):
        self.app = QtGui.QApplication(['-nograb', '-sync'])
        self.editor = PySci()


    def tearDown(self):
        self.app.quit()



class PySciConfigTest (PySciTest):
    """Test PySci configuration features
    """
    def assertColorsEqual(self, color_a, color_b):
        """Assert that the two colors have the same name
        (even if they are not the same QColor object).
        """
        self.assertEqual(
            str(color_a.name()),
            str(color_b.name()),
        )


    def test_get_set_config(self):
        """get_config() returns the value set by set_config().
        """
        self.editor.set_config('indentationsUseTabs', True)
        self.assertEqual(self.editor.get_config('indentationsUseTabs'), True)
        self.editor.set_config('tabWidth', 3)
        self.assertEqual(self.editor.get_config('tabWidth'), 3)


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
            autoCompletionCaseSensitivity = False,
            autoCompletionReplaceWord = True,
            selectionToEol = True,
        )
        self.assertEqual(self.editor.tabIndents(), True)
        self.assertEqual(self.editor.indentationsUseTabs(), False)
        self.assertEqual(self.editor.backspaceUnindents(), True)
        self.assertEqual(self.editor.autoIndent(), False)
        self.assertEqual(self.editor.indentationGuides(), False)
        self.assertEqual(self.editor.eolVisibility(), True)
        self.assertEqual(self.editor.autoCompletionCaseSensitivity(), False)
        self.assertEqual(self.editor.autoCompletionReplaceWord(), True)
        self.assertEqual(self.editor.selectionToEol(), True)



    def test_custom_getters(self):
        """Custom attribute-getters return correct values.
        """
        # caretLineVisible
        self.editor.configure(caretLineVisible=True)
        self.assertEqual(self.editor.caretLineVisible(), True)
        self.editor.configure(caretLineVisible=False)
        self.assertEqual(self.editor.caretLineVisible(), False)

        # caretLineBackgroundColor
        white = QtGui.QColor('#FFFFFF')
        red = QtGui.QColor('#FF0000')
        self.editor.configure(caretLineBackgroundColor=white)
        self.assertEqual(self.editor.caretLineBackgroundColor(), white)
        self.editor.configure(caretLineBackgroundColor=red)
        self.assertEqual(self.editor.caretLineBackgroundColor(), red)


    def test_numeric_configuration(self):
        """Numeric configuration values are correctly applied.
        """
        self.editor.configure(
            tabWidth = 4,
            edgeColumn = 72,
            # Deprecated or new?
            #extraAscent = 2,
            #extraDescent = 3,
        )
        self.assertEqual(self.editor.tabWidth(), 4)
        self.assertEqual(self.editor.edgeColumn(), 72)
        #self.assertEqual(self.editor.extraAscent(), 2)
        #self.assertEqual(self.editor.extraDescent(), 3)


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

            # Tuple settings
            foldMarginColors = (red, white),

            # Whitespace (deprecated or new?)
            #whitespaceForegroundColor = blue,
            #whitespaceBackgroundColor = grey,
        )
        self.assertColorsEqual(self.editor.color(), red)
        self.assertColorsEqual(self.editor.paper(), white)

        # FIXME: Write getters for these - QsciScintilla doesn't provide them
        #self.assertEqual(self.editor.marginsBackgroundColor(), grey)
        #self.assertEqual(self.editor.marginsForegroundColor(), black)
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


class PySciGeometryTest (PySciTest):
    """Test PySci geometry methods.
    """
    def test_line_rect(self):
        """Line geometry rectangle is correctly calculated.
        """
        self.editor.setText("Hello world")
        rect = self.editor.line_rect(0)
        self.assertEqual(rect, (62, 0, 88, 16))


class PySciBufferTest (PySciTest):
    """Test PySci buffer methods.
    """
    def test_modified_get(self):
        """modified() retrieves the isModified flag.
        """
        self.editor.setText('hello')
        self.editor.setModified(True)
        self.assertEqual(self.editor.modified(), True)
        self.editor.setModified(False)
        self.assertEqual(self.editor.modified(), False)


    def test_modified_set(self):
        """modified(flag) sets the isModified flag.
        """
        self.editor.setText('hello')
        self.editor.modified(True)
        self.assertEqual(self.editor.isModified(), True)
        self.editor.modified(False)
        self.assertEqual(self.editor.isModified(), False)


    def test_clear(self):
        """clear() empties the buffer.
        """
        self.editor.setText('hello')
        self.assertEqual(self.editor.text(), 'hello')
        self.editor.clear()
        self.assertEqual(self.editor.text(), '')


class PySciLanguageTest (PySciTest):
    """Test PySci language methods.
    """
    def test_default_language(self):
        """New editors initially have no syntax highlighting defined.
        """
        self.assertEqual(self.editor.language(), 'None')
        self.assertEqual(self.editor.lexer(), None)


    def test_get_set_language(self):
        """language() returns the value set by setLanguage().
        """
        self.editor.setLanguage('Python')
        self.assertEqual(self.editor.language(), 'Python')
        self.editor.setLanguage('Ruby')
        self.assertEqual(self.editor.language(), 'Ruby')
        self.editor.setLanguage('JavaScript')
        self.assertEqual(self.editor.language(), 'JavaScript')


    def test_language_lexer(self):
        """setLanguage() sets the correct lexer.
        """
        self.editor.setLanguage('Python')
        lexer_class = self.editor.lexer().__class__.__name__
        self.assertEqual(lexer_class, 'QsciLexerPython')

        self.editor.setLanguage('Ruby')
        lexer_class = self.editor.lexer().__class__.__name__
        self.assertEqual(lexer_class, 'QsciLexerRuby')


    def test_no_language_lexer(self):
        """setLanguage() can be used to disable the lexer.
        """
        self.editor.setLanguage(None)
        lexer = self.editor.lexer()
        self.assertEqual(lexer, None)

        self.editor.setLanguage('None')
        lexer = self.editor.lexer()
        self.assertEqual(lexer, None)

        self.editor.setLanguage('')
        lexer = self.editor.lexer()
        self.assertEqual(lexer, None)


    def test_invalid_language(self):
        """setLanguage() raises an exception on invalid language name.
        """
        self.assertRaises(ValueError, self.editor.setLanguage, 'Z++')
        self.assertRaises(ValueError, self.editor.setLanguage, 'Bogus')
        self.assertRaises(ValueError, self.editor.setLanguage, 'NoSuchLanguage')


