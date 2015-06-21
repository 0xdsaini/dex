"""Defines constant variables"""

from curses import KEY_UP, KEY_DOWN, KEY_BACKSPACE  # imports action keys

# alias of each supported *action key*
KEYS = {"quit": "q", "enter": '\n', "up": KEY_UP, "down": KEY_DOWN,
        "back": KEY_BACKSPACE}

# properties of files and directories when normal and when selected.
ELEMENT_PROPERTIES = {"dir": ((False, 3), (True, 4)),
                      "file": ((False, 1), (True, 2))}

# Element line prefixes(placeholders)
ELEMENT_PREFIX = {"dir": '+ ', "file": '  '}

# filetypes to be considered as directories
DIRS = ('mountpoint', 'dir')

# filetypes to be considered as files.
FILES = ('file', 'link', 'other')

# printing preference of different filetypes.
PRINT_ORDER = ('dir', 'file')

# Special directories.
SPECIAL_DIRS = {'BACK_DIR': '..', 'CURR_DIR': '.'}

# determines how contents will be sorted.
CONTENTS_SORTFUNC = lambda x: x.lower()
