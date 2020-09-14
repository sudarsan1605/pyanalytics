#Topic ---- Case Study - Denco - Manufacturing Firm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%case details
#%%Objective
#Expand Business by encouraging loyal customers to Improve repeated sales
#Maximise revenue from high value parts
#%%Information Required
#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts
#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#%%%
#see all columns
pd.set_option('display.max_columns',15)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
#read data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
df=pd.read_csv(url)
df
df['custname'].unique()
df2 = df['custname'].value_counts()
plot1 = df2.head()
plot1
df.describe()
df.groupby('custname').sum().sort_values(by='revenue',ascending=0).head(5).plot(kind='bar')
df.iloc[1:,1:2].plot(kind='bar')
df.groupby('partnum').sum().sort_values(by='revenue',ascending=0).head(5).plot(kind='bar')

df.iloc[1:,0:1].head()
df.groupby('partnum').sum().sort_values(by='margin',ascending=0)
df.groupby(['custname','partnum']).size()
df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]    })
df4 = df.custname.value_counts().sort_values(ascending=False).head(5)
df4.region.value_counts().plot(kind='bar')
