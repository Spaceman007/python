#!/usr/bin/env python3

'get .bmp info. usage: python3 bmpInfo.py shark.bmp'

import struct
import sys

if len(sys.argv) != 2:
    print('usage: command filename')
    exit()
else:
    filename = sys.argv[1]

with open(filename, 'rb') as f:
    a = struct.unpack('<ccIIIIIIHH', f.read(30))

if a[0] == b'B' and a[1] == b'M':
    pass
else:
    print('Not bmp file')
    exit()


print('{:10} : {} bytes'.format('size', str(a[2])))
print('{:10} : {}'.format('width', a[6]))
print('{:10} : {}'.format('height', a[7]))
print('{:10} : {}'.format('color-bit', a[9]))
