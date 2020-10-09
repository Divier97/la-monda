# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:14:17 2020

@author: JESUS
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn import preprocessing 
from sklearn.metrics import pairwise_distances_argmin_min
 
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
datos=pd.read_csv('iris.csv')



_,idlx = np.unique(datos['variety'],return_inverse=True)
datos['variety'] = idlx
print(datos)

X = np.array(datos[["sepal.length","sepal.width","petal.length",'petal.width']])
y = np.array(datos[['variety']])
X.shape




Nc = range(1, 18)
kmeans = [KMeans(n_clusters=i) for i in Nc]
error = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]

""""
plt.plot(Nc,error)
plt.xlabel('Numero de Clusters')
plt.ylabel('Suma de los errores cuadraticos')
plt.title('Curva de codo')
plt.show()
"""

kmeans = KMeans(n_clusters=3).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)

#print(datos.summary() )#Muestra las estadísticas correspondientes al modelo

#colores=['cyan','green','blue','fuchsia','yellow','red','black','reset']
#Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
colores=['green','red','black']
asignar=[]
for row in labels:
    asignar.append(colores[row])
 
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2],X[:, 3], c=asignar,s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='8', c=colores, s=1000)
