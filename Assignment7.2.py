# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:21:00 2020

@author: Nitish
"""


s=input("Enter the String:: ")
d=dict()
for i in s:
    j=i.upper()
    if j not in d.keys():
        d[j]=1
    else:
        d[j]=d[j]+1

for i in sorted(d.keys()):
    print(str(d[i])+i)