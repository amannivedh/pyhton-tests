import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv('C:/Users/localadmin/Downloads/healthcare-dataset-stroke-data.csv')
plt.bar(df.work_type,df.gender,color='black') #bar graph
plt.show()

plt.figure(figsize=(15,5),dpi=100) #dpi=dot per inch
plt.plot(df.gender,df.smoking_status,'rH-',linewidth=2,markeredgecolor='g',markerfacecolor='y') #scatterplot

plt.hist(df.age,bins=[0,25,50,75,100])
plt.show() #histogram


sns.distplot(df.avg_glucose_level,hist=False)
plt.show() #wave-distplot

plt.pie(df.age)
plt.show() #pie-chart

