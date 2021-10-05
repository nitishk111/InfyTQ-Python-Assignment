# -*- coding: utf-8 -*-


num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
list_num=list()
if num2>num1:
    while num1<=num2 and num1<100:
        if num1/10<1:
            a=num1%10
            b=0
        else:
            a=num1%10
            b=num1//10
        if (a+b)%3==0 and num1%3==0:
            list_num.append(num1)
            num1+=3
        else:
            num1+=1
        
    print("Numbers are: ",end=" ")
    for i in list_num:
        print(i,end=" ")
else:
    print("num1 should be less than num2.")