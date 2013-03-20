#!/usr/bin/python
# spliting a list

def split(list,count):
    for i in range(0,len(list),count):
        print list[i:i+count]
split([1,2,3,4,5,6,7,8,9],2)
