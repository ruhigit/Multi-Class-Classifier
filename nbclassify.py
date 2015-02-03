import pickle
import sys
import os
import math

modelfile=open(sys.argv[1],"rb")
words_dict=pickle.load(modelfile)
##prints=list()
i=0
##mismatch=0
##total=0
##directory='SPAM_dev'
		##find all files in that directory
##for root,dirs,files in (os.walk(directory)):
		##open individual file and paste contents
	##for f in sorted(files):	
		##total+=1
		##f=f.split('.')
		##prints.append(f[0])
##with open("spam.out",'w') as outputfile:
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
		##print("\n")
			#outputfile.write(prints[i])
			#outputfile.write("\t")
		##outputfile.write(name)
		##outputfile.write("\n")
			##if(prints[i]!=name):
			##	mismatch+=1
			##i+=1
			##precision:#actual no of docs of class1 identified correctly/#no of docs identified as class1
			##recall:#actual no of docs of class1 identified correctly/#total no of docs of class1
			
		##print(mismatch)
				
			
