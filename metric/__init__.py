#!/usr/bin/env python3
'''Metric Python library.

See https://github.com/southcoast-python/metric for more.
'''
import resource
__author__ = 'Metric library authors'
__copyright__ = 'Copyright 2014, Metric authors'
__credits__ = [
    'Nick Bargnesi'
]
__license__ = 'Apache License 2.0'
__version__ = '0.1'
__maintainer__ = 'Nick Bargnesi'
__email__ = 'nbargnesi@selventa.com'
__status__ = 'alpha'


def used_memory():
    rusage = resource.getrusage(resource.RUSAGE_SELF)     
    return rusage.ru_maxrss

