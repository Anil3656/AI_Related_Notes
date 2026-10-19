#Simple Linear Regression Ml Model 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\aneel.kumar\OneDrive - IMCS Group\Desktop\Aneel\Naresh_IT\Salary_Data.csv')

X = dataset.iloc[:,:-1]
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X, y,test_size= 0.2, random_state=0)


from sklearn.linear_model import LinearRegression     #Linearregression is my Algorithm   LR = SimpleLinear regression and Miltilinear regression

#reg is my Model
reg = LinearRegression()    
reg.fit(x_train, y_train) 

y_pred = reg.predict(x_test)

plt.scatter(x_test, y_test, color='red')
plt.plot(x_train,reg.predict(x_train),color='blue')
plt.title('Salary Vs Experience Test')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()

#Calculating the slope of simplelinear regression
m = reg.coef_
#constant
c = reg.intercept_

#Feature predicted values
exp_12 = (m*12) + c

exp_20 = (m*20) + c


bais = reg.score(x_train, y_train)
bais

variance = reg.score(x_test,y_test)
variance


#Stats For Simple Linear regression Model

#Finding The Mean
dataset.mean()
dataset['Salary'].mean()

#Finding Median
dataset.median()
dataset['Salary'].median()

#Finding Mode 
dataset.mode()
dataset['Salary'].mode()

#Finding Variance
dataset.var()
dataset['Salary'].var()

#Finding Standard Deviation
dataset.std()
dataset['Salary'].std()

#Coefficient of Variations(CV)

from scipy.stats import variation

variation(dataset.values)
variation(dataset['Salary'])

#Correlation
dataset.corr()
dataset['Salary'].corr(dataset['YearsExperience'])   

#Skewness 
dataset.skew()
dataset['Salary'].skew()


#Standard Error
dataset.sem()
dataset['Salary'].sem()


#Z-Score
import scipy.stats as stats

dataset.apply(stats.zscore)
stats.zscore(dataset['Salary'])

#Degree Of Freedom
a = dataset.shape[0] #It will gives no.of Rows in dataset
b = dataset.shape[1] #It will dives no.of Columns in Dataset

print("Number of Rows:",a)
print("Number of Columns: ",b)

degree_Of_Freedom = a-b
print(degree_Of_Freedom)

#SSR (Sum Of Square regression)
y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)


#SSE(sum of Square Error)
y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)
 
#SST (Sum of Square Total)
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values - mean_total)**2)
print(SST)

#r^2
r_square = 1 - SSR/SST
print(r_square) 
