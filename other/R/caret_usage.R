library(caret)
set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = .8, list = FALSE, times = 1)
head(trainIndex)

irisTrain <- iris[ trainIndex,]
irisTrain$data <- 1
irisTest  <- iris[-trainIndex,]
irisTest$data <- 2

out <- as.data.frame(rbind(irisTrain,irisTest))