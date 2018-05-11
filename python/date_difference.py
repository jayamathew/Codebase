import pandas as pd

import numpy as np

from datetime import datetime, timedelta
 
frame['now'] = datetime.now()

frame
frame['DOB'] = pd.to_datetime(frame['date_var'],unit='ns') 

frame
frame.dtypes

#difference of 2 date variables
frame['age'] = (frame['now'] - frame['DOB'])

frame
