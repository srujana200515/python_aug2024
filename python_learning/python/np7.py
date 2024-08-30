import numpy as np 
d1=np.array([1,2,3,4,5,6])
d2=np.array([11,2,4,6,1,8])
data=np.stack((d1,d2),axis=0)
print(data)
corelation_matrix=np.corrcoef(data)
print(corelation_matrix,type(corelation_matrix))