# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 08:40:02 2020

@author: Nitish
"""


a="itnamnotgodnotpersonpoornessisbad"
not_ind=a.index("not")
poor_ind=a.index("poor")
print("First apperence of not is from index {}, and of poor is from index {}.".format(not_ind,poor_ind))
while 'not' in a:
    not_ind=a.index("not")
    a=a[:not_ind]+"good"+a[not_ind+3:]
while 'poor' in a:
    poor_ind=a.index("poor")
    a=a[:poor_ind]+"good"+a[poor_ind+4:]
print("Updated string is "+a)