#!/usr/bin/env python

import os
import re
import sys

from codecs import open
from setuptools import find_packages, setup
from distutils.core import setup

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist bdist_egg upload')
    sys.exit()

packages = [
    'coincheck'
]
requires = [ ] 
with open('requirements.txt','r') as fp:
    for line in iter(fp.readline, ''):
        requires.append(line.replace('\n',''))

version = ''
with open('coincheck/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='coincheck',
    version=version,
    description='Coincheck API Library for Python',
    long_description=readme + '\n\n' + history,
    author='Shohei Kamon',
    author_email='kamonshohei@gmail.com',
    url='https://github.com/kmn/coincheck',
    packages=find_packages(),
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'coincheck': 'coincheck'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        b'Development Status :: 5 - Production/Stable',
        b'Intended Audience :: Developers',
        b'Natural Language :: English',
        b'License :: OSI Approved :: MIT License',
        b'Programming Language :: Python',
        b'Programming Language :: Python :: 2.7',
        b'Programming Language :: Python :: 3',
        b'Programming Language :: Python :: 3.3',
    ),
)
