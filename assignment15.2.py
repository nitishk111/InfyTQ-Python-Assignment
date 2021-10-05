
age=int(input("Enter age of person: "))
health_condition=input('Enter health condition, "excellent" for good and "poor" for bad health: ')
residence=input("Enter residency of person, city or village: ")
gender=input("Enter gender of person, male or female: ")

if age>25 and age<35:
    if gender=='male':
        if residence=='city' and health_condition=='excellent':
            print("the premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.")
        elif residence=='village' and health_condition=='poor':
            print("policy amount cannot exceed Rs. 2 lakhs.")
        else:
            print("Person can't be insured.")
    elif gender=='female' and residence=='city' and health_condition=='excellent':
        print("the premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakhs.")
    else:
        print("Person can't be insured.")
else:
    print("Person can't be insured.")
