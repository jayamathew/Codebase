library(magrittr)

quantile(rnorm(100), c(0.25, 0.75), na.rm = TRUE) %>% diff -> a

add(c(-3,+3)*a)
