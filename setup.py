#!/usr/bin/env python3
import os
import sys
import metric
from setuptools import setup, Command


class _Command(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class PEP8(_Command):
    description = 'PEP8 analysis'

    def run(self):
        code = os.system('scripts/pep8.sh')
        if code != 0:
            sys.exit(1)


class Pyflakes(_Command):
    description = 'Pyflakes analysis'

    def run(self):
        code = os.system('scripts/pyflakes.sh')
        if code != 0:
            sys.exit(1)


class Test(_Command):
    description = 'Run tests'

    def run(self):
        os.system('scripts/test.sh')


class Check(_Command):
    description = 'Run all checks'

    def run(self):
        codes = []
        codes.append(os.system('scripts/pep8.sh'))
        codes.append(os.system('scripts/pyflakes.sh'))
        codes.append(os.system('scripts/test.sh'))
        if any([code != 0 for code in codes]):
            sys.stderr.write('One or more checks have failed.\n')
            sys.stderr.flush()
            sys.exit(1)
        else:
            sys.stdout.write('All checks have passed.\n')
            sys.stdout.flush()


name = 'metric'
license = 'Apache License (2.0)'
packages = ['metric']
description = 'Library to gather own process metrics'
author = 'Metric library authors'
author_email = 'nbargnesi@selventa.com'
url = 'https://github.com/southcoast-python/metric'
download_url = 'https://github.com/southcoast-python/metric/releases'
classifiers = [
    'Programming Language :: Python :: 3',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

long_description = '''\
Metric
------

A Python library to gather own process metrics.
'''

setup(
    cmdclass={
        'pep8': PEP8,
        'pyflakes': Pyflakes,
        'test': Test,
        'allchecks': Check
    },
    name=name,
    packages=packages,
    version=metric.__version__,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    download_url=download_url,
    classifiers=classifiers,
    long_description=long_description
)
