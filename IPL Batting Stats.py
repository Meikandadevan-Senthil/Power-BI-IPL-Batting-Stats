#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt # importing required packages
import numpy as np
import pandas as pd
import math 
import seaborn as sns


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


data = pd.read_csv("D:/Cricket/T20/ipl_batting.csv") # loading dataset 


# In[4]:


data.info()


# In[5]:


data.head()


# In[6]:


data['100'] = data['100'].replace(to_replace='-',value='0')


# In[7]:


data['100'] = pd.to_numeric(data['100'])


# In[8]:


data['50'] = data['50'].replace(to_replace='-',value='0')


# In[9]:


data['50'] = pd.to_numeric(data['50'])


# In[10]:


data['0'] = data['0'].replace(to_replace='-',value='0')


# In[11]:


data['0'] = pd.to_numeric(data['0'])


# In[12]:


data['NO'] = data['NO'].replace(to_replace='-',value='0')


# In[13]:


data['NO'] = pd.to_numeric(data['NO'])


# In[14]:


highest = data['HS']


# In[18]:


high = []
for i in highest:
    if len(i)==2:
        if i[-1]=='*':
            i = i[0:1]
        else:
            i = i
        high.append(i)
    if len(i)==3:
        if i[-1]=='*':
            i = i[0:2]
        else:
            i = i
        high.append(i)
    if len(i)==4:
        i = i[0:3]
        high.append(i)


# In[19]:


data['HS'] = high


# In[20]:


data['HS'] = pd.to_numeric(data['HS'])


# In[21]:


data.info()


# In[22]:


year = data['Span']
syear = []
eyear = []
for i in year:
        j = i[0:4]
        syear.append(j)
        k =  i[5:]
        eyear.append(k)


# In[23]:


data['SYear'] = syear
data['EYear'] = eyear


# In[24]:


data['SYear'] = pd.to_numeric(data['SYear'])
data['EYear'] = pd.to_numeric(data['EYear'])


# In[25]:


data.info()


# In[26]:


data.head()


# In[27]:


data.columns


# In[28]:


# Define original column names
original_column_names = ['Player', 'Span', 'Mat', 'Inns', 'NO', 'Runs', 'HS', 'Ave', 'BF', 'SR',
       '100', '50', '0', '4s', '6s', 'SYear', 'EYear']
# Create DataFrame with original column names
df = pd.DataFrame(data, columns=original_column_names)


# In[29]:


# Define new column names
new_column_names = ['Player', 'Span','Matches Played', 'Innings Played', 'Not Outs', 'Total Runs', 
                    'Highest Score', 'Batting Average', 'Balls Faced', 'Strike Rate', 
                    'Centuries', 'Half Centuries', 'Ducks', 'Fours', 'Sixes', 
                    'Start Year', 'End Year']


# In[30]:


# Rename columns
df = df.rename(columns=dict(zip(original_column_names, new_column_names)))


# In[32]:


# Save DataFrame to CSV
df.to_csv("D:/Cricket/Orange_data/T20/IPLBatting.csv", index=False)


# In[ ]:




