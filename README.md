## Multi-Class-Classifier ##
Created text classifier and applied it to two datasets corresponding to two tasks: (1) spam filtering, and (2) sentiment analysis.
This repository contains the files: nblearn.py, nbclassify.py, spam.nb, sentiment.nb, spam.out, sentiment.out, and createTrainingFile.py code for generating the training file from the training documents and createTestfile.py for generating the test file from the test documents.
One file with source code to learn the model (nblearn.py) and one file with source code to classify new text (nbclassify.py).

###Description of each file###

createTrainingfile.py This file is used to generate the training file from a directory specified inside the code itself.

createTestFile.py This file is used to generate the test file from a directory specified inside the code itself.

nbclassify.py This mile contains the code to classify new text which has the model file as input.

nblearn.py This file contains the code to create a model file from the training file given as input.

spam.nb This file is created as the output of nblearn.py for the spam dataset which contains the learned model from training set.

spam.out This file is created as the output of nbclassify.py for the spam dataset which contains the output labels from test set.

sentiment.nb This file is created as the output of nblearn.py for the sentiment dataset which contains the learned model from training set.

sentiment.out This file is created as the output of nbclassify.py for the sentiment dataset which contains the output labels from test set.

### Explanation ###
Training file could look like this:

HAM subject : meeting today hi , could we have a meeting today . thank you . 
SPAM subject : low rates click here to apply for new low rates do not miss this chance !

To learn a classification model from the training data file,software will be invoked in the following way:

python3 nblearn.py TRAININGFILE MODELFILE

where TRAININGFILE is the name of the training file (this could be spam_training.txt for the spam dataset, and sentiment_training.txt for the sentiment dataset), MODELFILE is the name of the file that will contain the model that the classifier will learn (for the spam dataset the file name could be spam.nb, and sentiment.nb for the sentiment dataset).
To classify a file with new documents, software will be invoked in the following way:

python3 nbclassify.py MODELFILE TESTFILE

where MODELFILE is the name of the model file generated by nblearn, TESTFILE is the name of the file containing the features for the new documents to be classified.
