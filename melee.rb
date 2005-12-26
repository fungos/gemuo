#
#  libuoclient-ruby
#  $Id$
#
#  (c) 2005 Max Kellermann <max@duempel.org>
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
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

$:.unshift(File.dirname($0) + '/glue')
$:.unshift(File.dirname($0))

require 'uo/client'
require 'uo/engines/main'
require 'uo/engines/melee'

raise "syntax: test.rb host port username password charname target_serial" unless ARGV.length == 6

client = UO::Client.new(ARGV[0], ARGV[1], nil,
                        ARGV[2], ARGV[3], ARGV[4])

target_serial = ARGV[5].hex

UO::Engines::Main.new(client, UO::Engines::Melee.new(client, target_serial, false)).start

client.run