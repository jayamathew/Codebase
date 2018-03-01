#Installing a new package in R
print(version)
install.packages("src/foo/mclust.zip", lib = ".", repos = NULL, verbose = TRUE)
success <- library("mclust", lib.loc = ".", logical.return = TRUE, verbose = TRUE)

print(success)
library(mlcust)

data(diabetes)
class = diabetes$class
table(class)
## class
## Chemical   Normal    Overt 
##       36       76       33
X = diabetes[,-1]

BIC = mclustBIC(X)
plot(BIC)

output = summary(BIC)

mod1 = Mclust(X, x = BIC)
output = summary(mod1, parameters = TRUE)

out = as.data.frame(output)
