#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='UC_module',
      version='0.1',
      description='A python packge to process UC module spectral data.',
      license='MIT',
      entry_points={
        'console_scripts': [
            'ucmod=bin.uc_mod:main',
        ]
      },
      packages=find_packages(),
      install_requires=['numpy', 'pandas'],
    )