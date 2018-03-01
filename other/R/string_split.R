s <- strsplit(dataset1$v2, split = ",")
s1 <- data.frame(v1 = rep(dataset1$v1, sapply(s, length)), v2 = unlist(s))

# Sample operation
data.set = as.data.frame(s1) 