Future Plans
=================================

As of this writing, PySci is a fairly minimal wrapper around the existing
QsciScintilla widget. It provides a few convenience features, but nothing
earth-shattering. Here are some features that may appear in the future:

- Support for choosing syntax highlighting for any of the language lexers that
  QsciScintilla supports
- Direct attribute-based wrappers around the getter/setter methods
- Loading and saving of files, with auto-detection of syntax highlighting based
  on filename extension
- Loading and saving of PySci configuration preferences
- Built-in docstrings for the standard QsciScintilla methods


Missing methods
-------------------

QsciScintilla provides several "setter" methods with no "getter" counterpart.
For example, many of the methods for specifying colors:

- ``setMarginsBackgroundColor``
- ``setMarginsForegroundColor``
- ``setCaretLineBackgroundColor``
- etc.

Once a color is set, there's no way to retrieve it later. In other words, these
are **write-only** attributes.

Another feature that is lacking from QsciScintilla is the ability to easily
retrieve geometry information. For instance, what if you need to know the
Y-coordinate in screen pixels of a given line in your editor widget? Or a
bounding rectangle around the text in a given line? Many of the other PyQt4
widgets provide such methods, but QsciScintilla doesn't. PySci aims to remedy
this, making the widget fit more closely with its Qt counterparts.


