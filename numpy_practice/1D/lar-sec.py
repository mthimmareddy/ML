import numpy as np

list1=[10,20,5,3,12,6,7,45,34,23,67,89,90,64,43]
#Find the smallest and second largets in list
ele=np.array(list1)
ele.sort()
print ("List has {} as smallest and {} has second largets".format(ele[0],ele[len(ele)-2]))

