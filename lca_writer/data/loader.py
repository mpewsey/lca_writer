"""
Summary
-------
Provides methods and variables for loading data from the package data folder.

Global Variables
----------------
DATA_FOLDER
    The absolute path to the data folder.

Methods
-------

"""

import os
from ..lca_writer import LCAWriter

DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))

def load_data(name):
    """
    Loads an Excel form from the data folder with the specified name.

    name : str
        The name of the form without file extension.
    """
    p = os.path.join(DATA_FOLDER, name + '.xlsx')
    return LCAWriter(p)
