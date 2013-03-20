#!/usr/bin/python
# printing unique elements in alist

def unique(list):
    l2=[]
    for i in list:
        if i not in l2:
           l2.append(i)
    print l2
unique([1,2,1,3,2,4])
