# -*- coding: utf-8 -*-
"""Optimizing_Flight_Booking_Decisions_through_Machine_Learning_Price_Predictions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UH_U2WAWmB8244b1eiQhe0UT1861JhAi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix
import warnings
import pickle
from scipy import stats

warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')

data = pd.read_csv("/content/Data_Train.csv")
data.head()
data.shape
data.isnull().sum()
data.dropna(inplace=True)
data.isnull().sum()
Category = ['Airline', 'Source', 'Destination', 'Additional_Info']

for i in Category:
    print(i, data[i].unique())
category_cols=data.select_dtypes (include=['object']) .columns
category_cols
#plotting a barchart for each of the categorical value
#for column in category_cols:
  #plt.figure(figsize=(20,4))
  #plt.subplot(121)
  #data[column].value_counts().plot(kind='bar')
  #plt.title(column)
data.Route =  data.Route.str.split('->')
data['City1']=data.Route.str[0]
data['City2']=data.Route.str[1]
data['City3']=data. Route.str[2] 
data['City4']=data. Route.str[3]
data['City5']=data.Route.str[4]
data['City6']=data. Route.str[5]
data.Date_of_Journey=data.Date_of_Journey.str.split('/')
data.Date_of_Journey

#Treating the data_column
data['Date']=data.Date_of_Journey.str[0]
data['Month']=data.Date_of_Journey.str[1]
data['Year']=data.Date_of_Journey.str[2]
data.Dep_Time=data.Dep_Time.str.split(':')
data['Dep_Time_Hour']=data.Dep_Time.str[0]
data['Dep_Time_Mins']=data.Dep_Time.str[1]
data.Arrival_Time=data.Arrival_Time.str.split(' ')
data['Arrival_date']=data.Arrival_Time.str[1] 
data['Time_of_Arrival']=data. Arrival_Time.str[0]
data['Time_of_Arrival']=data.Time_of_Arrival.str.split(':')
data['Arrival_Time_Hour' ]=data.Time_of_Arrival.str[0]
data['Arrival_Time_Mins']=data.Time_of_Arrival.str[1]
#Next, we divide the 'Duration' column to 'Travel_hours' and Travel_mins'
data.Duration=data.Duration.str.split(' ')
data['Travel_Hours']=data.Duration.str[0]
data['Travel_Hours']=data['Travel_Hours'].str.split('h')
data['Travel_Hours']=data['Travel_Hours'].str[0]
data.Travel_Hours = data. Travel_Hours
data['Travel_Mins']=data.Duration.str[1]

#Next, we divide the 'Duration' column to 'Travel_hours' and Travel_mins'  24
data.Duration=data.Duration.str.split(' ')

data['Duration'] = data['Duration'].astype(str)
data['Travel_Hours']=data.Duration.str[0]
data['Travel_Hours']=data['Travel_Hours'].str.split('h') 
data['Travel_Hours']=data['Travel_Hours'].str[0]
data.Travel_Hours =data.Travel_Hours
data['Travel_Mins']=data.Duration.str[1]
data. Travel_Mins=data.Travel_Mins.str.split('m')   
data.Travel_Mins=data.Travel_Mins.str[0]

data. Total_Stops.replace('non_stop', 0, inplace=True)
data. Total_Stops = data. Total_Stops.str.split(' ')
data. Total_Stops=data. Total_Stops.str[0]

data. Additional_Info.unique()

data. Additional_Info.replace('No Info', 'No info', inplace=True)
data.isnull().sum

if 'City4' in data.columns and 'City5' in data.columns and 'City6' in data.columns:
    data.drop(['City4', 'City5', 'City6'], axis=1, inplace=True)

print(data.columns)

data.drop(['Date_of_Journey','Route', 'Dep_Time','Arrival_Time','Duration'], axis=1, inplace=True)
data.drop(['Time_of_Arrival'], axis=1, inplace=True)

data.isnull().sum()
data.info()

data['City3'].fillna ('None', inplace=True)
data['City2'].fillna ('None', inplace=True)
data['Arrival_date'].fillna (data['Date'], inplace=True)
data['Travel_Mins'].fillna(0,inplace=True)
data.info()

data.Date=data.Date.astype('int64')
data.Month=data. Month.astype('int64')
data.Year=data.Year.astype('int64')
data.Dep_Time_Hour=data.Dep_Time_Hour.astype('int64')
data.Dep_Time_Hour=data.Dep_Time_Hour.astype('int64')
data.Dep_Time_Mins=data.Dep_Time_Mins.astype('int64')

data. Arrival_date=data.Arrival_date.astype("int64")
data.Arrival_Time_Hour=data. Arrival_Time_Hour.astype('int64')
data. Arrival_Time_Mins=data. Arrival_Time_Mins.astype('int64')

data.info()

data[data['Travel_Hours']=='5m']

data.Travel_Hours=data.Travel_Hours.astype('int64')

categorical=['Airline', 'Source', 'Destination', 'Additional Info', 'City1']

numerical=['Total_Stops', 'Date', 'Month', 'Year', 'Dep_Time_Hour', 'Dep_Time_Mins', 'Arrival_date', 'Arrival_Time_Hour', 'Arrival_Time_Mins', 'Travel_Hours', 'Travel_Mins']

import seaborn as sns
c=1
plt.figure(figsize=(20,45))
for i in categorical:
  plt.subplot(6,3,c)
  sns.scatterplot(x=data[i],y=data.Price)
  plt.xticks(rotation=90)

  c=c+1
plt.show()

data[data. Price>50000]
data.head()
pd.set_option('display.max_columns',25)
data.head()

data['Year'].max()
sns.heatmap (data.corr(), annot=True)

plt.figure(figsize=(15,8))
sns.distplot(data.Price)

import seaborn as sns
sns.boxplot(data['Price'])


c=1
for i in numerical:
  plt.figure(figsize=(10,20))
  plt.subplot(6,3,c)
  sns.scatterplot(x = data[i], y=data.Price)
  plt.xticks(rotation=90)
#plt. tight_Layout (pad=3.0)
  C=c+1
plt.show()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data.Airline = le.fit_transform (data. Airline)
data.Source = le.fit_transform(data.Source)
data.Destination = le.fit_transform(data. Destination)
data.Total_Stops= le.fit_transform(data. Total_Stops)
data.City1=le.fit_transform(data.City1)
data.City2=le.fit_transform(data.City2)
data.City3=le.fit_transform(data.City3)
data.Additional_Info = le.fit_transform(data. Additional_Info)
data.head()
data.head()

data = data[['Airline', 'Source', 'Destination', 'Date', 'Month', 'Year', 'Dep_Time_Hour', 'Dep_Time_Mins','Arrival_date', 'Arrival_Time_Hour', 'Arrival_Time_Mins', 'Price' ]]
data.head()

### Scaling the Data
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
datal = ss.fit_transform(data)
datal = pd.DataFrame(datal, columns=data.columns)
datal.head()

y = datal['Price']
x = datal.drop(columns = ['Price'], axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)

x_train.head()

x_train.shape

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
rfr = RandomForestRegressor()
gb = GradientBoostingRegressor()
ad = AdaBoostRegressor()
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
for i in [rfr, gb,ad]:
  i.fit(x_train,y_train)
  y_pred=i.predict(x_test)
  test_score=r2_score (y_test,y_pred)
  train_score=r2_score (y_train, i.predict(x_train))
if abs (train_score-test_score)<=0.2:
  print(i)
print("R2 score is", r2_score (y_test,y_pred))
print("R2 for train data", r2_score (y_train, i.predict(x_train)))
print("Mean Absolute Error is", mean_absolute_error(y_pred,y_test))
print("Mean Squared Error is", mean_squared_error(y_pred,y_test))
print("Root Mean Sqaured Error is", (mean_squared_error(y_pred,y_test, squared=False)))

from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
knn=KNeighborsRegressor()
svr=SVR()
dt=DecisionTreeRegressor()
for i in [knn, svr,dt]:
  i.fit(x_train,y_train)
  y_pred=i.predict(x_test)
  test_score=r2_score (y_test,y_pred)
  train_score=r2_score (y_train,i.predict(x_train))
  if abs(train_score-test_score)<=0.1:
    print(i)
    print('R2 Score is', r2_score (y_test,y_pred))
    print('R2 Score for train data', r2_score (y_train, i.predict(x_train)))
    print('Mean Absolute Error is', mean_absolute_error(y_test,y_pred))
    print('Mean Squared Error is', mean_squared_error(y_test,y_pred))
    print('Root Mean Squared Error is', (mean_squared_error(y_test, y_pred, squared=False)))

from sklearn.model_selection import cross_val_score
for i in range(2,5):
  cv=cross_val_score (rfr,x,y,cv=i)
  print(rfr,cv.mean())

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
model = keras.Sequential()
model.add(Dense (7, activation = 'relu', input_dim=11))
model.add(Dense (7, activation='relu'))
model.add(Dense(1, activation="linear"))
model.summary()

model.compile(loss = 'mse', optimizer ='rmsprop', metrics=['mae'])
model.fit(x_train, y_train, batch_size = 20, epochs = 10)

from sklearn.model_selection import cross_val_score
for i in range(2,5):
  cv=cross_val_score (rfr,x,y,cv=i)
  print (rfr, cv.mean())
from sklearn.model_selection import RandomizedSearchCV
param_grid={'n_estimators': [10, 30, 50, 70, 100], 'max_depth': [None, 1, 2, 3], 'max_features': ['auto', 'sqrt']}
rfr=RandomForestRegressor()
rf_res = RandomizedSearchCV(estimator=rfr, param_distributions=param_grid, cv=3, verbose=2,n_jobs=-1)
rf_res.fit(x_train,y_train)

gb = GradientBoostingRegressor()

# Define parameter grid to search over
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.1, 0.01, 0.001]
}

# Perform randomized search over parameter grid
gb_res = RandomizedSearchCV(estimator=gb, param_distributions=param_grid, cv=3, verbose=2, n_jobs=-1)
gb_res.fit(x_train, y_train)

rfr=RandomForestRegressor (n_estimators=10, max_features='sqrt', max_depth=None)
rfr.fit(x_train,y_train)
y_train_pred=rfr.predict(x_train)
y_test_pred=rfr.predict(x_test)
print("train accuracy", r2_score (y_train_pred,y_train))
print("test accuracy", r2_score (y_test_pred,y_test))

from sklearn.model_selection import cross_val_score
for i in range(2,5):
  cv=cross_val_score (gb, x,y,cv=i)
  print (rfr, cv.mean())

gb=GradientBoostingRegressor (n_estimators=10, max_features='sqrt', max_depth=None)
gb.fit(x_train,y_train)
y_train_pred=gb.predict(x_train)
y_test_pred=gb.predict(x_test)
print("train accuracy", r2_score (y_train_pred,y_train)) 
print("test accuracy", r2_score (y_test_pred,y_test))

from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
knn=KNeighborsRegressor()
svr=SVR()
dt=DecisionTreeRegressor()
for i in [knn, svr,dt]:
  i.fit(x_train,y_train)
  y_pred=i.predict(x_test)
  test_score=r2_score (y_test,y_pred)
  train_score=r2_score (y_train, i.predict(x_train))
  if abs(train_score-test_score)<=0.1:
    print(i)

knn=KNeighborsRegressor (n_neighbors=2, algorithm= 'auto', metric_params=None, n_jobs=-1)
knn.fit(x_train,y_train)
y_train_pred-knn.predict(x_train)
y_test_pred-knn.predict(x_test)
print("train accuracy", r2_score (y_train_pred,y_train))
print("test accuracy", r2_score (y_test_pred,y_test))

from sklearn.model_selection import cross_val_score
for i in range(2,5):
  cv=cross_val_score (knn, x,y,cv=i)
  print (knn, cv.mean())
predicted_values = pd.DataFrame({'Actual' :y_test, 'Predicted' :y_pred})
predicted_values

import pickle
pickle.dump(rfr,open('flight_booking.pkl','wb'))

from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd
model=pickle.load(open ('flight_booking.pkl','rb'))

app = Flask (__name__)

@app.route("/")
def home():

  return render_template('/content/Flask/home.html')
@app.route("/content/Flask/predict.html")
def pred():
  return render_template('/content/Flask/predict.html')
@app.route("/pred", methods=['POST', 'GET'])
def predict():
  x = [[int(x) for x in request.form.values()]]
  print(x)
  x = np.array(x)
  print(x.shape)
  print (x)
  pred = model.predict(x)
  print (pred[0])
  return render_template('/content/Flask/submit.html', prediction_text=pred[0])
if __name__ == "__main__":
  app.run(debug=False)