# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 22:39:15 2020

@author: Nitish
"""


courses=["Python Programming","RDBMS","Web Technology","Software Engg."]
elective=["Business Intelligence","Big Data Analysis"]

print("Number of courses opted by 'John' is- ",len(courses))
print("ALl the course opted by student 'John' is- ",(courses))
add_ellective=int(input("{0} courses are being offred, press 1 for {1} and 2 for {2}- ".format(len(elective),elective[0],elective[1])))
if add_ellective==1:
    courses.append(elective[0])
elif add_ellective==2:
    courses.append(elective[1])
else:
    print("Choose valid Subject..")
    
print("Updated Tuple with elective is- ",tuple(courses))

if "Computer Networks" in elective:
    print("Yes, 'John' can change subject from software Engg. to Computer Networks.")
else:
    print("NO, 'John' can't change subject from software Engg. to Computer Networks.")
