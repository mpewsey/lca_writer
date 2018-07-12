import os
from ..lca_writer import LCAWriter
from ..data import load_data, DATA_FOLDER


def test_load_data():
    lca = load_data('test_lca_form')


def test_save_template():
    p = os.path.join(DATA_FOLDER, 'lca_form_writer.xlsx')
    LCAWriter.save_template(p)
    assert os.path.exists(p)
    os.remove(p)


def test_write_lca():
    lca = load_data('test_lca_form')
    versions = ['12.2']

    for v in versions:
        p = os.path.join(DATA_FOLDER, 'test_lca_{}.lca'.format(v.replace('.', '_')))
        with open(p, 'rt') as file:
            s1 = file.read()
            s1 = s1.strip()

        p = os.path.join(DATA_FOLDER, 'test_lca_form.lca')
        lca.write_lca(version = v)
        with open(p, 'rt') as file:
            s2 = file.read()
            s2 = s2.strip()

        assert s1 == s2
        os.remove(p)
