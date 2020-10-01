import pandas as pd, numpy as np

gf = pd.DataFrame(np.random.randn(5,4), columns=['Col-1','Col-2','Col-3','Col-4'])
for key, value in gf.iteritems():
    print(key,value)