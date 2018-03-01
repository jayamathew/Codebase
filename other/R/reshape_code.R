library(reshape)

# Sample operation

mdata <- melt(dataset, id=c("orderid", "item")) 

table = cast(mdata, orderid~item+variable, mean)
table[is.na(table)] 

data.set = data.frame(table)