# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:28:45 2020

@author: Nitish
"""


s=input("Enter string: ")
i=0
j=len(s)-1
c=0
while i<j:
    if s[i]!=s[j]:
        c+=1
    i+=1
    j-=1
if c==0:
    print("{0} is a Pallindrome String.".format(s))
else:
    print("{0} is not a Palindrome string.".format(s))