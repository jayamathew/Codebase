# Sample code from https://stackoverflow.com/questions/42941310/creating-pandas-dataframe-with-datetime-index-and-random-values-in-column/42941507

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

date_today = datetime.now()
days = pd.date_range(date_today, date_today + timedelta(7), freq='D')

np.random.seed(seed=1111)
data = np.random.randint(1, high=100, size=len(days))
df = pd.DataFrame({'test': days, 'col2': data})
#df = df.set_index('test')
print(df)

df.head(2)

df.dtypes

#Extracting date from datetime variable

df['just_date'] = df['test'].dt.date

df