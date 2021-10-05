# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:04:02 2020

@author: Nitish
"""


furniture=["Sofa Set","Dining Table","TV Stand","CUP Board"]
cost=[2000,8500,4599,13920]
req_fur=input("Enter the name of Furniture, you want to buy from the list {0}:".format(furniture))
req_qun=int(input("Enter Quantity of Furniture: "))

if req_fur in furniture and req_qun>0:
    x=furniture.index(req_fur)
    bill=req_qun*cost[x]
    print("Bill Amount for {0} set of {1} is Rs {2}".format(req_fur,req_qun,bill))
else:
    print("Bill Amount is Rs. 0.")