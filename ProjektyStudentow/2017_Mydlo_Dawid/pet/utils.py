import os


def makedirs(exists_ok=False, *args, **kwargs):
    path = kwargs.pop('path')
    try:
        return os.makedirs(path, *args, **kwargs)
    except OSError as e:
        if not exists_ok:
            raise e
