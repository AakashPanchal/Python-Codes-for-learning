import pandas as pd, matplotlib.pyplot as mpt, numpy as np
mpt.figure(figsize=(50,50))
dataset = pd.read_csv('allcon.csv')
# print(dataset.shape)
# print(dataset.head(20))
# print(dataset.dtypes)
# print(dataset.describe())

select_area = dataset.loc[:, ['Country', 'GDP ($ per capita)','Birthrate']]
# for i in select_area.itertuples():
#     if i[2] < 500:
#         print(i)
x=np.array(select_area['GDP ($ per capita'])
y=np.array(select_area['Birthrate'])
mpt.scatter(x,y)
mpt.xlim(0,2000)
mpt.show()