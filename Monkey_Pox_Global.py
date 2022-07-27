#!/usr/bin/env python
# coding: utf-8

# In[113]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# Exploring Monkey Pox Data
# Dataset From Global.Health

# Read dataset from url, using skipinitial attribute to remove extra space
url="https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv"
df=pd.read_csv(url,skipinitialspace = True,delimiter=',')

print(df)


# In[136]:


# Removing white space in column
# Convert the Gender column into lower case using Pandas’ str.lower() function 
# printing count
df["Gender"] = df["Gender"].str.strip()
df.Gender= df.Gender.str.lower()
print(df['Gender'].value_counts())



# Show results in pie chart
df2 = df.value_counts('Gender')
colors=['lightblue','blue','silver']
ax=df2.plot.pie(figsize=(10,10),startangle=15, 
                                   colors=colors,pctdistance=0.8,ylabel=(''),textprops={'fontsize': 14})
plt.title('Monkey Pox Cases Gender', color='black', size=18)


# In[53]:


# Counting how many countries currently listed
# by finding dimesions in array and sorting the unique elements

print(df["Country"].shape)
print(f'\n There are {len(df["Country"].unique())} contries listed here.\n')
df["Country"].unique()


# In[186]:


# Find out which countries have the highest case rate
print(df['Country'].value_counts())

# Save countries case rate into a list
country_list = df["Country"].value_counts()

# Make bar graph with countries case rate
color = ["#071e22","#1d7874","#679289","#f4c095","#ee2e31","#ffb563","#918450","#f85e00","#a41623","#9a031e","#d6d6d6","#ffee32","#ffd100","#333533","#202020"]
country_list[0:20].plot(kind='bar', width=.30, color=color, figsize=(25,20), fontsize=18)
plt.title('Top 20 Country with Highest Monkey Pox Case Rate', fontsize=24)
plt.ylabel('Case Rate', fontsize=18)
plt.xticks(rotation=20, ha='right')
plt.show()



