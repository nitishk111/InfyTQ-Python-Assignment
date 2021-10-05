# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 02:12:10 2020

@author: Nitish
"""


mileage=10
fule_price=70
ticket_price=80

route_dis=int(input("Enter distance of route in KM: "))
passengers=int(input("Enter no of passengers for the route: "))

fule_cost=(route_dis/mileage)*fule_price

earning=ticket_price*passengers

profit=earning-fule_cost

if profit>0:
    print("Profit on {0} long road is {1}.".format(route_dis,profit))
else:
    print("profit is -1.")