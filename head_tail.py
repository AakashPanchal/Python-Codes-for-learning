import pandas as pd , numpy as np
df = pd.DataFrame({'a': pd.Series(np.arange(1,50)),'b': pd.Series(np.arange(51,100))})
print(df.tail(10))