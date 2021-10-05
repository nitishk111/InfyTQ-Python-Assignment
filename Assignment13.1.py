# -*- coding: utf-8 -*-

def product(num1,num2,num3):
    if num1!=7 and num2!=7 and num3!=7:
        return (num1*num2*num3)
    elif num1==7:
        return (num2*num3)
    elif num2==7:
        return num3
    else:
        return -1
    

    
l=list(map(int,input().split()))
pro=product(l[0],l[1],l[2])
print("Product is: ",pro)
