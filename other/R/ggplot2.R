library(ggplot2)

data.df <- data.frame(Plant = c("Plant1", "Plant1", "Plant1", "Plant2", "Plant2", "Plant2"), Type = c(1, 2, 3, 1, 2, 3), Axis1 = c(0.2, -0.4, 0.8, -0.2, -0.7, 0.1), Axis2 = c(0.5, 0.3, -0.1, -0.3, -0.1, -0.8))

ggplot(data.df, aes(x = Axis1, y = Axis2, shape = Plant, color = Type)) + geom_point(size = 5)