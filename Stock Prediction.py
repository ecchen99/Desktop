#Predict price of stock on a specifc day
#Import libraries
from sklearn.svm import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Load the data
from google.colab import files
files.upload()

#Store the data
df = pd.read_csv('GME.csv')
#Show the data
df

#Show and store last row of data
actual_price = df.tail(1)
#Show the data
actual_price

#Get all of the data except the last row
df = df.head(len(df)-1)
df

#Create empty lists to store independent and dependent data
days = list()
adj_close_prices = list()

#Get only the date and the adjusted close prices
df_days = df.loc[:, 'Date']
df_adj_close = df.loc[:,'Adj Close']

#Create the independent data set (dates)
x=0
for day in df_days:
  x = x+1
  days.append([int(x)])
#Create the dependent data set (adjust close prices)
for adj_close_price in df_adj_close:
  adj_close_prices.append(float(adj_close_price))

#Show the days
days

#Show prices
adj_close_prices

#Create 3 models for predictions

lin_svr = SVR(kernel='linear', C=1000.0)
lin_svr.fit(days, adj_close_prices)

poly_svr = SVR(kernel='poly', C=1000.0, degree=2)
poly_svr.fit(days, adj_close_prices)

rbf_svr = SVR(kernel='rbf', C=1000.0, gamma = 0.85)
rbf_svr.fit(days, adj_close_prices)

#Plot models
plt.figure(figsize =(16,8))
plt.scatter(days, adj_close_prices, color = 'black', label ='Data')
plt.plot(days,rbf_svr.predict(days), color = 'green', label = 'RBF Model')
plt.plot(days,poly_svr.predict(days), color = 'blue', label = 'Polynomial Model')
plt.plot(days,lin_svr.predict(days), color = 'red', label = 'Linear Model')
plt.xlabel('Days')
plt.ylabel('Adj Close Price')
plt.legend()
plt.show()

x = int(input('How many days ahead?'))
new_day = 253 + x
day = [[new_day]]
print('RBF SVR Predicted Price:', rbf_svr.predict(day))
print('Polynomial SVR Predicted Price:', poly_svr.predict(day))
print('Linear SVR Predicted Price:', lin_svr.predict(day))

#Show the actual price
print('Actual Price:', actual_price['Adj Close'])

#Clear list
days.clear()
adj_close_prices.clear()

newdays = list()

#All days
for i in range(int(new_day)):
    days.append([i])

days

#Just new days
for i in range(253,int(new_day)):
    newdays.append([[i]])

newdays

#Append known close price into price
for adj_close_price in df_adj_close:
  adj_close_prices.append(float(adj_close_price))

adj_close_prices

#For loop RBG regression to get new price and append to adj_close_prices list
for i in newdays:
  x = rbf_svr.predict(i)
  adj_close_prices.append(x)
 adj_close_prices

 #Plot models
plt.figure(figsize =(16,8))
plt.plot(days,lin_svr.predict(days), color = 'green', label = 'Linear Model')
plt.xlabel('Days')
plt.ylabel('Adj Close Price')
plt.legend()
plt.show()
