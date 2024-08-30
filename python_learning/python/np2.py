import numpy as np 
array1=np.array([17,11,13,2,5,3,])
mean_value=np.mean(array1)
median_value=np.median(array1)
sd_value=np.std(array1)

print('array1= \n',array1)
print("Mean=",median_value)
print('Median=',median_value)
print("standard deviation=",sd_value)
array2=array1.reshape(2,3)
print("Reshaped array=",array2)
array3=np.arange(2,12,0.2)
print("Array=",array3)




