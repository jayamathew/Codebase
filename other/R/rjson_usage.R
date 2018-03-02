library(rjson)

data <- fromJSON(json_str = as.character(dataset1), method = 'C')

out <- as.data.frame(data)