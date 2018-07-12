import os
from ..lca_writer import LCAWriter

DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))

def load_data(name):
    p = os.path.join(DATA_FOLDER, name + '.xlsx')
    return LCAWriter(p)
