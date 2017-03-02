import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import Perceptron
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split

X=pd.read_csv('titanic_data.csv')
y=X.pop('Survived')

print (X.head())
print (X['Sex'].head())
print (y.head())

print (X.describe())

X['Age'].fillna(X['Age'].mean(),inplace=True)

print (X.describe())

#Non Categerial variables 

print (X.dtypes)

numeric_variables=list(X.dtypes[X.dtypes!="object"].index)
print (X[numeric_variables].head())
#To describe categerical data types
print (X.columns[X.dtypes== "object"])
print (X[X.columns[X.dtypes == "object"]].describe())
X.drop(['Name','PassengerId','Ticket'],axis=1,inplace=True)
print (X.head())
print (X.shape)
print (y.shape)

categerical_variables =['Sex','Cabin','Embarked']

#print (X['Cabin'])
#print (X['Embarked'])

def clean_cabin(x):
	try:
		return x[0]
	except TypeError:
		return None

X['Cabin']=X.Cabin.apply(clean_cabin)
#print (X['Cabin'])


#print (X['Embarked'].head())

for variable in categerical_variables:
	X[variable].fillna('Missing',inplace=True)
	dummeis=pd.get_dummies(X[variable],prefix=variable)
	X=pd.concat([X,dummeis],axis=1)
	X.drop([variable],inplace=True,axis=1)
print (X.head())

#print (X['Embarked'])'''
print (X.columns,X.shape)
#plt.plot(X)
#plt.show()
X[['Pclass','Age','Fare','Sex_female','Sex_male']].plot()
#plt.show()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)
#X.plt[]
#clf=MultinomialNB()
clf=RandomForestClassifier(n_estimators=100)
#clf=Perceptron()

clf.fit(X_train,y_train)
pred=clf.predict(X_test)
#print (pred)
#print (actual)
actual=y_test.values
print(actual)

count=0
total=len(pred)
#print (len(pred))
i=0

for i in range (len(pred)):
	if (pred[i]==actual[i]):
		count=count+1

print (count)
accuracy=count/total
print ("Accuracy:{}".format(accuracy))