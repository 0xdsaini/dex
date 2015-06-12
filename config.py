
"""defines curses configurations"""

from colorpairs import * # import color pairs

# Set up bold variable,
# BOLD[False] -> curses.A_NORMAL, BOLD[True] -> curses.A_BOLD
BOLD = [curses.A_NORMAL, curses.A_BOLD]

# Make curses invisible
curses.curs_set(0)

# Disable echoing typed character.
curses.noecho()
