import pickle
import sys
import math

modelfile=open(sys.argv[1],"rb")
words_dict=pickle.load(modelfile)

with open(sys.argv[2],"r") as testfile:
	#read testfile one line at a time representing one doc
	for line in testfile:
		words=line.split()
		maxprob=-9999999
		for classes in words_dict['Meta_Info']['names_of_classes']:
			#print(classes)
			#print(maxprob)
			prob=words_dict['Meta_Info']["P("+classes+")"] ##P(class)
			#print(prob)
			for word in words:
				#print(word)
				if word in words_dict[classes]:
					prob+=words_dict[classes][word]
				else:
					##If word not present add-one smoothing
					a=1/(words_dict['Meta_Info'][classes+"_words"]+words_dict['Meta_Info']['size_vocab'])
					a=math.log(a)
					prob+=a
					#print(prob)
			
			if(prob>maxprob):
				name=classes
				maxprob=prob
		print(name)
	#print(words_dict)
