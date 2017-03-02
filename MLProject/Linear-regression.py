import numpy as np
import pandas as pd

from sklearn import linear_model
from sklearn.cross_validation import train_test_split

from sklearn.datasets import load_boston

boston=load_boston()


df_x=pd.DataFrame(boston.data,columns=boston.feature_names)
df_y=pd.DataFrame(boston.target)

'''print (df_y)
df_y.columns=['target']

print (df_y.head())

df_new=pd.concat([df_x,df_y],axis=1)
print (df_new.head())

print (df_x.head())
R
print (df_x.shape)

print (df_x.describe())

print (df_x.columns)

print (df_y)'''

clf=linear_model.LinearRegression()
#from sklearn import tree
#clf=tree.DecisionTreeClassifier()
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)
clf.fit(x_train,y_train)
pr=clf.predict(x_test)



print (pr[0])
#print (a)
#print (y_test)

#mean square error
#print (a.mean())
np.mean((pr-y_test)**2)
#from sklearn.metrics import accuracy_score
#print (accuracy_score(y_test,pr))

#error=(a.mean()-y_test)

