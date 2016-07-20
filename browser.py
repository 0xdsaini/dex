# Copyright (c) 2015 ICRL
# See the file LICENSE for copying permission.

"""Contains Browser class"""

from helpers import prepareLine

from itertools import islice


class Browser(object):

    """Browses a list of contents on screen."""

    def __init__(self, stdscr, contents):

        """Takes curses `screen` to be used for rendering and, a list of
        Contents(of Content-type) to be rendered and browsed.

        01) Each Content in `contents` member have a index associated
            with it.

        02) selectIndex member keeps track of whether a specific content is
            selected by storing its index in itself.

        03) `minSelectIndex` and `maxSelectIndex` members are the lower and
            upper limits of `selectIndex` member respectively.

            i.e. They limits the selectIndex to be no less and no more than
            `minSelectIndex` and `maxSelectIndex` respectively.

        04) _update_dims_() method gets the most recent screen dimensions(y, x)
            and updates `dims` member whenever it is called.

        05) _print_elements_() method prepares an iterator called
            `onscreen_contents`(sliced from original `contents` list to contain
            exactly the number of contents as the screen size) whose contents
            are to be rendered on screen in the exact same order.

           5.1) `scrollIndex` slices the original member list,
                `contents` to provide a facility to scroll up & scroll down if
                `selectIndex` exceeds the vertical screen limit(y-coordinate).

           5.2) Before rendering, each content gets prepared(to be rendered)
                and gets it properties(color properties etc.) from prepareLine
                function(from helpers module).

        06) setContents() method changes(sets) the contents' list to a new
            list(provided as an argument), redetermines the `maxSelectIndex` and
            sets selectIndex to its default value.

        07) getContents() method returns the current contents' list to the
            caller.

        08) getSelected() method returns the selected content to the caller.

        09) Move() method moves the `selectIndex` pointer by `moveSteps` if
            the resulting selectIndex lies somewhere between `minSelectIndex`
            and `maxSelectIndex`(both inclusive).

        10) Jump() method jumps and select a content at the
            provided(as an argument) index on screen if it is
            selectable(lies between minSelectIndex and maxSelectIndex, both
            inclusive).
        """

        # Standard screen
        self.stdscr = stdscr

        # list containing Content-objects. To be printed on screen.
        self.contents = contents

        # Minimum index to be selected
        self.minSelectIndex = 1

        # Maximum index to be selected
        self.maxSelectIndex = len(self.contents)

        # element selection index.
        self.selectIndex = 1

        # start slice of contents
        self.scrollIndex = 0

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
        localIndex = self.selectIndex - self.scrollIndex

        # If local selection is greater than height
        if localIndex > height:

            # Increase slicing to scroll down
            self.scrollIndex = self.selectIndex - height

            # Stay at the last element
            localIndex = height

        # If  local selection is less than 0
        elif localIndex <= 0:

            # Decrease slicing to scroll up
            self.scrollIndex = self.selectIndex - 1

            # Stay at the first element
            localIndex = 1

        # Generator object of on-screen contents.
        onscreen_contents = islice(self.contents, self.scrollIndex,
                                   self.scrollIndex + height)

        # loop through all contents.
        for curr_line, item in enumerate(onscreen_contents):

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

        If moved succesfully, return True, else, False.
        """

        # boolean expression to determine : "will the resulting selectIndex lie
        # within limits(inclusively)"?
        should_move = self.minSelectIndex <= self.selectIndex + moveSteps and\
            self.selectIndex + moveSteps <= self.maxSelectIndex

        # Should I move?
        if should_move:

            # move by moveSteps
            self.selectIndex += moveSteps

        # print elements.
        self._print_elements_()

        # return
        return should_move

    def Jump(self, jumpIndex):

        """Jump and select a content at given index.
        If jumped succesfully, return True, else, False."""

        # boolean experssion to determine : "whether the jumpIndex lies within
        # limits(inclusively)"?
        should_jump = self.minSelectIndex <= jumpIndex <= self.maxSelectIndex

        # Should I jump?
        if should_jump:

            # jump to select jumpIndex.
            self.selectIndex = jumpIndex

        # print elements.
        self._print_elements_()
