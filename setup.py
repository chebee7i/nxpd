# -*- coding: utf-8 -*-
"""
Setup script for `nxpd`.

"""

from __future__ import print_function

import os
import sys

from distutils.core import setup

def main():

    requires = [
        'networkx(>=1.6)',
        'pyparsing(>=2.0.1)',
    ]

    packages = [
        'nxpd',
        'nxpd.pydot',
    ]

    description = """
`nxpd` is a Python package for visualizing NetworkX graphs using `pydot`
and `graphviz`. Support is also provided for inline displays within IPython
notebooks.
"""
    setup(
          name             = "nxpd",
          version          = "0.1",
          url              = "https://github.com/chebee7i/nxpd",

          packages         = packages,
          provides         = ['nxpd'],
          requires         = requires,

          author           = "chebee7i",
          author_email     = "chebee7i@gmail.com",
          description      = "NetworkX Pydot Draw",
          long_description = description,
          license          = "Unlicense",
         )

if __name__ == '__main__':

    v = sys.version_info[:2]
    if v < (2, 6):
        msg = "nxpd requires Python 2.6 or newer.\n"
        print(msg)
        sys.exit(-1)

    if sys.argv[-1] == 'setup.py':
        print("To install, run 'python setup.py install'.\n")

    main()
