#! /usr/bin/env python

import io

try:
    from setuptools import setup
    have_setuptools = True
except ImportError:
    from distutils.core import setup
    have_setuptools = False

VERSION = "0.5.123"
M_VERSION = "0.5"

setup_kwargs = {
    "version": VERSION,
    "description": 'The enlightened pager: less paging. more content. read widely.',
    "author": 'Paul Ivanov',
    "author_email": 'pi@berkeley.edu',
    "url": 'http://kant-en.org/',
    "download_url": "https://github.com/ivanov/kanten/zipball/" + M_VERSION,
    "classifiers": [
        "License :: OSI Approved",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "Topic :: Utilities",
        ],
    "zip_safe": False,
    "data_files": [("", ['LICENSE', 'README.md']),],
    }

if have_setuptools:
    setup_kwargs['install_requires'] = [
        'Pygments >= 1.6',
        'urwid >= 1.1.1',
        ]

if __name__ == '__main__':
    setup(
        name='kanten',
        py_modules=['kanten'],
        entry_points={'console_scripts': ['kanten = kanten:main',],},
        long_description=io.open('README.md', encoding='utf-8').read(),
        **setup_kwargs
        )
