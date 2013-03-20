#!/usr/bin/python
# frequency of values in a list

def dic(list):
    d = {}
    for i in list:
        x=list.count(i)
        d[i]=x
    print d
d = ['a','b','a','c','c','d']
print d
print "frequency of list elements in a dic"
dic(d)

