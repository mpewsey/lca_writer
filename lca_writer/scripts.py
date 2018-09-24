"""
===================================
Scripts (:mod:`lca_writer.scripts`)
===================================

Summary
-------
Includes classes for parsing command line arguments.

Classes
-------

"""

import sys
from argparse import ArgumentParser

class LCAWriterArgParser(ArgumentParser):
    """
    Command line argument parser for lca_writer scripts.

    .. code-block:: none
    """
    def __init__(self):
        ArgumentParser.__init__(self, prog='lca_writer')
        self.add_argument('lca_forms',
                          nargs = '*',
                          help = 'Excel LCA form paths.')

        self.add_argument('-t', '--template',
                          nargs = '?',
                          help = 'Path to save the Excel form template (optional).',
                          default = None)

        self.add_argument('-v', '--version',
                          nargs = '?',
                          help = 'LCA file version to write.',
                          default = '12.2')

    @staticmethod
    def _doc_string():
        """Returns a doc string with the usage and help formats included."""
        s = LCAWriterArgParser()
        s = s.format_help()
        s = '\n\t'.join(s.split('\n'))
        return LCAWriterArgParser.__doc__ + '\n\t' + s + '\n\n'

if sys.version_info[0] >= 3:
    LCAWriterArgParser.__doc__ = LCAWriterArgParser._doc_string()
