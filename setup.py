#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Install using distutils

Run:
    python setup.py install

to install this package.
"""
from setuptools import setup, find_packages
from os.path import join

name = "ctinspector"

desc = "Show detailed information for docker images"
long_desc = "Shows detailed information for docker images"


classifiers = '''
Development Status :: 1 - Planning
Intended Audience :: Developers
License :: Freely Distributable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.4
'''

requirements = open('requirements.txt').read()

setup(
    name=name,
    version=open(join(name, 'version')).readline().strip("\r\n"),
    description=desc,
    long_description=long_desc,
    author='João Pinto',
    author_email='lamego.pinto@gmail.com',
    classifiers=[x for x in classifiers.splitlines() if x],
    install_requires=[x for x in requirements.splitlines() if x],
    url='https://github.com/joaompinto/'+name,
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts':[name + ' = ' + name + '.__main__:main']},
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
)
