#!/usr/bin/env python3

'Usage: python3 wordFreq.py Harry_stone.txt'

import re
import sys

if len(sys.argv) != 2:
    print('usage: command file')
    exit(0)

filename = sys.argv[1]

linkre = re.compile(r'\b[a-zA-Z]+\b')
dic = {}

with open(filename, 'r') as f:
    for line in f.readlines():
        for item in linkre.findall(line):
            if item in dic.keys():
                dic[item] += 1
            else:
                dic[item] = 1


L = sorted(dic.items(), key=lambda d: d[1], reverse=True)

for item in L:
    print('{:16} : {}'.format(item[0], item[1]))
