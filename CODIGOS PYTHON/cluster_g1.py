# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:49:28 2020

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
datos=pd.read_csv('german.csv')

_,idx = np.unique(datos['Trabajo'],return_inverse=True)
datos['Trabajo'] = idx
print(datos['Trabajo'])

_,idlx = np.unique(datos['Proposito'],return_inverse=True)
datos['Proposito'] = idlx
print(datos['Proposito'])

"""
print(pd.get_dummies(datos["Proposito"]))
propo = pd.get_dummies(datos["Proposito"], drop_first = True)
print(propo)"""
print(datos.count())
#como se comportan los datos 
#sb.pairplot(datos.dropna(), hue='Proposito','Proposito','Planes_cuotas,size=4,vars=["Monto_credito","Edad","Duracion_mes"],kind='scatter')

X = np.array(datos[["Monto_credito","Edad","Duracion_mes"]])
y = np.array(datos[['Trabajo','Proposito','Planes_cuotas']])
X.shape
"""
#graficamos los datos en 3D
fig = plt.figure()
ax = Axes3D(fig)
colores=['blue','red','green','blue','cyan','yellow','orange','black','pink','brown','purple']
asignar=[]
for row in y:
    asignar.append(colores[row])
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)"""

#obtenemos el vaor de K
Nc = range(1, 15)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score

plt.plot(Nc,score)
plt.xlabel('Numero de Clusters')
plt.ylabel('Suma de los errores cuadraticos')
plt.title('Curva de codo')
plt.show()


kmeans = KMeans(n_clusters=3).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)
#colores=['red','green','blue','cyan','yellow','fuchsia']
#Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
colores=['cyan','green','red','cyan']
asignar=[]
for row in labels:
    asignar.append(colores[row])
""" 
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000)
"""
# Getting the values and plotting it
f1 = datos['Monto_credito'].values
f2 = datos['Edad'].values

#plt.scatter(f1, f2, c=asignar, s=70)
#plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
#plt.show()