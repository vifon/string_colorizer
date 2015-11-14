"""Colorize strings according to a hashing function"""

#########################################################################
# Copyright (C) 2013-2015  Wojciech Siewierski                          #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#########################################################################

import os
import hashlib

__version__ = "1.1.0"
__author__ = "Wojciech Siewierski"
__email__ = "wojciech.siewierski+python@gmail.com"
__license__ = "GPL3"

__all__ = ['StringColorizer', 'PathColorizer']


class StringColorizer(object):
    def __init__(
            self,
            colors      = None,
            reset       = "\033[0m",
            hashfunc    = hashlib.md5,
            use_hashlib = True):
        """
        Arguments:
        - `colors`: list of the used colors' numbers for the escape codes; default: range from 31 to 37 + bolds
        - `reset`: escape code used to reset the formatting; default: "\\033[0m"
        - `hashfunc`: function used to map the string to the integer used to determine the color
        - `use_hashlib`: set to False if the hashfunc returns integer and does not need to be converted like the hashlib functions

        """
        self.reset = reset
        if use_hashlib:
            self.hashfunc = lambda x: int(hashfunc(x.encode('utf-8')).hexdigest(), base=16)
        else:
            self.hashfunc = hashfunc

        if colors is None:
            colors = ["{1};{0}".format(color, bold)
                      for bold in [0, 1]
                      for color in range(31, 38)]
        self.colors = ["\033[{0}m".format(color)
                       for color in colors]

    def choose_color(self, string):
        """Return a coloring string for the given string"""
        return self.colors[self.hashfunc(string) % len(self.colors)]

    def colorize(self, string):
        """Color the given string according to its hash"""
        return self.choose_color(string) + string + self.reset


class PathColorizer(StringColorizer):
    def colorize_path(self, path):
        """Colors each path component to the appropriate color"""
        return os.sep.join([self.colorize(component)
                            for component in path.split(os.sep)])
