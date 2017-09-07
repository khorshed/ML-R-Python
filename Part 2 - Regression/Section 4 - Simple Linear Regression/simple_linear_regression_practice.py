
#Simple Linear Regression

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset= pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 1].values

#splitting the dataset into the Training and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state = 0)

#Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Preparing the Test set result

#y_pred= regressor.predict(X_test)

#Visualizing the training set result
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regressor.predict(X_train), color = "blue")
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visualization for the Test set result 
plt.scatter(X_test, y_test, color = "red")
t_predict = regressor.predict(X_train)
plt.plot(X_train, t_predict, color="blue")
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()