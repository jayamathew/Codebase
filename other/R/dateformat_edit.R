Created_date = "28.12.2014 15:02"

Date <- sapply(strsplit(as.character(Created_date), " "), "[", 1)
Time <- sapply(strsplit(as.character(Created_date), " "), "[", 2)

Date_Modified <- as.Date(Date, format = "%d.%m.%Y")

print(Date_Modified)

out = data.frame(Date_Modified)
