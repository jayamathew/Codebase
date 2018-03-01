Created_date = "28.12.2014 15:02"

Date <- sapply(strsplit(as.character(Created_date), " "), "[", 1)
Time <- sapply(strsplit(as.character(Created_date), " "), "[", 2)

Date_Modified <- as.Date(Date, format = "%d.%m.%Y")

print(Date_Modified)

out = data.frame(Date_Modified)

datetime= "2013-07-25 08:32:07"

datetime_edit = as.POSIXct(datetime, tz=Sys.timezone())

datetime_edit1 = strftime(datetime_edit, format="%Y-%m-%d")

data.set <- as.data.frame(datetime_edit1)

Date=c("8/6/2015", "8/20/2015", "7/9/2015") 

Date<-as.character(Date)

Date<-as.Date(as.POSIXct(strptime(Date, "%m/%d/%Y"), "GMT"))

Date<-format(Date, "%m/%d/%Y")

Date<-as.Date(Date, "%m/%d/%Y")

data.set <- as.data.frame(Date)
