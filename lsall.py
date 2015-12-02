#!/usr/bin/env python

'''
list all (specific)files in the current directory and subdirectory, with recursion
'''

import os

# list all files in the specific directory and subdirectories, with recursion
def lsDir(prename, dirName):
    for item in os.listdir(dirName):
        subname = dirName + '/' + item
        print(prename + '|--' + item)

        if os.path.isdir(subname):
            pre = prename + '  '
            lsDir(pre, subname)

# list all specific files in the specific directory and subdirectories, with recursion
def lsTarget(dirName, filetypeStr):
    for item in os.listdir(dirName):
        subname = dirName + '/' + item

        if os.path.isdir(subname):
            lsTarget(subname, filetypeStr)
        else:
            prefile, ext = os.path.splitext(item)
            ext = ext.lower()
            if ext == filetypeStr:
                print(subname)

if  __name__ == '__main__':
    lsTarget('.', '.txt')
# lsDir('', '.')
