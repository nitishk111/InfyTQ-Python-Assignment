# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 23:20:12 2021

@author: Nitish
"""


def check_double(list1,list2):
    new_list=[]
    #write your logic here
    for i in list1:
        if i*2 in list2:
            new_list.append(i)
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))