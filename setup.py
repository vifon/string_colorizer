#!/usr/bin/env python

from distutils.core import setup

import string_colorizer

if __name__ == '__main__':
    setup(
        name='string_colorizer',
        description="Color strings according to a hashing function",
        long_description=string_colorizer.__doc__,
        version=string_colorizer.__version__,
        author=string_colorizer.__author__,
        author_email=string_colorizer.__email__,
        license=string_colorizer.__license__,
        packages=['string_colorizer'],
        scripts=['color-paths'],
    )
