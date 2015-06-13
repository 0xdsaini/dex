from curses import initscr, wrapper
from curses import KEY_UP, KEY_DOWN # imports action keys

# alias of each supported *action key*
KEYS = {"quit": "q", "enter": '\n', "up": KEY_UP, "down": KEY_DOWN}


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

    # default keyboard input
    stdscr_key = None

    # Main loop. Quits when keyboard input is 'q'
    while stdscr_key is not ord(KEYS['quit']):

        # Get input from keyboard.
        stdscr_key = stdscr.getch()

        # Enter/Return key pressed
        if stdscr_key == KEYS['enter']:
            pass # TODO

        # Arrow Up key pressed
        elif stdscr_key == KEYS['up']:
            pass # TODO

        # Arrow Down key pressed
        elif stdscr_key == KEYS['down']:
            pass # TODO

        # Wait for 100 ms
        stdscr.timeout(100)


if __name__ == "__main__":

    # Initializes curses screen.
    stdscr = initscr()

    # import configured `curses` module and other configurations.
    from config import *

    # call `main` and wait till it exits.
    wrapper(main)
