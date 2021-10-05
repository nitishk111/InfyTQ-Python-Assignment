# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 08:31:28 2020

@author: Nitish
"""


a=input("Enter two digit String:: ").split(" ")
b,c=a[0],a[1]
b,c=c[0]+b[1:],b[0]+c[1:]
print(b+"\n"+c)
