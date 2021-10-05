# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 07:37:26 2020

@author: Nitish
"""


data={1001:"John",1004:"Jill",1005:"Joe",1003:"Jack"}
print("Details of customers.")
print("Customer_ID","\t","Customer_Name")
for i,j in data.items():
    print(i,"\t\t",j)
print("No of Customers: ",len(data))
print("Customer name in ascending order--",end=" ")
for i in sorted(data.values()):
    print(i,end="\t")
print()    

del data[1005]
print("Details of customers, after deleting data 0f 1005--")
print("Customer_ID","\t","Customer_Name")
for i,j in data.items():
    print(i,"\t\t",j)
data[1003]="Marry"
print("Details of customers.")
print("Customer_ID","\t","Customer_Name")
for i,j in data.items():
    print(i,"\t\t",j)
    
if 1002 in data.keys():
    print("Detail of customers of id 1002 exist.")
else:
    print("Detail of customers of id 1002 does not exist.")