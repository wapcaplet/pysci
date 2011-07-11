# language.py

"""Language and lexer support for PySci.
"""

import os

# Language lexers and their file extensions
# (Name, extensions) tuples, where <Name> must match
# QsciLexer<Name>
language_extensions = (
    ('None', '.txt'),
    ('Bash', '.sh'),
    ('Batch', '.bat'),
    #('CMake', ''),
    ('CPP', '.cpp .h'),
    ('CSharp', '.cs'),
    ('CSS', '.css'),
    #('D', ''),
    ('Diff', '.diff'),
    #('Fortran', ''),
    #('Fortran77', ''),
    ('HTML', '.html'),
    #('IDL', ''),
    ('Java', '.java'),
    ('JavaScript', '.js'),
    #('Lua', ''),
    #('Makefile', ''),
    #('Pascal', ''),
    ('Perl', '.pl'),
    #('PostScript', ''),
    #('POV', ''),
    #('Properties', ''),
    ('Python', '.py .pyw'),
    ('Ruby', '.rb'),
    ('SQL', '.sql'),
    #('TCL', ''),
    #('TeX', ''),
    #('VHDL', ''),
    ('XML', '.xml .svg'),
    ('YAML', '.yaml'),
)

def guess_language(filename):
    """Guess the language based on the given filename's extension, and return
    the name of the language, or the string 'None' if no extension matches.
    """
    # Get the file's extension
    root, ext = os.path.splitext(filename)

    # See if any known language extensions match
    for language, extensions in language_extensions:
        if ext in extensions.split(' '):
            return language

    # No match -- asume plain text
    return 'None'


