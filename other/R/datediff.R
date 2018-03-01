data.set$diff1 = difftime(data.set$dategel, data.set$Date, units = "days") # days
data.set$diff2 = difftime(data.set$dategel6, data.set$Date, units = "days") # days

data.set$Y = ifelse(data.set$diff1 > 0 & data.set$diff2 > 0 ,1,0)

out = as.data.frame(data.set)
