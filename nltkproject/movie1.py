import nltk
import random
from nltk.corpus import movie_reviews
import pickle

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
print(len(documents))

#print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

#print (all_words)    

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]

#print (word_features)


def find_features(document):
    words = set(document)
    features = {}
    i=0
    for w in word_features:
    	if w in words:
    		features[w] = i + 1

    return features
#print(all_words.most_common(25))
#print(all_words[""])
#feature1=find_features(movie_reviews.words('neg/cv000_29416.txt'))


#print((find_features(movie_reviews.words('pos/cv988_18740.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

#for rev, category in documents:
#	print (len(rev))




# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]

#print (featuresets[800])

classifier = nltk.NaiveBayesClassifier.train(training_set):x

save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()


classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()






classifier.show_most_informative_features(15)

#print (len(featuresets)):x