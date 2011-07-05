Motivation
================

Although QsciScintilla is a rich and full-featured editor widget that works
nicely with PyQt4, its API is very C-like, and feels too low-level in the
context of a Python application. PySci was developed to bring a more idiomatic
Python approach to QsciScintilla.


Configuration
-------------------

QsciScintilla makes heavy use of enumerated types with individual getters and
setters for configuration settings::

    editor = QsciScintilla()
    editor.setWhitespaceVisibility(QsciScintilla.WsInvisible)
    editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
    editor.setWrapMode(QsciScintilla.WrapWord)

A more Pythonic library should allow the use of keyword arguments, and simple
string expressions, combined with the ability to configure several attributes at
once::

    editor.configure(
        whitespaceVisibility = 'WsInvisible',
        braceMatching = 'SloppyBraceMatch',
        wrapMode = 'WrapWord')

Considering the enormous number of methods in QsciScintilla for dealing with
configuration settings, it's a little surprising that a dedicated configuration
widget is not provided. If you've worked with QsciScintilla with any seriousness,
you've probably build an ad-hoc configuration widget yourself (and so has
everyone else). That's a shameful duplication of programming effort. PySci
provides a ready-made one to save you the trouble.


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


Docstrings
-------------------

Another feature lacking in the typical binary distribution of QsciScintilla is
the integrated docstrings that Pythonistas often depend on when programming.
It's a hassle to look up online documentation when it could be built into the
source code. PySci may eventually provide builtin docstrings for the standard
QsciScintilla methods.

