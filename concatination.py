import pandas as pd

a = pd.DataFrame({
    'Key': ['KO','K1','K2','K3','k6'],
    'A': ['A0','A1','A2','A3','a4'],
    'B': ['B0','B1','B2','B3','b4']
})

b = pd.DataFrame({
    'Key': ['KO','K1','K2','K3','k4'],
    'C': ['C0','C1','C2','C3','c4'],
    'D': ['D0','D1','D2','D3','d4']
})

# print(pd.concat([right,left], axis=0))
# print(pd.concat([right,left], axis=1))
print(pd.merge(a,b, on='Key', how='right'))
print("=================================")
print(pd.merge(a,b, on='Key', how='left'))
print("=================================")
print(pd.merge(a,b, on='Key', how='outer'))
print("=================================")
print(pd.merge(a,b, on='Key', how='inner'))
# print(right.append(left))
# print("=========================")
# print(left.append(right))