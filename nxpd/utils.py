# -*- coding: utf-8 -*-

import os
import subprocess
import sys

def default_opener(filename):
    """Opens `filename` using system's default program.

    Parameters
    ----------
    filename : str
        The path of the file to be opened.

    """
    cmds = {'darwin': ['open'],
            'linux2': ['xdg-open'],
            'win32': ['cmd.exe', '/c', 'start', '']}
    cmd = cmds[sys.platform] + [filename]
    subprocess.call(cmd)

def is_string_like(obj): # from John Hunter, types-free version
    """Check if obj is string."""
    try:
        obj + ''
    except (TypeError, ValueError):
        return False
    return True

def get_fobj(fname, mode='w+'):
    """Obtain a proper file object.

    Parameters
    ----------
    fname : string, file object, file descriptor
        If a string or file descriptor, then we create a file object. If *fname*
        is a file object, then we do nothing and ignore the specified *mode*
        parameter.
    mode : str
        The mode of the file to be opened.

    Returns
    -------
    fobj : file object
        The file object.
    close : bool
        If *fname* was a string, then *close* will be *True* to signify that
        the file object should be closed after writing to it. Otherwise, *close*
        will be *False* signifying that the user, in essence, created the file
        object already and that subsequent operations should not close it.

    """
    if is_string_like(fname):
        fobj = open(fname, mode)
        close = True
    elif hasattr(fname, 'write'):
        # fname is a file-like object, perhaps a StringIO (for example)
        fobj = fname
        close = False
    else:
        # assume it is a file descriptor
        fobj = os.fdopen(fname, mode)
        close = False
    return fobj, close

def make_str(t):
    """Return the string representation of t."""
    if is_string_like(t): return t
    return str(t)
