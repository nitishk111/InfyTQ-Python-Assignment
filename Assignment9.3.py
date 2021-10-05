# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:23:41 2020

@author: Nitish
"""


veg_combo=120
nonveg_combo=150
food_type=input("Enter 'V' for vegetarian food, and 'N' for non-vegetarian food: ")
food_qut=int(input("Enter no of plates you want to buy: "))
distance=int(input("Enter approximate distance in KM: "))
delivery_charge=0
if (food_type=="V" or food_type=="N") and food_qut>=1 and distance>0:
    if distance>3 and distance<=6:
        delivery_charge=(distance-3)*3
    elif distance>6:
        delivery_charge=((distance-6)*6)+9
    print(delivery_charge)
    if food_type=="N":
        bill=nonveg_combo*food_qut+delivery_charge
    else:
        bill=veg_combo*food_qut+delivery_charge
    print("Total Bill amount is: "+str(bill))
else:
    print("Bill amount is -1.")