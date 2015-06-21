from curses import initscr, wrapper


def getContents(path):

    # Dictionary containing sorted list directory contents in some fashion.
    # See -> lsdir's docstring.
    dirContents = tools.lsdir(path, True)

    # contains those dirs whose filetype is considered as 'dir' by DIRS
    dirs = [Content(fname, 'dir') for _type in DIRS for fname in dirContents[_type]]
    # contains those files whose filetype is considered as 'file' by FILES
    files = [Content(fname, 'file') for _type in FILES for fname in dirContents[_type]]

    # Single list containing dirs and files classes combined.
    contentsAll = []

    dirs = sorted(dirs, key=lambda x: x.name)
    files = sorted(files, key=lambda x: x.name)

    # Append Content objects in the order defined in PRINT_ORDER constant.
    for type in PRINT_ORDER:

        # Requires `dirs` and `files` lists to be existed.
        for item in locals()[type+'s']:

            # Append Content-object.
            contentsAll.append(item)

    # Return all contents
    return contentsAll


class Paths(object):

    """Paths manager"""

    def __init__(self, startPath):

        """Start with `startPath` as current path"""

        # Initialize path history with startPath
        self.pathHistory = [abspath(startPath)]

    def chPath(self, newPath):

        """Change the current path to newPath and return it"""

        # Last path
        lastPath = self.pathHistory[-1]

        # Append new absolute path to path history.
        self.pathHistory.append(join(abspath(lastPath), newPath))

        # Return the most recent path(the current path)
        return self.getHistory()

    def getHistory(self, history_depth=0):

        """Return the path from path history

        --Parameters--

        history_depth(int)(default=0):

          Range - [0, x] (x is no. of paths in the history)
          min value means *most recent path*
          max value means *oldest path*
        """

        return self.pathHistory[-(history_depth + 1)]

    def popHistory(self, history_depth=0):

        """Pop(remove & return) path from path history

        --Parameters--

        history_depth(int)(default=0):

          Range - [0, x] (x is no. of paths in the history)
          min value means *most recent path*
          max value means *oldest path*
        """

        # Remove every path after history_depth
        self.pathHistory = self.pathHistory[:-history_depth]

        # Return the required path
        return self.pathHistory[-1]


def main(stdscr):

    """Contains curses main loop"""

    # Configure standard screen.
    stdscr = config(stdscr)

    # default keyboard input
    stdscr_key = None

    # Path tracker : track every navigation from path to path
    pathHistory = [abspath('/')]

    # Get all contents
    contentsAll = getContents(pathHistory[-1])

    ### TEMPORARY ###
    browser = Browser(stdscr, contentsAll)

    # Main loop. Quits when keyboard input is 'q'
    while stdscr_key is not ord(KEYS['quit']):

        # Get input from keyboard.
        stdscr_key = stdscr.getch()

        # Enter/Return key pressed
        if stdscr_key == ord(KEYS['enter']):

            # Get selected Content from browser
            selected_content = browser.getSelected()

            # If it is a directory
            if selected_content.type == 'dir':

                # Gets new path
                newPath = join(abspath(pathHistory[-1]), selected_content.name)

                # Get new list of Contents
                contentsAll = getContents(newPath)

                # Set new contents
                browser.setContents(contentsAll)

                # Append new path to pathHistory
                pathHistory.append(newPath)

        # Arrow Up key pressed
        elif stdscr_key == KEYS['up']:
            # Move selection to previous element
            browser.Move(-1)

        # Arrow Down key pressed
        elif stdscr_key == KEYS['down']:
            # Move selection to next element.
            browser.Move(1)

        # Wait for 100 ms
        # TODO -> increase to decrease CPU cycles.
        stdscr.timeout(100)


if __name__ == "__main__":

    # Initializes curses screen.
    stdscr = initscr()

    # import configured `curses` module and other configurations.
    from config import *

    # import all required modules
    from imports import *

    # call `main` and wait till it exits.
    wrapper(main)
