string_colorizer
================

Color strings according to a given hashing function.

Supports coloring the path segments inside a string separately.

INSTALLATION
------------

    pip install string_colorizer

color-paths
===========

An example script using this library.

SYNOPSIS
--------

    locate myfile | color-paths
    find . -name myfile | color-paths

DESCRIPTION
-----------

Colors the path segments in each path given on stdin or in the file
specified in the argument.

COPYRIGHT
---------

Copyright (C) 2013-2015  Wojciech Siewierski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
