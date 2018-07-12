import os
from glob import glob
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name = 'lca_writer',
      version = '0.0.0',
      description = '',
      long_description = long_description,
      url = 'https://github.com/line-mind/lca_writer',
      license = 'BSD 3-Clause License',
      packages = find_packages(),
      include_package_data = True,
      install_requires = ['pandas', 'xlrd'],
      dependency_links = [],
      keywords = [],
      classifiers = [],
      python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*')
