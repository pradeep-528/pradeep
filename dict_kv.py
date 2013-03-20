#!/usr/bin/python
# interchanging keys,values in a dictionary

def dic(d):
    dd = {}
    for k,v in d.items():
        dd[v] = k
    print dd
dic({'a':1,'b':2,'c':3})
