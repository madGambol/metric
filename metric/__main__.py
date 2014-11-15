#!/usr/bin/env python3
'''Metric Python library.

See https://github.com/southcoast-python/metric for more.
'''
import metric


def main():
    info = '''
    Metric
    --
    {copyright}
    License: {license}
    Version: {version}
    URL: {url}

    The metric library is made possible by the help of %d contributors.
    '''
    kwargs = {
        'version': metric.__version__,
        'url': 'https://github.com/southcoast-python/metric',
        'license': metric.__license__,
        'copyright': metric.__copyright__
    }
    print(info.format(**kwargs) % (len(metric.__credits__)))
    

if __name__ == '__main__':
    main()

