#PF-Prac-34
def check_well_formatted(input_item,list_label):
    #Start writing your code here
    # length,first matches or not
    if len(input_item)<2 or input_item[0] not in list_label:
        if type(input_item) is not list:
            return False
    else:
        for i in range(1,len(input_item)):
            if type(input_item[i]) is not str and type(input_item[i]) is not list:
                return False
        while i in input_item:
            if type(i) is list:
                return check_well_formatted(input_item[i],list_label)
        return True




input_list1=['NP',['N','A','or','b'],'c']
list_label1=['NP', 'V','N']
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")

    
