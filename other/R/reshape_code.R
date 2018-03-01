library(reshape)

# Sample operation

mdata <- melt(dataset, id=c("orderid", "item")) 

table = cast(mdata, orderid~item+variable, mean)
table[is.na(table)] 

data.set = data.frame(table)

# transpose data
mdata <- t(dataset1)

library(reshape2)

fp.cast <- dcast(data = data.set, formula = ProductName ~ TermName, value.var = "Score", fun.aggregate = sum)

out <- as.data.frame(fp.cast)