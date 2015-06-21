
from constants import *  # import all constants
from config import curses, BOLD  # import configured curses and other configs


def prepareLine(Item, select, Width):

    """Prepares line to rendered on screen

    Item     -> name of item(object of Content type)
    type     -> type of item(string)
    select   -> bool to state whether to prepare it as a select element(bool)
    Width    -> Width of screen(int/long)
    """

    # Spaces followed by filename i.e. Item
    tail = (Width - (len(Item.linePrefix) + len(Item.name)) - 1) * " "

    # Prepares line
    currElement = "%s%s%s" % (Item.linePrefix, Item.name, tail)

    ## Set properties

    bold, colorPair = ELEMENT_PROPERTIES[Item.type][select]

    properties = curses.color_pair(colorPair) | BOLD[bold]

    return (currElement, properties)


def sortContents(dirContents):

    """Sorts directory contents of types returned by tools.lsdir() function"""

    # returns
    return {key: sorted(dirContents[key], key=CONTENTS_SORTFUNC)
            for key in dirContents}
