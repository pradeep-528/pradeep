#!/usr/bin/python
# printing months

d={"jan":1,"feb":2,"mar":3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
print "enter first 3 letters in a month"
s=raw_input("enter month:")
if s in d.keys():
   print d[s]
else:
   print "wrong entry"
