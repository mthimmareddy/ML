import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

# Change False to True for this block of code to see what it does

# DataFrame apply() - use case 2
if False:   
    print df.apply(np.mean)
    print df.apply(np.max)

#print (second_largest(df['a']))
  
def second_largest(columns):
    new=columns.sort_values(ascending=False)
    return new.iloc[1]


#print (second_largest(df['a']))

print (df.apply(second_largest))
    
    

    
