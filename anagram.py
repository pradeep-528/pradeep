#!/usr/bin/python

# anagram
 
def anagram(word1,word2):
    if sorted(word1) == sorted(word2):
       print "i am anagram"
    else:
       print "not anagram"
anagram('eat','ate')
 
