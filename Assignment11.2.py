# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 02:02:08 2020

@author: Nitish
"""
def fact(num):
    if num==0:
        return 1
    else:
        return fact(num-1)*num

num_list=list(map(int,input("Enter list: ").split()))
strong_num=list()
for i in num_list:
    b=0
    j=i
    while i>0:
        a=i%10
        i=i//10
        b=b+fact(a)
    if j==b:
        strong_num.append(b)
print("Strong numbers from the given list is/are: ",end="")
for i in strong_num:
    print(i,end=" ")