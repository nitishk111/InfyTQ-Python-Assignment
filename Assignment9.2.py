# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:14:05 2020

@author: Nitish
"""

acc_no=int(input("Enter 4 digit account number: "))
acc_bal=int(input("Enter total balance in account: ").strip("Rs.rs.only"))
sal=int(input("Enter Salary: ").strip("Rs.rs."))
loan_type=int(input("Input Loan type: 1 for car, 2 for house and 3 for business loan: "))
exp_loan_am=int(input("Enter amount required for loan: ").strip("Rs.rs."))
exp_emi=int(input("Enter EMI, you want to fill: ").strip("RS.rs."))

if acc_no//1000==1 and acc_bal>100000:   
    if loan_type==1 and exp_loan_am<=500000 and exp_emi<=36 and sal>25000:
        print("Acc no {0} is elligible for Car loan of 500000, expected loan amount is {1}".format(acc_no,exp_loan_am))         
    elif loan_type==2 and exp_loan_am<=6000000 and exp_emi<=60 and sal>50000:
        print("Acc no {0} is elligible for House loan of 6000000, expected loan amount is {1}".format(acc_no,exp_loan_am))            
    elif loan_type==3 and exp_loan_am<=7500000 and exp_emi<=84 and sal>60000:
            print("Acc no {0} is elligible for Business loan of 7500000, expected loan amount is {1}".format(acc_no,exp_loan_am))
    else:
        print("Your demand for loan didn't meet loan elligibility.")
else:
    print("Your account is not elligible for loan.")