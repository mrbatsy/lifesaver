# -*- coding: utf-8 -*-
"""ML_Practical_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i9pYi-K9ZeyNVUyyrJXvUU8bCBH8n2ZV
"""

import pandas as pd

df = pd.read_csv(r'/content/sample_data/uber.csv')

df

df.size

df.shape

df.isnull().sum()

df = df.drop('Unnamed: 0' , axis =1)

df

df = df.dropna(axis=0)

df

df = df.drop('key' , axis = 1)

df

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

df = df.assign(
    hour = df.pickup_datetime.dt.hour,
    day = df.pickup_datetime.dt.day,
    month = df.pickup_datetime.dt.month,
    year = df.pickup_datetime.dt.year,
    dayofweek = df.pickup_datetime.dt.dayofweek
)

df

df = df.drop('pickup_datetime' , axis='columns')

df

X = df.drop('fare_amount' , axis=1)

X

y = df['fare_amount']

y

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(X,y,random_state=40 , test_size = 0.2)

X_train

from sklearn.linear_model import LinearRegression

model_Linear_Regression = LinearRegression()

model_Linear_Regression.fit(X_train , y_train)

y_pred_liner = model_Linear_Regression.predict(X_test)

from sklearn.metrics import accuracy_score , mean_absolute_error ,mean_squared_error

print("Mean Square Error for LinearRegression")
mean_squared_error(y_pred_liner , y_test)

print("Root Mean Square Error for LinearRegression")
mean_squared_error(y_pred_liner , y_test , squared=False)

print("Mean Absolute Error for LinearRegression")
mean_absolute_error(y_pred_liner , y_test)

from sklearn.ensemble import RandomForestRegressor

model_Random_Forest = RandomForestRegressor(n_estimators=100)

model_Random_Forest.fit(X_train , y_train)

y_pred_random = model_Random_Forest.predict(X_test)

print("Mean Square Error for RandomForest")
mean_squared_error(y_pred_random , y_test)

print("Root Mean Square Error for RandomForest")
mean_squared_error(y_pred_random , y_test , squared=False)

print("Mean Absolute Error for RandomForest")
mean_absolute_error(y_pred_random , y_test)
