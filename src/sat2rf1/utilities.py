# Copyright (C) 2021  Joakim Skogø Langvand / Orbit NTNU

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re

from kiss.kiss import Kiss
from sat2rf1 import logger, constants


def query(radio: Kiss) -> None:
    radio.write(constants.M_GET_FREQ)


def bytes_to_str(bytes_in: bytes) -> str:
    """
    Return human readable string
    """
    tmp = bytes_in.hex().upper()
    return str.join(" ", list(filter(None, re.split(r'(.{2})', tmp))))


def uint32_to_bytes(i: int, endian: str = "little") -> bytes:
    return int.to_bytes(i, length=4, byteorder=endian)


def uint16_to_bytes(i: int, endian: str = "little") -> bytes:
    return int.to_bytes(i, length=2, byteorder=endian)


def uint8_to_bytes(i: int, endian: str = "little") -> bytes:
    return int.to_bytes(i, length=1, byteorder=endian)


def encode_freq(freq: float) -> bytes:
    return uint32_to_bytes(int(freq * 10e5), endian="big")


def decode_freq(freq: bytes) -> float:
    return int.from_bytes(freq, byteorder="big", signed=False)


def tests():
    print(f"435.000 as bytes: {bytes_to_str(encode_freq(435.000))}")
