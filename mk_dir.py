#!/usr/bin/python
# making a directory and sub_directory in it

import os

def md(dir,f):
    print os.mkdir(dir)
    print os.chdir(dir)
    print os.mkdir(f)
md('python','list')
