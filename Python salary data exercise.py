#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


import matplotlib as plt


# In[4]:


import numpy as np 


# In[5]:


#Read csv file
df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")


# In[6]:


df


# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.head(10)


# In[10]:


df.head(20)


# In[11]:


df.head(50)


# In[12]:


df.dtypes


# In[13]:


df.columns


# In[14]:


df.axes


# In[15]:


df.shape


# In[16]:


df.size


# In[17]:


df.ndim


# In[18]:


df.values


# In[19]:


df.count


# In[20]:


df.shape


# In[21]:


df.describe 


# In[22]:


df.max


# In[23]:


df.max()


# In[24]:


df.min()


# In[25]:


df.std()


# In[26]:


df.dropna()


# In[27]:


df.describe()


# In[28]:


df.mean()


# In[30]:


df.discipline.value_counts()


# In[31]:


df.discipline


# In[33]:


df.discipline


# In[40]:


df.mean()


# In[35]:


df.describe()


# In[38]:


df.std()


# In[39]:


df.head(50).mean()


# In[42]:


df[:50].mean()


# In[43]:


df.rank


# In[44]:


df.phd


# In[46]:


df.phd.count()


# In[47]:


df.phd.mean()


# In[48]:


df.phd.describe()


# In[ ]:




