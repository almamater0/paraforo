#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import os
import io
from setuptools import setup, find_packages


BASE_DIR = os.path.join(os.path.dirname(__file__))


VERSION = '1.0'

with io.open(os.path.join(BASE_DIR, 'requirements.txt'), encoding='utf-8') as fh:
    REQUIREMENTS = fh.read()

if sys.platform.startswith(('win32', 'darwin')):
    PYTHON_MAGIC_DEP = ['python-magic-bin==0.4.14']
else:  # Linux?
    PYTHON_MAGIC_DEP = ['python-magic==0.4.15']

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='spirit',
    version=VERSION,
    packages=find_packages(),
    #test_suite="runtests.start",
    entry_points="""
[console_scripts]
spirit=spirit.extra.bin.spirit:main
""",
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    extras_require={
        'files': PYTHON_MAGIC_DEP},
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)