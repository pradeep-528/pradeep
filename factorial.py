#!/usr/bin/python
# factorial of a number

def fact(n):
    p = 1
    for i in range(n):
        p = p*(i+1)
    print p

fact(4)
