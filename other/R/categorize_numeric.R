data$Load_edit <- data$Load
data$Load_edit[data$Load > 100] <- 100

data$cat[data$Load > 75] <- "High"
data$cat[data$Load >= 40 & data$Load <= 74] <- "Medium"
data$cat[data$Load < 40] <- "Low"