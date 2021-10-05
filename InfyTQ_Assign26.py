# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:57:18 2020

@author: Nitish
"""


legs=94
heads=35

for i in range(1,heads+1):
    if (i*4)+(heads-i)*2==legs:
        print("Chickens:: {1}, Rabbits:: {0}.".format(i,heads-i))
        break
    elif (i*2)+(heads-i)*4==legs:
        print("Chickens:: {1}, Rabbits:: {0}.".format(heads-i,i))
        break
        
else:
    print("No Solution.")