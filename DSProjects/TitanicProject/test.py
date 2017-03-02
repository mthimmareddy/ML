import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file='titanic_data.csv'

df=pd.read_csv(file)
#Give the number of rows and columns in Dataframe
print (df.shape)
#print (df.head())
print (df.describe())
#if the count not equal to total number of rows we can identify missing values
#to fill the missinn values in df

print (df['Age'].mean())
df['Age'].fillna(df['Age'].mean(),inplace=True)
print (df.describe())

print (df.Survived.value_counts())
#print (plt.show())

print (df.Sex.value_counts())

#plt.plot(df[df.Sex =='female'])
#print (df.Fare.hist())
#plt.show()
#print (df[df.Sex == 'female'].head())
#print (df[Sex=='male'].value_counts())

#print (df[~df.Cabin.isnull()])


#print (df.head())
infants=df[(df.Age <10) & (df.Sex == 'female')]
#female= df[df.Sex =='female']
#female_kid= infants & female
#print (infants.Survived.value_counts())

print (infants.Survived.value_counts())

females=df[df.Sex == 'female']
print (females.Survived.value_counts())

males=df[df.Sex == 'male']
print (males.Survived.value_counts())
print (df.head())
print (df.ix[:,3:8].head())
#print ("Females Survied {} out of  {}".format(females.Survived.value_counts,females.shape))
#df.plot()
#print ("{} {} {}" .format(df['Age'], df['Sex'],df['Fare']))
#df[['Age','Sex','Fare']].plot()
#plt.show()
#plt.show()