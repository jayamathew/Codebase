library('Matrix')

sparse <- Matrix(0, nrow = 1000, ncol = 1000, sparse = TRUE)

x <- serialize(sparse, connection=NULL)

out <- as.data.frame(as.integer(x))