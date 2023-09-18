
import pandas as pd
import matplotlib.pyplot as plt

# Read the .csv file and store it in a Pandas dataframe

df=pd.read_csv("QueryResults.csv")

df.head()
df.tail()
df.shape
df.count()


# Which Programming language has had the highest total number of posts of all time?
df.groupby("TagName").sum()


# Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.
# 
# **Challenge**: How many months of data exist per language? Which language had the fewest months with an entry? 
# 

df.groupby("TagName").count()


# ## Data Cleaning
# 
# Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"

# In[43]:


type(df['m'][1])


# In[44]:


print(pd.to_datetime(df['m'][1]))
type(pd.to_datetime(df['m'][1]))


# In[69]:


df.date=pd.to_datetime(df.m)
df.head()


# ## Data Manipulation
# 
# 

# **Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe.

# In[70]:


reshaped_df=df.pivot(index="m",columns='TagName',values="posts")


# In[71]:


reshaped_df.head(5)


# In[72]:


reshaped_df.shape
reshaped_df.columns


# **Challenge**: Count the number of entries per programming language. Why might the number of entries be different? 

# In[73]:


reshaped_df.count()


# In[74]:


reshaped_df.fillna(0,inplace=True)
reshaped_df.head()


# In[75]:


reshaped_df.isna().values.any()


# ## Data Visualisaton with with Matplotlib
# 

# **Challenge**: Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart.

# In[76]:


import matplotlib.pyplot as plt


# In[80]:


plt.plot(reshaped_df.index,reshaped_df.java)


# **Challenge**: Show two line (e.g. for Java and Python) on the same chart.

# In[81]:


plt.plot(reshaped_df.index,reshaped_df.java)
plt.plot(reshaped_df.index,reshaped_df.python)


# # Smoothing out Time Series Data
# 
# Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html). 

# In[82]:


roll_df=reshaped_df.rolling(window=6).mean()


# In[88]:


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date",fontsize=14)
plt.ylabel("No of posts",fontsize=14)
plt.ylim(0,35000)
for column in roll_df.columns:
    plt.plot(roll_df.index,roll_df[column],linewidth=3,label=roll_df[column].name)
plt.legend(fontsize=16)    


# In[ ]:




