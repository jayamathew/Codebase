library(lubridate)

data.set$out = as.Date(as.character(data.set$Input),format="%m/%d/%Y")
data.set$not_a_date_identification = is.na(data.set$out)