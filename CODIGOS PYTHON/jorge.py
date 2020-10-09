# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:18:25 2020

@author: JESUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs



# In[5]:


dataframe=pd.read_csv('german.csv')


# In[6]:


for i in dataframe.columns:
    if i=='Estado_cuenta_corriente':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Historial_credito':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Proposito':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Cuenta_ahorro_bonos':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Empleo_actual':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Estado_civil_sexo':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Otros_deudores':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Propiedad':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Planes_cuotas':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Vivienda':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Trabajo':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Telefono':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)
        
    elif i=='Extranjero':
        x=str(i)
        x2=str(i)
        x=pd.get_dummies(dataframe[x], drop_first=True)
        dataframe= pd.concat([dataframe,x], axis=1)
        dataframe.drop([x2], axis=1, inplace=True)


# In[7]:


dataframe




#sns.heatmap(dataframe)



# In[28]:


from sklearn.cluster import KMeans


# In[31]:



modelo= KMeans(n_clusters=5)


# In[32]:


print(modelo.fit(dataframe))


# In[33]:


print(modelo.cluster_centers_)


# In[34]:


Nc = range(1, 15)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score

plt.plot(Nc,score)
plt.xlabel('Numero de Clusters')
plt.ylabel(' errores')
plt.title()
plt.show()