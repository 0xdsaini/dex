# Copyright (c) 2015 ICRL
# See the file LICENSE for copying permission.

"""Configures curses module, defines other configurations and functions"""

from constants import *  # all constant configurations
from colorpairs import *  # all color pairs

# Set up bold variable,
# BOLD[False] -> curses.A_NORMAL, BOLD[True] -> curses.A_BOLD
BOLD = [curses.A_NORMAL, curses.A_BOLD]

# Make curses invisible
curses.curs_set(0)

# Disable echoing typed character.
curses.noecho()


def config(stdscr):

    """Standard screen configuration.
    Return configured screen."""

    # Enable use of KEY_UP, KEY_DOWN etc.
    stdscr.keypad(True)

    # Set background color
    stdscr.bkgd(" ", curses.color_pair(1))

    # Return configured standard screen
    return stdscr
