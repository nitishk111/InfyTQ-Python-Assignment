# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:58:26 2020

@author: Nitish
"""


s=input("Enter String:: ")
d=dict()
for i in s:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]=d[i]+1
for i,j in d.items():
    print(i,"-- ",j)