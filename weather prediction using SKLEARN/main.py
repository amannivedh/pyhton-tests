import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error

%matplotlib inline
weather_df = pd.read_csv('weather.csv', parse_dates=['YEAR'], index_col='YEAR')
weather_df.head(5)

weather_df_num=weather_df.loc[:,['JAN','FEB','MAR','APR','MAY', 'JUN','JUL', 'AUG', 'SEP','OCT','NOV','DEC']]
weather_df_num.head()

weather_df_num.columns

weth=weather_df_num['2010':'2017']
weth.head(8)

weather_y=weather_df_num.pop('JAN')
weather_x=weather_df_num
train_X,test_X,train_y,test_y=train_test_split(weather_x,weather_y,test_size=0.2,random_state=4)
train_X.shape

#USING DECISION TREE MODEL
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(train_X,train_y)
prediction=regressor.predict(test_X)
np.mean(np.absolute(prediction-test_y))
for i in range(len(prediction)):
  prediction[i]=round(prediction[i],1)
pd.DataFrame({'Actual':test_y,'Prediction':prediction,'diff':(prediction-test_y)})

print("Mean absolute error: %.2f" % np.mean(np.absolute(prediction - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((prediction - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y,prediction ) )

#USING LINEAR REGRESSION MODEL
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(train_X,train_y)

prediction2 = model.predict(test_X)
np.mean(np.absolute(prediction2-test_y))
print('Variance score: %.2f' % model.score(test_X, test_y))

for i in range(len(prediction2)):
  prediction2[i]=round(prediction2[i],2)
pd.DataFrame({'Actual':test_y,'Prediction':prediction2,'diff':(test_y-prediction2)})

print("Mean absolute error: %.2f" % np.mean(np.absolute(prediction2 - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((prediction2 - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y,prediction2 ) )