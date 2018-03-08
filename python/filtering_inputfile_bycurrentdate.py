# Sample code to filter data by the current time stamp for a time period

# Check datetime range (assuming variable is called hourly)
min_datetime = min(input_data.hourly)
print(min_datetime)

max_datetime = datetime.datetime.now()
print(max_datetime)

# Cut off dates for filtering the dataset
scoring_cutoff_min = max_datetime - pd.to_timedelta(60, unit='d')
print(scoring_cutoff_min)

scoring_cutoff_max = max_datetime + pd.to_timedelta(2, unit='d')
print(scoring_cutoff_max)

# Filter the input data by these cutoffs
input_data_filter = input_data[((input_data['hourly'] >= scoring_cutoff_min) & (input_data['hourly'] <= scoring_cutoff_max))]  

# Check the filtered date range
print(min(input_data_filter.hourly))
print(max(input_data_filter.hourly))