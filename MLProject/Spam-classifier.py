import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from  sklearn.feature_extraction.text  import  CountVectorizer

from sklearn.naive_bayes import MultinomialNB

from sklearn.cross_validation import train_test_split

from  sklearn.feature_extraction.text  import  TfidfVectorizer

df=pd.read_csv('smsspam',sep='\t',names=['Status','Message'])

print (df.head())

df2=df[df.Status=='spam']
df3=df[df.Status !='spam']
print (df2.shape)
print (df3.shape)

def clean_data(x):
	if (x== 'spam'):
		return 1
	else:
	    return 0
df['Status']=df.Status.apply(clean_data)	

print (df.head())

df_x=df['Message']
df_y=df['Status']

x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)
cv1=TfidfVectorizer(min_df=1,stop_words='english')

xtraincv=cv1.fit_transform(x_train)
xtestcv=cv1.transform(x_test)

print (y_test)
#a=xtraincv.toarray()
actual=np.array(y_test)
print (actual)
#print (cv1.get_feature_names())
#print (cv1.inverse_transform(a[0]))
#print (a[0])

clf=MultinomialNB()

clf.fit(xtraincv,y_train)
pred=clf.predict(xtestcv)
#print (pred)
#print (actual)

count=0
print (len(pred))
i=0

for i in range (len(pred)):
	if (pred[i]==actual[i]):
		count=count+1

print (count)
'''
print (df['Status'].head())
df.loc[df["Status" =='spam'],"Status"]=1
df.loc[df["Status" =='ham'],"Status"]=0

print (df.head())'''
