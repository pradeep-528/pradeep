#!/usr/bin/python

x=[("jan",1),("feb",2),("mar",3),("apr",4),("may",5),("jun",6),("jul",7),("aug",8),("sep",9),("oct",10),("nov",11),("dec",12)]
print "enter first 3 letters of a month"
z=raw_input("enter month: ")
for y in x:
    if z in y:
       print y[1]
    
