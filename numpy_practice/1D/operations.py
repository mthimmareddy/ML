import numpy as np


n1=np.array([1,2,3,45,1,78,90,23,45,67,87,64,43,52,97])
n2=np.array([1,2,3])
n3=np.array([False,False,True])

#Access the elements of n1 only greater than 30
if True:
	n4=n1[n1>30]
	print (n4)

#Vectorized Operations on numpy arrays
if True:
	arr1=np.array([1,2,3,4,5])
	arr2=np.array([3,4,5,6,7])
	print (arr1+arr2)
	print (arr1*2)

	
#Adding the boolen values with array
if True:
	print (n2+n3)

if True:
	a=np.array([1,2,3,4])
	b=a
	a+=np.array([1,1,1,1])
	print (b)

if True:
	a=np.array([1,2,3,4])
	b1=a
	a=a+np.array([1,1,1,1])
	print (b1)

#Slicing with numpy array
if True:
	a=np.array([1,2,3,4,5])
	slice=a[:3]
	slice[0]=100
	print (a)

