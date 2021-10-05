# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:23:02 2020

@author: Nitish
"""
i=0
def num_convert(a):
    global i
    i+=1
    if i%2==1:
        return a
    else:
        return int(a)

gem_price={'Emerald':1760,'Ivory':2119,'Jasper':1599,'Ruby':3920,'Garnet':3999}
discount={'Ivory':3,'Ruby':4,'Emerald':6,'Jasper':6,'Garnet':6}
print("Available Gems are:",end=": ")
for a in gem_price.keys():
    print(a, end=" ")
print()
gem_list=list()
quat_list=list()

customer_list=list(map(num_convert,input("Enter the name and quantity to be purchased from list\n").split()))

for i in range(0,len(customer_list)):
    if i%2==0:
        gem_list.append(customer_list[i])
    else:
        quat_list.append(customer_list[i])
bill=0

if sum(quat_list)==0:
    print("Bill is Rs. -1")
else:
    for b in range(0,len(customer_list),2):
        x=customer_list[b]
        bill=bill+customer_list[b+1]*(gem_price[x]-gem_price[x]*(discount[x]/100))
    
    print("Bill is Rs. ",bill)