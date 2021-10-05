# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:37:45 2020

@author: Nitish
"""


stack_size=int(input("Enter size of Stack: "))
i=1
stack=list()
while True:
    j=int(input("Press 1 for add in stack 2 for delete in stack, other keywords to terminate this session:: "))
    if j==1:
        if i>stack_size:
            print("stack is full.")
        else:
            stack.append(int(input("Enter number to add:: ")))
            i+=1
    elif j==2:
        if i<=1:
            print("Stack is already empty.")
        else:
            print("Deleted value is:: ",stack.pop())
            i-=1
    else:
        break