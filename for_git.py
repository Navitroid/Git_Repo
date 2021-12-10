#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import scipy.stats as ss
import seaborn as sns
import matplotlib as plt
import numpy as np

df = pd.read_csv('//home/jupyter-i.netreba-11/Mat_stat/conversion.csv')


# In[ ]:


# знакомимся с данными


# In[2]:


df.shape


# In[5]:


df.head()


# In[3]:


#проверяем количество пропущенных значений


# In[4]:


df.isna().sum()


# In[ ]:





# In[ ]:


# считаем кликабельность (CTR) и добавлем в новую колонку


# In[8]:


df['CTR'] = df.Clicks / df.Impressions


# In[ ]:


# находим строку с максимальным значением CTR в данных


# In[9]:


df['CTR'].idxmax()


# In[10]:


df.iloc[150]


# In[ ]:





# In[ ]:


# считаем и добавляем новую метрику затрат на клик CPC


# In[13]:


df['CPC'] = df.Spent / df.Clicks


# In[ ]:





# In[ ]:


# смотрим распределение CPC с группировкой по полу пользователя


# In[23]:


sns.distplot(df.query("gender=='M'").CPC.dropna(), kde=False, bins = 20)
sns.distplot(df.query("gender=='F'").CPC.dropna(), kde=False, bins = 20)


# In[ ]:


# считаем и добавлем метрику CR


# In[15]:


df['CR'] = ((df.Approved_Conversion / df.Clicks) * 100).round(2)


# In[25]:


df


# In[ ]:




