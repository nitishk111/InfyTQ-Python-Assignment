# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:52:42 2020

@author: Nitish
"""


int_list=list(map(int,input().split()))
count=0;
i=1;
prev=int_list[0];
while i < len(int_list):
    for j in range(i,len(int_list)):
        if prev==int_list[j]:
            count+=1;
            i+=1
        else:
            prev=int_list[j]
            i+=1
            break;
print("No of occurence is "+str(count))