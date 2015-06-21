"""module defines curses color pairs to be used by the importer program"""

import curses


try:

    # Start using curses colors
    curses.start_color()

    """Make following fg(foreground) bg(background) color pairs"""

    ## Color Pairs Specially For Files
    # BLUE & WHITE
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    # WHITE & BLUE
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    ## Color Pairs Specially For Directories
    # MAGENTA & WHITE
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    # WHITE & MAGENTA
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

    ## Color Pair For Author Credits
    # CYAN & BLACK
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)

except NameError:
    raise NameError(" Colors pairs initialization before main")
