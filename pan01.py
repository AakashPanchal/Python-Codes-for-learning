import pandas as pd
import numpy as np
arr= np.array([4,5,6,7,8,9,'Aakash'])
data_dic= {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
print(type(arr))
series= pd.Series(data_dic)
print(type(series))
print(series[1:])
listx=[{'in1': 1, 'in2':2},{'in1': 3, 'in2':4},{'in1': 5, 'in2':3 , 'in3':7}]
table=pd.DataFrame(listx, index=['Ak1','Ak2','Ak3'])
print(table)
series1= pd.Series([56,57,58],index=['In1','In2','In3'])
series2= pd.Series([70,72,72],index=['In1','In2','In3'])
table=pd.DataFrame({'Akp':series1,'PP':series2})
print(table)