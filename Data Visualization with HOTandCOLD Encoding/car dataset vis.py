import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('cars.csv')

df['brand'].value_counts()

pd.get_dummies(df,columns=['owner'])
plt.pie(df.owner=="First Owner")
plt.show() #pie chart with hot_and_cold encoded data

#hot and cold encoding using sklearn module

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

df=pd.read_csv('cars.csv')

x_train,x_test,y_train,y_test=train_test_split(df.iloc[:,0:4],df.iloc[:,-1],test_size=0.2,random_state=2)
ohe=OneHotEncoder(drop='first',sparse=False,dtype=np.int32)
x_train_new=ohe.fit_transform(x_train[['fuel','owner']])
print(x_train_new)

plt.figure(figsize=(12,5),dpi=100)
plt.bar(df.owner,df.selling_price)
plt.show() #bar graph of encoded data

