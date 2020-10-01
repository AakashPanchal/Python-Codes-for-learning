import pandas as Pd
import numpy as np
world = {
    'Team': ['West Indies','West Indies','India','pakistan','Sri Lanka','Austraila','Austraila','Austraila','India','Austraila'],
    'Rank': [7,7,5,8,6,1,5,7,1,2],
    'Year': [1998,1857,1997,1963,1478,2548,5896,5889,3698,7412]}
df=Pd.DataFrame(world)
# print(df.groupby(['Team','Rank']).groups)
# for name, group in df.groupby('Team'):
#     print('Group Name:',name)
#     print(group['Rank'])
#     print('============================================')
# for name, group in df.groupby('Year'):
#     print("YEar", name)
#     print(group)
#     print("========================")

df1 = df.groupby('Team')
print( df1.get_group('India'))