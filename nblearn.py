#Program will be invoked as python3 nblearn.py TRAININGFILE MODELFILE
#TRAININGFILE will be spam_training.txt for the spam dataset, and sentiment_training.txt for the sentiment dataset
#MODELFILE will be spam.nb, and sentiment.nb
#MODELFILE will contain all the probabilities of words with respect to given class stored in 1 dictionary
#The words will be stored insdie nested dictionary
#{'spam': {'pharmacy':2}, 'ham': {'china': 1},'Info':{'totaldocs':2}}
#P(word|class)=(frequency of word in document of class C)/(Total number of words in documents of Class C)
#Add-one smoothing=(freq+1)/(total words+size of vocabulary)
#To prevent underflow we take the logs of probabilities

import sys
import pickle
import math
def calculate_word_prob(ip,op):
	
	words_dict=dict() ##store the unique words in dictionary
	words_dict['Meta_Info']=dict()##store the number of documents,classes count etc
	words_dict['Meta_Info']['names_of_classes']=list()##store the names of classes
	words_dict['Meta_Info']['size_vocab']=0 #no of unique words in vocab which will be stored in dictionary
	words_dict['Meta_Info']['total_no_docs']=0 #total no of documents
	with open(ip,'r') as trainingfile:
		with open(op,'wb')as modelfile:
			for line in trainingfile:
				words_dict['Meta_Info']['total_no_docs']+=1
				words=line.split()
				for index,word in enumerate(words):
					## If index is 0 then store the class name
					class_name=words[0]##first word is the class name
					##print("classname:",class_name)
					if index==0:
						
						##check if class has been detected before
						if class_name in words_dict:
							##if class already exists just increase count of documents of that class
							words_dict['Meta_Info'][class_name+"_Docs_Count"]+=1
							
						else:
							words_dict['Meta_Info']['names_of_classes'].append(class_name)
							##if class is new and does not exist already add it to list of class names
							words_dict[class_name]=dict()
							words_dict['Meta_Info'][class_name+"_Docs_Count"]=1
							words_dict['Meta_Info'][class_name+'_words']=0
					
					##else store the frequencies of words in dictionary                          
					else:
						words_dict['Meta_Info'][class_name+'_words']+=1
						if(word in words_dict[class_name]):
							words_dict[class_name][word]+=1
						else:
							words_dict[class_name][word]=1
							#for calculating unique words in vocab
							count=0
							for classes in words_dict['Meta_Info']['names_of_classes']:
								if(word in words_dict[classes]):
									count+=1
							if count==1:
								words_dict['Meta_Info']['size_vocab']+=1
			
						
			
			
			for classes in words_dict['Meta_Info']['names_of_classes']:
				## Calculate the priors
				##P(class)=No of docs of that class/Total no of docs
				words_dict['Meta_Info']["P("+classes+")"]=(words_dict['Meta_Info'][classes+"_Docs_Count"]/words_dict['Meta_Info']['total_no_docs'])
				##Store as logs to eliminate underflow
				words_dict['Meta_Info']["P("+classes+")"]=math.log(words_dict['Meta_Info']["P("+classes+")"])
				for word in words_dict[classes]:
					#P(word|class)
					##Add 1 to numerator for add one smoothing
					##The denominator has legth of words of that class+unique vocab size
					words_dict[classes][word]=(words_dict[classes][word]+1)/(words_dict['Meta_Info'][classes+"_words"]+words_dict['Meta_Info']['size_vocab'])
					words_dict[classes][word]=math.log(words_dict[classes][word])
					
			print(words_dict['Meta_Info'])                                
			pickle.dump(words_dict,modelfile)
			modelfile.closed
		trainingfile.closed
	return

def main():
	calculate_word_prob(sys.argv[1],sys.argv[2])
	return

if __name__=="__main__":
	main()
