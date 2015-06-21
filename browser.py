"""Contains Browser class"""

from helpers import prepareLine


class Browser(object):

    """Browses a list of contents on screen."""

    def __init__(self, stdscr, contents):

        """Takes curses `screen` to be used for rendering and, a list of
        Contents(of Content-type) to be rendered and browsed.

        1) Each Content in `contents` member have a index associated
           with it.

        2) selectIndex member keeps track of whether a specific content is
           selected by storing its index in itself.

        3) minSelectIndex member is the lower limit of `selectIndex` member
           i.e. It limits `selectIndex` to be no less than it(minSelectIndex)
           if co-operated by Move() method.

        4) _update_dims_() method gets the most recent screen dimensions(y, x)
           and updates `dims` member whenever it is called.

        4) _print_elements_() method renders each content of `contents` on the
           screen(provided at the time of initialization) in the same order as
           provided in the list stopping rendering as soon as it hits the
           bottom of screen.

           4.1) Before rendering, each content gets prepared(to be rendered)
                and gets it properties(color properties etc.) from prepareLine
                function(from helpers module).

        5) Move() method defines the `maxSelectIndex`(upper limit of
           `selectIndex`) and moves the `selectIndex` pointer by `moveSteps` if
           the resulting selectIndex lies somewhere between `minSelectIndex`
           and `maxSelectIndex`(both inclusive).

           5.1) With contrary to `minSelectIndex`, `maxSelectIndex` is not a
                constant, it depends on multiple things which may require to be
                updated each time before being accessed.

        """

        # Standard screen
        self.stdscr = stdscr

        # list containing Content-objects. To be printed on screen.
        self.contents = contents

        # element selection index.
        self.selectIndex = 1

        # start slice of contents
        self.sliceIndex = 0

        #### TEMPORARY ####
        self._update_dims_()

        # Minimum index to be selected
        self.minSelectIndex = 1

        # Maximum index to be selected
        self.maxSelectIndex = len(self.contents)

        # render contents
        self._print_elements_()

    def _update_dims_(self):

        """Get recent, maximum standard screen dimensions and updates
        self.dims"""

        self.dims = self.stdscr.getmaxyx()

    def _print_elements_(self):

        """Renders directory contents on screen"""

        # Erase standard screen.
        self.stdscr.erase()

        # ensures to get updated standard screen dimensions.
        self._update_dims_()

        # height of standard screen.
        height = self.dims[0]

        # width of standard screen.
        width = self.dims[1]

        # local selection index. Index of elements of screen, not the index of
        # elements of contents.
        localIndex = self.selectIndex - self.sliceIndex

        # If local selection is greater than height
        if localIndex > height:

            # Increase slicing to scroll down
            self.sliceIndex = self.selectIndex - height

            # Stay at the last element
            localIndex = height

        # If  local selection is less than 0
        elif localIndex <= 0:

            # Decrease slicing to scroll up
            self.sliceIndex = self.selectIndex - 1

            # Stay at the first element
            localIndex = 1

        # loop through all contents.
        for curr_line, item in enumerate(self.contents[self.sliceIndex:]):

            # Whether to stop rendering lines(due to standard screen limits)
            if curr_line == height:
                break

            # boolean -> whether to select current item.
            selectCurrent = (curr_line == localIndex - 1)

            # Prepare current elements and determine its properties.
            currElement, properties = prepareLine(item, selectCurrent, width)

            # Render currElement
            self.stdscr.addstr(curr_line, 0, currElement, properties)

    def setContents(self, contents):

        """set contents' list.
        Primarily developed to change contents' list"""

        # change contents list
        self.contents = contents

        # Change maximum select index
        self.maxSelectIndex = len(self.contents)

        # Restore to defaults.
        self.selectIndex = 1

        # renders it
        self._print_elements_()

    def getContents(self):

        """Return contents' list"""

        # Return contents
        return self.contents

    def getSelected(self):

        """Return selected content"""

        return self.contents[self.selectIndex - 1]

    def Move(self, moveSteps):

        """Move selection by `moveSteps`.
        (+)ve `moveSteps` moves selection forward.
        (-)ve `moveSteps` moves selection backward.
        """

        # boolean expression to determine whether to move `selectIndex`
        should_move = self.minSelectIndex <= self.selectIndex + moveSteps and\
            self.maxSelectIndex >= self.selectIndex + moveSteps

        if should_move:

            # move by moveSteps
            self.selectIndex += moveSteps

        # print elements.
        self._print_elements_()
