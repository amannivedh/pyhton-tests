import pandas as pd
df=pd.read_csv('salaries_by_college_major.csv')

df.head()
df.shape
df.columns
df.isna()

clean_df=df.dropna()
clean_df.tail()


clean_df['Starting Median Salary'].max()

clean_df["Undergraduate Major"].loc[43]
clean_df.loc[43]


#highest mid career salary
print(clean_df['Mid-Career Median Salary'].max())
print(f'Index for the max mid career salary: {clean_df["Mid-Career Median Salary"].idxmax()}')
clean_df["Undergraduate Major"][8]

#lowest starting and mid career salary
print(clean_df["Starting Median Salary"].min())
clean_df['Undergraduate Major'].loc[clean_df["Starting Median Salary"].idxmin()]
clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

#lowest risk major
clean_df["Mid-Career 90th Percentile Salary"]-clean_df["Mid-Career 10th Percentile Salary"]

#inserting this data to the pandas dataframe
spread_col=clean_df['Mid-Career 90th Percentile Salary']-clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1,'Spread',spread_col)
clean_df.head()

#sorting by lowest spread
low_risk=clean_df.sort_values("Spread")
low_risk[["Undergraduate Major","Spread"]].head()

#majors with highest potential
highest_pot=clean_df.sort_values("Mid-Career 90th Percentile Salary",ascending=False)
highest_pot[['Undergraduate Major',"Mid-Career 90th Percentile Salary"]].head()


#majors with the greatest slaries in spread
highest_spread=clean_df.sort_values("Spread",ascending=False)
highest_spread[['Undergraduate Major',"Spread"]].head()
