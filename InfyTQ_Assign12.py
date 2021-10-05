#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
	#start writing your code here
	
    sentence_list=list()
    for i in subjects:
        for j in verbs:
            for k in objects:
                s=i+' '+j+' '+k
                sentence_list.append(s)
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
