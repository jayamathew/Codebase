test_agg = aggregate(state.x77, list(Region = state.region), mean)

test_wide <- reshape(Indometh, v.names = "conc", idvar = "Subject", timevar = "time", direction = "wide")
