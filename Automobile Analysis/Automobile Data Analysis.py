#!/usr/bin/env python
# coding: utf-8

# # Libraries 

# In[84]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Import Data From Computer

# In[85]:


data = pd.read_csv(r'C:\Users\user\OneDrive\Desktop\Portfolio Projects\EDA\Automobile Analysis\autos_new1.csv')


# In[86]:


data.head()


# In[87]:


data.describe()


# In[88]:


data.shape


# # Data Wrangling 

# In[89]:


#Removing Duplicates in Dataset
data_no_duplicates = data.drop_duplicates()


# In[90]:


#Drop First Coloumn 
if 'Unnamed: 0' in data.columns:
    data = data.drop('Unnamed: 0', axis=1)


# In[91]:


# Replace '?' with NaN in the 'normalized-losses' column
data['normalized-losses'] = data['normalized-losses'].replace('?', float('nan'))

# Convert the column to numeric (if it's not already)
data['normalized-losses'] = pd.to_numeric(data['normalized-losses'], errors='coerce')

# Calculate the mean of the column, excluding NaN values
mean_loss = data['normalized-losses'].mean()

# Replace NaN values with the mean
data['normalized-losses'].fillna(mean_loss, inplace=True)


# In[92]:


data.head()


# In[93]:


#Finding Frequency of Num Of Doors Coloumn
frequency = data['num-of-doors'].value_counts()

# Replace '?' with NaN in the 'num-of-doors' column
data['num-of-doors'] = data['num-of-doors'].replace('?', np.nan)

# Replace NaN values with the mean
data['normalized-losses'].fillna(frequency, inplace=True)

data.head()
data.shape


# In[94]:


# Replace '?' with NaN in the 'bore' column
data['bore'] = data['bore'].replace('?', float('nan'))

# Convert the column to numeric (if it's not already)
data['bore'] = pd.to_numeric(data['bore'], errors='coerce')

# Calculate the mean of the column, excluding NaN values
mean_loss = data['bore'].mean()

# Replace NaN values with the mean
data['bore'].fillna(mean_loss, inplace=True)


# In[95]:


data.head()


# In[96]:


# Replace '?' with NaN in the 'stroke' column
data['stroke'] = data['stroke'].replace('?', float('nan'))

# Convert the column to numeric (if it's not already)
data['stroke'] = pd.to_numeric(data['stroke'], errors='coerce')

# Calculate the mean of the column, excluding NaN values
mean_loss = data['stroke'].mean()

# Replace NaN values with the mean
data['stroke'].fillna(mean_loss, inplace=True)


# In[97]:


# Replace '?' with NaN in the 'horsepower' column
data['horsepower'] = data['horsepower'].replace('?', float('nan'))

# Convert the column to numeric (if it's not already)
data['horsepower'] = pd.to_numeric(data['horsepower'], errors='coerce')

# Calculate the mean of the column, excluding NaN values
mean_loss = data['horsepower'].mean()

# Replace NaN values with the mean
data['horsepower'].fillna(mean_loss, inplace=True)


# In[98]:


# Replace '?' with NaN in the 'peak-rpm' column
data['peak-rpm'] = data['peak-rpm'].replace('?', float('nan'))

# Convert the column to numeric (if it's not already)
data['peak-rpm'] = pd.to_numeric(data['peak-rpm'], errors='coerce')

# Calculate the mean of the column, excluding NaN values
mean_loss = data['peak-rpm'].mean()

# Replace NaN values with the mean
data['peak-rpm'].fillna(mean_loss, inplace=True)


# In[99]:


# Replace '?' with NaN in the 'price' column
data['price'] = data['price'].replace('?', float('nan'))

# Convert the column to numeric (if it's not already)
data['price'] = pd.to_numeric(data['price'], errors='coerce')

# Calculate the mean of the column, excluding NaN values
mean_loss = data['price'].mean()

# Replace NaN values with the mean
data['price'].fillna(mean_loss, inplace=True)


# # Data Visualization

# In[100]:


data = pd.DataFrame(data)

# Create a count plot for the 'drive-wheels' column
plt.figure(figsize=(8, 6))  # Optional: Adjust the figure size
sns.countplot(data=data, x='drive-wheels')

# Add labels and title
plt.xlabel('Drive Wheels')
plt.xlabel('Drive Wheels')
plt.ylabel('Frequency')
plt.title('Count of Vehicles by Drive Wheels')

# Show the plot
plt.xticks(rotation=45)  # Optional: Rotate x-axis labels for better readability
plt.show()


# In[101]:


data = pd.DataFrame(data)

# Create a count plot for the 'Make' column
plt.figure(figsize=(11, 5))  # Optional: Adjust the figure size
sns.countplot(data=data, x='make')

# Add labels and title
plt.xlabel('Make')
plt.ylabel('Frequency')
plt.title('Count of Vehicles Vehicles')

# Show the plot
plt.xticks(rotation=45)  # Optional: Rotate x-axis labels for better readability
plt.show()


# In[102]:


correlation = data['engine-size'].corr(data['horsepower'])
print(f"Correlation between engine-size and horsepower: {correlation}")

# Plot 'horsepower' on the x-axis and 'engine-size' on the y-axis
plt.figure(figsize=(8, 6))
sns.regplot(x='horsepower', y='engine-size', data=data, scatter_kws={"alpha":0.5})

# Add labels and title
plt.xlabel('Horsepower')
plt.ylabel('Engine Size')
plt.title('Scatter Plot with Linear Regression Line: Horsepower vs Engine Size')

# Show the plot
plt.grid(True)  # Optional: Add grid lines
plt.show()


# In[103]:


# Assuming you have your dataset loaded into a DataFrame called 'df'
# Select the numerical columns you want to analyze
numerical_columns = ['normalized-losses', 'wheel-base', 'length', 'width', 'height',
                     'curb-weight', 'engine-size', 'bore', 'stroke', 'compression-ratio',
                     'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

# Calculate the correlation matrix
correlation_matrix = data[numerical_columns].corr()

# Create a heatmap to visualize the correlations
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Add title
plt.title("Correlation Heatmap")

# Show the plot
plt.show()


# In[104]:


correlation = data['city-mpg'].corr(data['price'])
print(f"Correlation between city-mpg and price: {correlation}")

# Plot 'horsepower' on the x-axis and 'engine-size' on the y-axis
plt.figure(figsize=(8, 6))
sns.regplot(x='price', y='city-mpg', data=data, scatter_kws={"alpha":0.5})

# Add labels and title
plt.xlabel('price')
plt.ylabel('city-mpg')
plt.title('Scatter Plot with Linear Regression Line: price vs city-mpg')

# Show the plot
plt.grid(True)  # Optional: Add grid lines
plt.show()


# In[105]:


# Box plot: Price by Make
plt.figure(figsize=(12, 6))
sns.boxplot(x='make', y='price', data=data)
plt.xticks(rotation=90)
plt.title('Price by Make')
plt.xlabel('Make')
plt.ylabel('Price')
plt.show()


# In[106]:


# Bar chart: Fuel Type distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='fuel-type', data=data)
plt.title('Fuel Type Distribution')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()



# In[107]:


# Histogram: Car Length Distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['length'], bins=20, kde=True)
plt.title('Car Length Distribution')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()


# In[108]:


# Scatter plot: City MPG vs. Highway MPG
plt.figure(figsize=(8, 6))
sns.scatterplot(x='city-mpg', y='highway-mpg', data=data)
plt.title('City MPG vs. Highway MPG')
plt.xlabel('City MPG')
plt.ylabel('Highway MPG')
plt.show()


# In[109]:


# Box plot: Engine Type vs. Price
plt.figure(figsize=(10, 6))
sns.boxplot(x='engine-type', y='price', data=data)
plt.xticks(rotation=45)
plt.title('Engine Type vs. Price')
plt.xlabel('Engine Type')
plt.ylabel('Price')
plt.show()


# In[110]:


# Box plot: Number of Cylinders vs. Price
plt.figure(figsize=(10, 6))
sns.boxplot(x='num-of-cylinders', y='price', data=data)
plt.title('Number of Cylinders vs. Price')
plt.xlabel('Number of Cylinders')
plt.ylabel('Price')
plt.show()


# In[111]:


# Bar chart: Engine Type vs. City MPG
plt.figure(figsize=(8, 6))
sns.barplot(x='engine-type', y='city-mpg', data=data)
plt.title('Engine Type vs. City MPG')
plt.xlabel('Engine Type')
plt.ylabel('City MPG')
plt.show()


# In[112]:


# Bar chart: Number of Cylinders vs. Highway MPG
plt.figure(figsize=(8, 6))
sns.barplot(x='num-of-cylinders', y='highway-mpg', data=data)
plt.title('Number of Cylinders vs. Highway MPG')
plt.xlabel('Number of Cylinders')
plt.ylabel('Highway MPG')
plt.show()


# In[113]:


# Scatter plot: Symboling vs. Price
plt.figure(figsize=(8, 6))
sns.scatterplot(x='symboling', y='price', data=data)
plt.title('Symboling vs. Price')
plt.xlabel('Symboling')
plt.ylabel('Price')
plt.show()


# In[114]:


# Scatter plot: Engine Size vs. Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='engine-size', y='price', data=data)
plt.title('Engine Size vs. Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.show()


# In[115]:


# Scatter plot: Engine Size vs. City MPG
plt.figure(figsize=(10, 6))
sns.scatterplot(x='engine-size', y='city-mpg', data=data)
plt.title('Engine Size vs. City MPG')
plt.xlabel('Engine Size')
plt.ylabel('City MPG')
plt.show()


# In[116]:


# Scatter plot: Horsepower vs. Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='horsepower', y='price', data=data)
plt.title('Horsepower vs. Price')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.show()


# In[117]:


# Scatter plot: Horsepower vs. City MPG
plt.figure(figsize=(10, 6))
sns.scatterplot(x='horsepower', y='city-mpg', data=data)
plt.title('Horsepower vs. City MPG')
plt.xlabel('Horsepower')
plt.ylabel('City MPG')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




