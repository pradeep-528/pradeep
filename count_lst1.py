#!/usr/bin/python
# printing repeated values in a list

x=[1,2,4,5,2,3,5]
y=[]
for i in x:
    if x.count(i) > 1 :
       y.append(i)
print y
