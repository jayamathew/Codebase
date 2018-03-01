str<-"24 32, BLACKTOWN 2148"

library(stringr)
out <- str_match_all(str, "\\b[[:digit:]]{4,6}$")

out2 <- as.data.frame(out)