import numpy as np
import pandas as pd
path ='./test_data/tsfresh_features_all.csv'
data = pd.read_csv(path)
data.drop('id',inplace = True,axis = 1)
print((data.shape[0],data.shape[1]))
"""
data = data.dropna(how ='any',axis = 1)
data.columns=list(np.arange(data.shape[1]))
data.corr().to_csv('corr.csv')
"""