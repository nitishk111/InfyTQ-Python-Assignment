# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 07:53:58 2020

@author: Nitish
"""
i=0
def num_convert(a):
    global i
    i+=1
    if i%2==0:
        return a
    else:
        return int(a)
    

speciality={'P':'Pediatrics','O':'Orthopedics','E':'ENT'}

s=list(map(num_convert,input("Enter id and medical speciality visited by patient.").split()))

p,o,e=0,0,0
for i in s:
    if i=="P":
        p+=1
    elif i=="E":
        e+=1
    elif i=="O":
        o+=1
if p>e:
    if p>o:
        print(speciality['P'])
    else:
        print(speciality["O"])
else:
    if e>o:
        print(speciality['E'])
    else:
        print(speciality["O"])
