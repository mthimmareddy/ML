import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt

#from  sklearn.datasets  import  load_digits

from sklearn.neural_network import MLPClassifier

from sklearn.cross_validation import train_test_split
from sklearn.metrics.classification import accuracy_score

'''digits=load_digits()

df_x=pandas.DataFrame(digits.)'''

df=pd.read_csv('mnist.csv')

df_x=df.iloc[:,1:]
df_y=df.iloc[:,0]

x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)
#clf=RandomForestClassifier(n_estimators=100)
clf=MLPClassifier(activation='logistic',solver='sgd',hidden_layers=(10,15),random_state=1)
clf.fit(x_train,y_train)

actual=y_test.values

print (actual)
total=len(actual)
print ("Total values",total)

predictions=clf.predict(x_test)
total_right=len(predictions)
print ("Total Predictions",total_right)
i=0
count=0

for i in range(len(predictions)):
	if predictions[i] == actual[i]:
		count =count+1
print ("Number of right predictions",count)
accuracy=count/total

print ("Accuracy",accuracy)