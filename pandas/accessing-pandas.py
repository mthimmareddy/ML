import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import style

plt.style.use('fivethirtyeight')


web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce_Rate':[65,67,78,65,45,52],
             'current_Rate':[23,34,45,34,23,78]}

df = pd.DataFrame(web_stats)

print (df)
print (df.set_index('Day',inplace=True))
print (df[['Visitors','Bounce_Rate']])
print (df.current_Rate)

df.to_csv("new1.csv")
df2=pd.read_csv('new1.csv')
print (df2)

#print(df['Bounce_Rate'],'Bounce_Rate')
#df['Visitors'].plot()
#plt.show()
#