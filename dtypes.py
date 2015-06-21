"""Contains all useful types and classes"""

from constants import ELEMENT_PREFIX  # import ELEMENT_PREFIX constant


class Content(object):

    """Contents class"""

    def __init__(self, name, type):

        self.name = name

        self.type = type

        self.linePrefix = ELEMENT_PREFIX[self.type]
