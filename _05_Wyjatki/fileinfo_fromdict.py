"""Framework for getting filetype-specific metadata.

This is the same as fileinfo.py with one difference:
instead of inheriting from UserDict, we inherit directly from dict.
This capability was introduced in Python 2.2, and makes UserDict
unnecessary (along with its cousins, UserList and UserString).

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

import os
import sys


def strip_nulls(data):
    """strip whitespace and nulls
    """
    return data.replace("\00", " ").strip()


class FileInfo(dict):
    """store file metadata
    """
    def __init__(self, file_name=None):
        super().__init__()
        self["name"] = file_name


class MP3FileInfo(FileInfo):
    """store ID3v1.0 MP3 tags
    """
    tagDataMap = {"title"   : (3, 33, strip_nulls),
                  "artist"  : (33, 63, strip_nulls),
                  "album"   : (63, 93, strip_nulls),
                  "year"    : (93, 97, strip_nulls),
                  "comment" : (97, 126, strip_nulls),
                  "genre"   : (127, 128, ord)}

    def __parse(self, filename):
        """parse ID3v1.0 tags from MP3 file
        """
        self.clear()
        try:
            f_sock = open(filename, "rb", 0)
            try:
                f_sock.seek(-128, 2)
                tag_data = f_sock.read(128).decode('ascii')
            finally:
                f_sock.close()
            if tag_data[:3] == 'TAG':
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tag_data[start:end])
        except IOError:
            pass

    def __setitem__(self, key, item):
        if key == "name" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)


def list_directory(directory, file_extension_list):
    """get list of file info objects for files of particular extensions
    """
    file_list = [os.path.normcase(f) for f in os.listdir(directory)]
    file_list = [os.path.join(directory, f) for f in file_list \
                if os.path.splitext(f)[1] in file_extension_list]

    def get_file_info_class(filename, module=sys.modules[FileInfo.__module__]):
        """get file info class from filename extension
        """
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
    return [get_file_info_class(f)(f) for f in file_list]


if __name__ == "__main__":
    for info in list_directory(r"C:\home\tomek\UG\Zajecia\Python\Wyk\_04", [".mp3"]):
        print("\n".join(["%s=%s" % (k, v) for k, v in info.items()]))
