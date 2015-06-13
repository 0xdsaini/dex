from curses import initscr, wrapper


def config(stdscr):

    """Standard screen configuration.
    Return configured screen."""

    # Enable use of KEY_UP, KEY_DOWN etc.
    stdscr.keypad(True)

    # Set background color
    stdscr.bkgd(" ", curses.color_pair(1))

    # Return configured standard screen
    return stdscr


def main(stdscr):

    """Contains curses main loop"""

    # Configure standard screen.
    stdscr = config(stdscr)

    # Wait for user input.
    stdscr.getch()


if __name__ == "__main__":

    # Initializes curses screen.
    stdscr = initscr()

    # import configured `curses` module and other configurations.
    from config import *

    # call `main` and wait till it exits.
    wrapper(main)
