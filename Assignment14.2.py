
marks_table={'John':86.5,'Jack':91.2,'Jill':84.5,'Harry':72.1,'Joe':80.5}

top=3
print("Top {} scorer of subject--".format(top),end=" ")
for i,j in sorted(marks_table.items(),key=lambda x:x[1]):
    if top>0:
        print(i,end=" ")
        top-=1
print("\nAverage score of all students: ",end=" ")
average=0
for i in marks_table.values():
    average=average+i
average=average/len(marks_table)
print(str(average)+"%")
