def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    for i,j in zip(list1,list2[::-1]):
        if i!=None and j!=None:
            merged_data+=i+j
        elif i==None:
            merged_data+=j
        else:merged_data+=i
        merged_data+=' '
    resultant_data=merged_data.strip()
    return resultant_data
