#
#  GemUO
#
#  (c) 2005-2012 Max Kellermann <max@duempel.org>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; version 2 of the License.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#

import os
import ConfigParser

paths = []
if 'HOME' in os.environ:
    paths.append(os.path.join(os.environ['HOME'], '.gemuo/config'))
paths.append('/etc/gemuo/config')

config = ConfigParser.ConfigParser()
config.read(paths)

def require(section, key):
    """Looks up a setting, and throws an exception if it does not
    exist."""
    return config.get(section, key)

def get(section, key, default=None):
    """Looks up a setting, and returns the specified default value if
    it does not exist."""
    try:
        value = require(section, key)
    except ConfigParser.Error:
        value = None
    if value is None:
        value = default
    return value

def get_data_path():
    path = get('uo', 'path')
    if path is None and 'HOME' in os.environ:
        path = os.path.join(os.environ['HOME'], '.wine/drive_c/uo')
    return path

def require_data_path():
    path = get_data_path()
    if path is None:
        raise 'No data path'
    return path
