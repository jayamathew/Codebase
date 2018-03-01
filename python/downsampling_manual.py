def azureml_main(dataframe1 = None, dataframe2 = None):
     
     # balance the classes so that pos-neg in a specified ratio
     
     import pandas as pd
     import random as rd
     import numpy as np
     from pandas import Series,DataFrame
     from random import sample
     
     d_class0 = dataframe1[dataframe1["Class"] == 0]
     d_class1 = dataframe1[dataframe1["Class"] == 1]
     
     numRows_class0 = len(d_class0.index)
     numRows_class1 = len(d_class1.index)
     
     # downsample the negative class 0
     df = pd.DataFrame(d_class0, columns=['Class'])

     rows = np.random.choice(df.index.values, numRows_class1)
     d_class0_downsampled  = df.ix[rows]
     
     # new output data frame containing 1:1 class ratios
     
     data_set = DataFrame()
     
     data_set = data_set.append(d_class0_downsampled)
     data_set = data_set.append(d_class1)     
     # shuffle the rows
     out = pd.DataFrame(data_set)
     out1 = out.iloc[np.random.permutation(len(out))]

     out2 = pd.DataFrame(out1)
    # Return value must be of a sequence of pandas.DataFrame    
     return out2,
