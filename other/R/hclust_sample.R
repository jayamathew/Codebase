data.set = rbind(dataset1);

fp <- data.set

#calc Eucledian distance
fp.dist <- dist(fp, method = "euclidean")

#using ward.D method
fp.hclust = hclust(fp.dist, method="ward.D")
plot(fp.hclust) 
print(fp.hclust$labels)

#
df <- data.frame(cbind(fp.hclust$labels,cutree(fp.hclust, k = 5)))
print(tail(df))