from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps=PorterStemmer()
example="hi hello i am doing nltk foirst program, this is to learn the natural lanuage processing, hello manju stop thinking and start working hard as if you never seen"
#print(sent_tokenize(example))
#print(word_tokenize(example))
list1=word_tokenize(example)
print (list1)

#print (dir(nltk.word_tokenize))

#for word in word_tokenize(example):
	#print (word)


stop_words=set(stopwords.words('english'))
 
filtered_words=[]

for word in list1:
	if word not in stop_words:
		filtered_words.append(word)

print (filtered_words)	

stemming_list=['python','pythonly','pythoned','pythoning']	

for word in stemming_list:
	print(ps.stem(word))



