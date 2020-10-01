import pandas as pd , numpy as np
df = pd.DataFrame({'odd': np.arange(1,100,2),'even': np.arange(0,100,2)})
print(df.std())