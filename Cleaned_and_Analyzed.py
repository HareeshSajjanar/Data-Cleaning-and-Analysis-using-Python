#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


df=pd.read_csv(r'C:\Users\Sachin kumar Sajjan.LAPTOP-Q9SO6CKL\Downloads\Diwali Sales Data.csv',encoding='unicode_escape')


# In[6]:


df.shape


# In[7]:


df.head()


# In[10]:


df.info()


# In[11]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[13]:


pd.isnull(df).sum()


# In[14]:


df.dropna(inplace=True)


# In[15]:


df.info()


# In[16]:


df['Amount']=df['Amount'].astype(int)


# In[17]:


df['Amount'].dtype


# In[18]:


df.describe()


# In[22]:


df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# In[24]:


sns.countplot(x='Gender',data=df)


# In[25]:


Genwise_Sales=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[26]:


sns.barplot(x='Gender',y='Amount',data=Genwise_Sales)


# From above graphs we can see that most of the buyers are females and even the purchasing power of females is greater than males

# # Age

# In[32]:


sns.countplot(x='Age Group',data=df,hue='Gender')


# From above graph we can say that most buyers are of age group between 26-35 females

# # Sate

# In[40]:


Statewise_Sales=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(7)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Amount',data=Statewise_Sales)


# From above graph we can say that most buyers are from state UttarPradesh, Maharashtra, Karnataka

# # Conclusion:

# Women age group from 26 to 35 yrs from states UttarPradesh, Maharashtra, Karnataka are more likely to buy products.

# In[ ]:




