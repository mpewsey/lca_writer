# LCA Writer

[![Build Status](https://travis-ci.com/line-mind/lca_writer.svg?token=8VnQgt1kpLw7KrQy9Bzq&branch=master)](https://travis-ci.com/line-mind/lca_writer)
[![Documentation Status](https://readthedocs.org/projects/lca-writer/badge/?version=latest)](https://lca-writer.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/line-mind/lca_writer/branch/master/graph/badge.svg)](https://codecov.io/gh/line-mind/lca_writer)

<!--

## Table of Contents

* [LCA Writer](lca_writer.rst)
* [Scripts](scripts.rst)
* [Data Loaders](data.rst)

-->

## About

Write PLS-POLE and TOWER Load Case Analysis (LCA) files

## Installation & Usage

To use the package, first install it via pip:

```
pip install git+https://github.com/line-mind/lca_writer#egg=lca_writer
```

Save a copy of the submission form template using the command line script:

```
lca_writer --template lca_form.xlsx
```

Fill out the form and submit it using the command line script:

```
lca_writer folder1/lca_form.xlsx
```

An LCA file will be written to the same folder as the form.

Multiple forms can be submitted simultaneously as well:

```
lca_writer folder1/lca_form1.xlsx folder2/lca_form2.xlsx
```
