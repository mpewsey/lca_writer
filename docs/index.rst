========================
LCA Writer Documentation
========================

.. image:: https://travis-ci.com/mpewsey/lca_writer.svg?token=8VnQgt1kpLw7KrQy9Bzq&branch=master
    :target: https://travis-ci.com/mpewsey/lca_writer

.. image:: https://readthedocs.org/projects/lca-writer/badge/?version=latest
    :target: https://lca-writer.readthedocs.io/en/latest/?badge=latest

.. image:: https://codecov.io/gh/mpewsey/lca_writer/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mpewsey/lca_writer


About
=====
Write PLS-POLE and TOWER Load Case Analysis (LCA) files


Installation & Usage
====================

To use the package, first install it via pip:

.. code-block:: none

    pip install git+https://github.com/mpewsey/lca_writer#egg=lca_writer


Save a copy of the submission form template using the command line script:

.. code-block:: none

    lca_writer --template lca_form.xlsx


Fill out the form and submit it using the command line script:

.. code-block:: none

    lca_writer folder1/lca_form.xlsx


An LCA file will be written to the same folder as the form.

Multiple forms can be submitted simultaneously as well:

.. code-block:: none

    lca_writer folder1/lca_form1.xlsx folder2/lca_form2.xlsx


API Documentation
=================
.. toctree::
    :maxdepth: 1

    lca_writer
