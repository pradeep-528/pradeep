#!/usr/bin/python
# sorting the strings in a list

def sort(list):
    y=[]
    z=[]
    for i in list:
        y.append(len(i))
        y.sort()
    for j in y:
        for k in list:
            if j == len(k):
               z.append(k)
    print z


sort(['ac','b','asd'])
