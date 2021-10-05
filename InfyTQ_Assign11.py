#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    result_list=[0,0]
    for i in sentence:
        if i.isupper():
            result_list[0]+=1
        elif i.islower():
            result_list[1]+=1
    return result_list

sentence="Come Here Boy!"
print(find_upper_and_lower(sentence))
