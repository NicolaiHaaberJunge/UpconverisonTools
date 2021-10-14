#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='UC_module',
      version='0.1',
      description='A python packge to process UC module spectra.',
      license='MIT',
      include_package_data=True,
      packages=find_packages(),
      install_requires=['numpy', 'pandas', 'matplotlib'],
      #python_requires='>=3.8'
    )