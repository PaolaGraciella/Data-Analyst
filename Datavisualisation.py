#!/usr/bin/env python
# coding: utf-8

# In[1]:



import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Sales analyst

# In[2]:


pip install pandas


# In[3]:


import pandas as pd


# # Importer les fichiers datas

# In[8]:



files = [file for file in os.listdir(r'C:\Users\DELL\Downloads\Sales_Data\Sales_Data')]
for file in files :
    print(file)


# In[9]:


path = r'C:\Users\DELL\Downloads\Sales_Data\Sales_Data'

#Créer une base de données vide 
all_data = pd.DataFrame()

for file in files :
    current_data = pd.read_csv(path+'/'+file)
    all_data = pd.concat([all_data, current_data])
print(all_data)


# In[13]:


janvier = pd.read_csv(path+'/Sales_January_2019.csv')
janvier.shape


# In[15]:


all_data.to_csv(path+'/all_data.csv', index = False)


# In[16]:


all_data.dtypes


# In[17]:


all_data.head()


# In[18]:


all_data.isnull().sum()


# In[20]:


#Supprimer les champs vides
all_data = all_data.dropna(how = 'all')
all_data.shape


# In[21]:


#Le mois du meilleur chiffre d'affaire 
def month(x):
    return x.split('/')[0]


# In[23]:


all_data['Month'] = all_data['Order Date'].apply(month)
all_data


# In[25]:


all_data = all_data[all_data['Month']!= 'Order Date']
all_data['Month'].unique()


# In[27]:


all_data['Month'] = all_data['Month'].astype(int)
all_data.dtypes


# In[29]:


all_data['Price Each'] = all_data['Price Each'].astype(float)
all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype(int)
all_data.dtypes


# In[30]:


all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
all_data


# In[31]:


all_data.groupby('Month')['Sales'].sum()


# In[34]:


import matplotlib.pyplot as plt
months = range(1,13)
plt.bar(months,all.groupby('Month')['Sales'].sum())
plt.xticks(Months)
plt.ylabel('Sales')
plt.ylabel('Months')
plt.show()


# In[35]:


pip install matplotlib


# In[39]:


import matplotlib.pyplot as plt
months = range(1,13)
plt.bar(months,all_data.groupby('Month')['Sales'].sum())
plt.xticks(months)
plt.ylabel('Sales')
plt.ylabel('Months')
plt.show()


# In[40]:



all_data


# # La ville ou on a enregister un maximum de commandes

# In[41]:


'917 1st St, Dallas, TX 75001'.split(',')[1]


# In[42]:


def city(x):
    return x.split(',')[1]


# In[44]:


all_data['city'] = all_data['Purchase Address'].apply(city)
all_data


# In[51]:


plt.bar(all_data.groupby('city')['city'].count().index,all_data.groupby('city')['City'].count().index.all_data.groupby('Month')['Sales'].sum())
plt.xticks(rotation = 'verticial')
plt.ylabel('Received orders')
plt.ylabel('City Name')
plt.show()


# In[52]:


plt.bar(all_data.groupby('city')['city'].count().index,all_data.groupby('Month')['Sales'].sum())
plt.xticks(rotation = 'verticial')
plt.ylabel('Received orders')
plt.ylabel('City Name')
plt.show()


# In[55]:


all_data.groupby('city')['city'].count().values


# In[60]:


plt.bar(all_data.groupby('city')['city'].count().index,all_data.groupby('city')['city'].count())
plt.xticks(rotation = 'vertical')
plt.ylabel('Received orders')
plt.xlabel('City Name')
plt.show()


# # A quel heure et jour doit-on faire une campagne Pour avoir le plus de vente

# In[62]:



all_data['Hour'] = pd . to_datetime(all_data['Order Date']).dt.hour
all_data


# In[64]:


keys = []
hours = []
for key, hour in all_data.groupby('Hour'):
    keys.append(key)
    hours.append(len(hour))
hours


# In[65]:


plt.grid()
plt.plot(keys,hours)
plt.xlabel('Heure')
plt.ylabel('Nombre de commande')


# # Le produit qui réalise le plus de vente 
# 

# In[74]:


all_data.groupby('Product')['Quantity Ordered'].sum().plot(kind = 'bar')


# # Examiner l'impact du prix sur les ventes
# all_data.groupby('Product')['Price Each'].mean()

# In[69]:


#Relation entre la quantité vendue et le prix du produit
products = all_data.groupby('Product')['Quantity Ordered'].sum().index
quantity = all_data.groupby('Product')['Quantity Ordered'].sum()
prices = all_data.groupby('Product')['Price Each'].mean()


# In[73]:


plt.figure(figsize = (40,24))
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(products, quantity, color = 'g')
ax2.plot(products,prices, 'b-')
ax1.set_xticklabels(products, rotation='vertical', size = 8)


# # La combinaison des produits qui sont les plus vendus
# 

# In[76]:


df = all_data[all_data['Order ID'].duplicated(keep = False)]


# In[79]:


df['Grouped']  = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df['Grouped']


# In[83]:


df.drop_duplicates(subset = ['Order ID'])
df


# 

# In[85]:


df['Grouped'].value_counts()[0:5].plot.pie()


# In[ ]:




