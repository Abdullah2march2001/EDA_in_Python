#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('Diwali Sales Data.csv', encoding='latin-1')


# # Data Cleaning

# In[3]:


data.shape


# In[4]:


data.head()


# In[5]:


data.describe()


# In[6]:


data.info()


# In[7]:


data.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[8]:


data.head()


# In[9]:


pd.isnull(data)
#bec i remove it in excel file


# In[10]:


data['Amount'] =data['Amount'].astype(int)


# In[11]:


data.info()


# In[12]:


data.columns 


# In[13]:


data.rename(columns={'Marital_Status':'Married_or_Unmarried'})


# # EDA 

# In[14]:


ax=sns.countplot(x='Gender',data=data)
for bars in ax.containers:
    ax.bar_label(bars)
    plt.title('Count of Gender')


# In[15]:


sales_by_gen = data.groupby('Gender', as_index=False)['Amount'].sum().sort_values(by = 'Amount',ascending=False)
sales_by_gen
sns.barplot(x='Gender',y='Amount', data=sales_by_gen)
plt.title('Sales by Gender')
plt.show()


# We can see that Female purchase more than Male on Dewali 

# In[16]:


data.columns


# In[17]:


ax=sns.countplot(data=data,x='Age Group',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
    plt.title('Age Group and Gender')


# In[18]:


sales_by_age= data.groupby('Age Group', as_index=False )['Amount'].sum().sort_values(by = 'Amount',ascending=False)
sales_by_gen
sns.barplot(x='Age Group',y='Amount', data=sales_by_age)
plt.title('Sales by Age Group')
plt.show()


# In[30]:


#creating a visualization 
sales_by_states = data.groupby('State', as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

#figure Size
sns.set(rc={'figure.figsize': (15, 6)})

#Labels of x-axis and y-axis
sns.barplot(x='State', y='Orders', data=sales_by_states)

#title
plt.title('Sales by States')
plt.show()


# In[31]:


#creating a visualization 
sales_by_amount = data.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

#figure Size
sns.set(rc={'figure.figsize': (15, 6)})

#Labels of x-axis and y-axis
sns.barplot(x='State', y='Amount', data=sales_by_amount)

#title
plt.title('Sales by Amount')
plt.show()


# In[33]:


data.columns


# In[39]:


ax=sns.countplot(x='Marital_Status',data=data)

for bars in ax.containers:
    ax.bar_label(bars)
    plt.title('Count of Marital Status')

sns.set(rc={'figure.figsize': (6, 6)})


# In[40]:


data.columns


# In[42]:


ax=sns.countplot(data=data,x='Marital_Status',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
    plt.title('Marital Status and Gender')


# In[51]:


sns.set(rc={'figure.figsize' : (20, 5)}) 
ax = sns.countplot(data = data, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[52]:


#creating a visualization 
sales_by_amount = data.groupby('Occupation', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

#figure Size
sns.set(rc={'figure.figsize': (15, 6)})

#Labels of x-axis and y-axis
sns.barplot(x='Occupation', y='Amount', data=sales_by_amount)

#title
plt.title('Sales by Occupation')
plt.show()


# In[57]:


sns.set(rc={'figure.figsize':(24,5)})
ax = sns.countplot(data = data, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Product Category ')


# In[60]:


sales_state = data.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')
plt.title('Amount Spend on Product Category ')


# In[64]:


data.columns


# In[67]:


sales_state = data.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(24,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
plt.title('Product ID ')


# In[69]:


fig1, ax1 = plt.subplots(figsize=(12,7))
data.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.title('Top 10 Most Sold Products')


# Conclusion:
# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
# 
# Thank you!

# In[ ]:




