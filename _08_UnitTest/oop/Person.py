class Person:
    """A simple class."""  # docstring
    species = "Homo Sapiens"  # class attribute

    def __init__(self, name):  # special method
        """This is the initializer. It's a special method (see below).
        """
        self.name = name  # instance attribute

    def rename(self, renamed):  # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
