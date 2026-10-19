import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
df = pd.read_csv(r'C:\Users\aneel.kumar\OneDrive - IMCS Group\Downloads\House Price India.csv')
df.columns

df.shape
x = df.iloc[:,2:22].values
x
y = df.iloc[:,-1].values
y
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
regressor = LinearRegression()
regressor.fit(x_train,y_train)
y_predict = regressor.predict(x_test)
y_predict

plt.scatter(y_test,y_predict)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Price vs Predicted Price')
plt.show()

import pickle
filename = 'house_price_model.pkl'
with open(filename,'wb') as file:
    pickle.dump(regressor,file)
print("Model has been pickled and saved as 'house_price_model.pkl'")

import os 
print(os.getcwd())
