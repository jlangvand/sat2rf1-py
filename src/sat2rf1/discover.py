"""
Discover connected devices.

Writes a ping to all serial ports and prints the result.
"""

import os
import serial

from sat2rf1 import logger


def main():
    discover()
    

def discover() -> None:
    print("Probing for Sat2RF1 units...")
    serialdevices = []
    usbttys = []
    devs = os.listdir('/dev')
    for dev in devs:
        if dev[0:6] == 'ttyUSB':
            usbttys.append(dev)
    for usbtty in usbttys:
        serialdevices.append(serial.Serial('/dev/' + usbtty, 115200, timeout=1))
    #for serialdevice in serialdevices:
        #serialdevice.read_all()
        #serialdevice.write(PING)  # Send ping
        #try:
        #    serialdevice.read_until(b'\xc0')
        #    msg = serialdevice.read_until(b'\xc0')[0:-1]
        #    if msg == b'\x25\x00\x00\x00\x00':
        #        print('Found radio on port {}'.format(serialdevice.name))
        #except serial.SerialException:
        #    print('No answer from {}'.format(serialdevice.name))

if __name__ == '__main__':
    main()
