#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    author="Ruman Gerst",
    author_email='ruman.gerst@leibniz-hki.de',
    classifiers=['License :: OSI Approved :: BSD-2-Clause License', 'Programming Language :: Python :: 3.10'],
    description="Provides integration into JIPipe",
    license="BSD-2-Clause license",
    include_package_data=True,
    name='jipipe-adapter',
    install_requires=[
      "pandas", "scikit-image"
    ],
    version='0.3.0',
    zip_safe=False)
