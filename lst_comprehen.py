#!/usr/bin/python
# list comprehensions-sorting dictionary from values

d = {'a':2,'b':5,'c':3,'d':1,'e':4}
print d
dic = [(v,k) for k,v in d.items()]
dic.sort()
dic = [(k,v) for v,k  in dic]
print dic


