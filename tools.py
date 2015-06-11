from os.path import isdir, isfile, islink, ismount
from os.path import join
from os import listdir


TYPES = {isfile: "file", isdir: "dir", islink: "link", ismount: "mountpoint"}


class listLocals(object):

    """Class to list contents of directory in a organized fashion.
    """

    def __init__(self, path):

        # path to directory
        self.path = path

    def fileType(self, filename):

        """Return a string containing file's filetype if known, return "other"
        otherwise.

        Known Filetypes : "file", "dir", "link", "mountpoint".
        """

        # check to see if file is of listed filetype.
        for func in TYPES.keys():

            filepath = join(self.path, filename)

            if func(filepath):
                return TYPES[func]

        # If file is of type not listed in TYPES
        return "other"

    def split_file_types(self, contentList):

        """contentList -> A single list containing directories, files, links and
        mount points and other types of files.

        return a Dict containing key:value pairs where keys are : "dir",
        "file", "link", "mountpoint" and "other".

        Each key corresponds to a list of items with same file type and "other"
        contains a list of unsupported file types."""

        # Dictionary containing names of different content on its own list.
        # Supported keys are "file", "dir", "link", "mountpoint", "others".
        contentDict = {"file": [], "dir": [], "link": [], "mountpoint": [],
                       "other": []}

        for filename in contentList:

            filetype = self.fileType(filename)
            contentDict[filetype].append(filename)

        return contentDict

    def lsdir(self, path=None):

        """Return a Dict containing items in given `path` as key:value pairs where
        keys are : "dir", "file", "link", "mountpoint" and "other".

        And each key corresponds to a list of files with same file type and
        "other" contains a list of unsupported file types.
        """

        # If new path is given
        if path:
            # change current path
            self.path = path

        return self.split_file_types(listdir(self.path))


def lsdir(path):

    """Instantiate listLocals to return contents of a directory(at location
    `path` as a dictionary) in a organized fashion.

    See docstring -> listLocals.lsdir method for more on return value.
    """

    return listLocals(path).lsdir()
