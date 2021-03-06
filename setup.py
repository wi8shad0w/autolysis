#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import open
# Require setuptools -- distutils does not support install_requires
from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession
import json


def req(path):
    return [entry.req.name for entry in parse_requirements(path, session=PipSession())]


setup(
    long_description=(open('README.rst', encoding='utf-8').read() + '\n\n' +
                      open('HISTORY.rst', encoding='utf-8').read().replace('.. :changelog:', '')),
    packages=find_packages(),
    package_dir={'autolysis': 'autolysis'},
    # Read: http://stackoverflow.com/a/2969087/100904
    # package_data includes data files for binary & source distributions
    # include_package_data is only for source distributions, uses MANIFEST.in
    package_data={
      'autolysis': ['release.json']
    },
    include_package_data=True,
    install_requires=req('requirements-conda.txt') + req('requirements.txt'),
    zip_safe=False,
    test_suite='tests',
    tests_require=[],
    **json.load(open('autolysis/release.json', encoding='utf-8'))
)
