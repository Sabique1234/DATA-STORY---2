import numpy as np
import pandas as pd 

df = pd.DataFrame(np.array([[2,3],[3,20],[4,200],[5,200]]),
                    columns=['p','q'])
df.quantile(.1)       

print(df)