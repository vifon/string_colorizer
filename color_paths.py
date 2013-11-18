#!/usr/bin/env python3
# -*- python -*-
"""path colorizer

Colors the path segments in each path given on stdin or in the file specified in the argument.
"""

import fileinput
import os
from sys import argv

from string_colorizer import string_colorizer

class path_colorizer(string_colorizer):
    def colorize_path(self, path):
        """Colors each path component to the appropriate color"""
        return os.sep.join([ self.colorize(component)
                             for component in path.split(os.sep) ])

def main():
    colorizer = path_colorizer()
    for line in fileinput.input():
        path = line.rstrip(os.linesep)
        print(colorizer.colorize_path(path))

if __name__ == "__main__":
    main()

__all__ = ['path_colorizer']
