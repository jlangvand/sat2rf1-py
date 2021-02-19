"""
Project wide constants
"""

M_SET_FREQ = b'\x20'
M_GET_FREQ = b'\x21'
M_SET_PWR = b'\x22'
M_GET_PWR = b'\x23'
M_GET_RSSI = b'\x24'
M_DEBUG = b'\x25'
M_ASCII = b'\x26'
M_SET_CORR_COEF = b'\x27'
M_GET_CORR_COEF = b'\x28'
M_SET_MODE = b'\x29'
M_GET_MODE = b'\x30'


DEBUG_PING = b'\x00\x00\x00\x00'
DEBUG_ENABLE_ASCII = b''
DEBUG_DISABLE_ASCII = b''

MODE_PACKET_RECEIVE = b''
MODE_TRANSPARENT_RECEIVE = b''
MODE_BEACON = b''
