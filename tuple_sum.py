#!/usr/bin/python
# adding tuple values using variable function

def sum(a,b,*c):
    t=0
    for i in c:
        t+=i
    r=a+b+t
    print r
sum(1,2,3,4) # c-varies

