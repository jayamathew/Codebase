import re
import pandas as pd
import numpy as np
import datetime
from math import ceil

#import the data
input_data = pd.read_csv(aml_dir + 'test_file.csv')

# convert to datetime for filtering by date
input_data['hourly'] = pd.to_datetime(input_data['hourly'])

nrows=input_data.shape[0]

# check max date
max_datetime = max(input_data.hourly)
print(max_datetime)

# generating future data by hour
new_data = pd.DataFrame()

for x in range(4):
    print(x)
    new_data = new_data.append(input_data)

# check the new data
new_data.shape
new_data.head(5)

# check the maximum time stamp to generate hourly new time stamp
new_data['hourly'] = max_datetime

# create datetime stamps to fill in the hour column
rng = pd.date_range(max_datetime, periods=nrows*4, freq='H')
rng.shape

# add in this column of values to hourly
new_data['hourly']=rng

new_data.shape
new_data.head(5)

# df is a pandas DataFrame, save as CSV for future use
new_data.to_csv('new_data.csv', sep=',', index=False)


