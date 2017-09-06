# Data Preprocessing Template

# Importing the dataset
datasets = read.csv('Data.csv')
datasets = datasets[, 2:3]


#Splitting the dataset into the Training set and Test set
#install.packages('caTools')
library(caTools)
set.seed(123)
split= sample.split(datasets$Purchased, SplitRatio = 0.8)
training_set=subset(datasets, split == TRUE)
test_set=subset(datasets, split == FALSE)

# #Feture Scaling 
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])


