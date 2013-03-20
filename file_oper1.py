#!/usr/bin/python

# reading lines in a file

fp1 = open('file1.txt','wb')
fp1.write("pradeep\n kumar\n python")
fp1.close()

fp2 = open('file1.txt','rb')
line = fp2.readlines()
fp2.close()
print line
print line[0]
print line[2]

