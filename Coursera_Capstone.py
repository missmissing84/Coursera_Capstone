#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[18]:


import numpy as np


# In[19]:


print('Hello Capstone Project Course!')


# # Data from Wikipedia, clean and display.
# 

# In[20]:



liste = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
df = pd.DataFrame(liste[0]) #Getting the table only


# In[21]:


df


# In[22]:


import re
new_df = pd.DataFrame()
dict_list = []
# Let's browse the table to make the required dataframe.
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        string = df.loc[i,j]
        postal_code = string[:3]
        if string[3:] != 'Not assigned': #Ignoring the non assigned postal codesd
            try:
                borough = string[3:].split('(')[0]
                found = string[3:].split('(')[1]
                found = found[found.find("(")+1:found.find(")")]
                neighborhood = found.replace('/',',')
                neighborhood = neighborhood.split(',')[0]
                borough = borough.replace('/',',')
                dictio = {'Postal code': postal_code, 'Borough':borough, 'Neighborhood': neighborhood}
                dict_list.append(dictio)
            except:
                print("No neighborhood " + str(string[3:]))
                borough = string[3:].replace('/',',')
                neighborhood = borough
                neighborhood = neighborhood.split(',')[0]
                dictio = {'Postal code': postal_code, 'Borough':borough, 'Neighborhood': neighborhood}
                dict_list.append(dictio)
new_df = pd.DataFrame.from_dict(dict_list)


# In[23]:


new_df


# In[24]:


new_df.shape


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




