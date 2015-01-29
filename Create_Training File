#Code for generating the training file from the training documents. 
#Formats the training data:LABEL_1 FEATURE_11 FEATURE_12 ... FEATURE_1N 
#Each line in training data file corresponds to one document. 
#Each line starts with the class label for the document, and continues with the feature vector that represents the document. 
#For eg:SPAM_training directory contains all the documents with SPAM_ or HAM_ as file name
#We split the string of the file name to derive the classes and lablel is class name
#spam_training.txt for the spam dataset, and sentiment_training.txt for the sentiment dataset

import os
import re

def main():
	## create spam_training.txt file to generate training file which contains 1 document per line
	with open('spam_training.txt','w',errors="ignore")as outputfile:
		##SPAM_training contains all the training files
		directory='SPAM_training'
		##find all files in that directory
		for root,dirs,files in os.walk(directory):
		##open individual file and paste contents
			for f in files:	
				##Extract class names from file name
				##Split on '.' The first part is the class name
				class_name=f.split('.')
				outputfile.write(class_name[0]+" ")
				##Open the file
				ip=root+"/"+f
				with open(ip,'r',errors="ignore")as inputfile:
					line=inputfile.read()
					line=line.replace("\n"," ") ##replace new line with space
					outputfile.write(line) ##write to output file
					inputfile.closed	
					outputfile.write("\n")
	outputfile.closed
			
	
	return
	
if __name__=="__main__":
	main()
