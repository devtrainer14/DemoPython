import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#import seaborn as sns

dataset = pd.read_csv('C:/Users/Hemant Verma/Desktop/Rupendra Data/share_13decdata.csv')
print(dataset.shape)
print(dataset.head())
print(dataset.describe())
print(dataset.columns)
dataset.plot(x='TIME', y='RS', style='o')
plt.title('time vs rs')
plt.xlabel('Time')
plt.ylabel('Rs')
plt.show()

x = dataset[['TIME']]
y = dataset['RS']

print("Time\n\n",x)
print("Rs\n\n",y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=0)

X_test=pd.DataFrame({
    'TIME':[13.00,13.05,13.10,13.15,13.20,13.25,13.30,13.35,13.40,13.45]
})
print("Customize")

print("X Train Shape :")
print(X_train.shape)
print("Y Train Shape :")
print(y_train.shape)
print("X Test Shape :")
print(X_test.shape)
print("Y Test Shape :")
print(y_test.shape)

print("X Train Data :")
print(X_train.head())
print("Y Train Data :")
print(y_train.head())
print("Y Test Data :")
print(X_test.head())
print("Y Test Data :")
print(y_test.head())

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print('y intercept: ',regressor.intercept_)

print('slope: ',regressor.coef_)

y_pred = regressor.predict(X_test)
#plt.plot(X_test,y_pred)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

from sklearn import metrics

#print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred))

#print('Mean Squared Error: ', metrics.mean_squared_error(y_test, y_pred))

#print('Root Mean Squared Error: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print(metrics.r2_score(y_test, y_pred))

