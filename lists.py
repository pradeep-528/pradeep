#!/usr/bin/python
# print common values in two lists

l1=[1,2,3,4]
print l1
l2=[2,3,5,6]
print l2
l3=[]
for i in l1:
    for j in l2:
        if i == j:
           l3.append(i)
print "the common values are",l3
