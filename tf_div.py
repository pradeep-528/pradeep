# numbers divisible by 3 and 5
a=range(100)
for i in a:
    if i%3==0 and i%5==0: # or if i%15==0 
       print i
