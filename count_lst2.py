#!/usr/bin/python
# printing unique values in a list

x=[1,2,2,4,5,3,2,5]
y=[]
for i in x:
    if x.count(i)==1:
       y.append(i)
print y 
