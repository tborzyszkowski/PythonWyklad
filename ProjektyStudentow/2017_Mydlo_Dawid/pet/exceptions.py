from enum import Enum, unique

__all__ = [
    'PetException', 'NameNotFound', 'NameAlreadyTaken', 'ProjectActivated', 'ShellNotRecognized', 'Info'
]


@unique
class ExceptionMessages(Enum):
    """
    Messages shown by pet in it's exceptions
    """
    project_not_found = "{0} - project not found"
    project_is_active = "{0} - project is active"
    project_is_locked = "{0} - project is locked"
    project_exists = "{0} - project under this name exists"
    project_in_archive = "{0} - name already taken in archive"
    template_not_found = "{0} - template not found"
    template_exists = "{0} - template under this name exists"
    task_not_found = "{0} - task not found"
    task_already_exists = "{0}- task already exists"
    shell_not_supported = "{0} - isn't supported"
    no_rc_file_found = "no rc file in {0}"
    directory_not_found = "{0} - directory not found\ntry 'pet recreate'"


class PetException(Exception):
    """
    Base class for exceptions raised by PET
    """


class NameNotFound(PetException):
    """
    Error raised when given name wasn't recognized
    """


class NameAlreadyTaken(PetException):
    """
    Error raised when name is already occupied by something
    """


class ProjectActivated(PetException):
    """
    Error raised when _lock file exists in project directory
    - meaning project is active
    """


class ShellNotRecognized(PetException):
    """
    Error raised when shell isn't recognized as implementedS
    """


class FolderNotFound(PetException):
    """
    Error raised when some of folders pet is using doesn't exist
    """


class Info(PetException):
    """
    Error raised when not critical error occurs
    """
