import os
from ..lca_writer import LCAWriter

DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))

def load_data(name):
    """
    Loads an Excel form from the data folder with the specified name.

    Parameters:
        name : str
            The name of the form without file extension.
    """
    p = os.path.join(DATA_FOLDER, name + '.xlsx')
    return LCAWriter(p)
