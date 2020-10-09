# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:32:48 2020

@author: JESUS
"""


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
datos=pd.read_csv('Delitos_Cibern_ticos.csv')

print(datos.count())
print(datos['ZONA'])
print (pd.value_counts(datos['ZONA']))

#pd.get_dummies(datos, columns = ["ZONA"])
#datos = pd.get_dummies(datos, columns = ["ZONA"], drop_first = True)
#cosa=sns.plot(datos['CLASE DE SITIO'].value_counts()[:10])
#cosas = datos.groupby('DELITO')['ZONA'].count().plot(kind='bar',legend='Reverse',figsize=(9,8))


#age_gro = pd.cut(datos['ZONA'], bins=["URBANA","RURAL","OTRAS"])
#print (pd.crosstab(age_gro, datos['DELITO']))
plo = pd.crosstab(age_gro, datos['DELITO']).plot(kind='bar', title='DELITO',figsize=(9,8))
dat=datos['CLASE DE SITIO'].value_counts()[:10]
#plot=pd.crosstab(index=datos['DELITO'], columns=dat).plot(kind='barh',stacked=True,legend='Reverse',figsize=(9,8))

#plot=pd.crosstab(index=datos['DIA'], columns=datos['HORA']).plot(kind='bar',stacked=True,legend='Reverse',figsize=(9,8))

#plot=pd.crosstab(index=datos['DEPARTAMENTO'], columns=datos['DELITO']).plot(kind='bar',stacked=True,legend='Reverse',figsize=(9,8))
lista=['VIAS PUBLICAS','CAJERO AUTOMATICO','CASAS DE HABITACION','OFICINAS','BANCOS','DENTRO DE LA VIVIENDA']
labels = datos['CLASE DE SITIO'].value_counts()[:6]
explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#D679DB','#E7F97B']
print (datos['CLASE DE SITIO'].value_counts()[:6])
dat=datos['CLASE DE SITIO'].value_counts()[:6]
#fig1, ax1 = plt.subplots()
#ax1.pie(dat,labels=lista,colors=colors,autopct='%1.1f%%',shadow = True)
#plt.title("SITIOS MAS COMUNES", bbox={"facecolor":"0.9", "pad":1})
#ax1.axis('equal')
#plt.tight_layout()
#plt.show()

print (datos['HORA'].value_counts()[:10])
deli=datos['DELITO'].value_counts()[:1]


#plot = datos['CLASE DE SITIO'].value_counts()[:6].plot(kind='bar',title='Pasajeros del Titanic')

#plot = pd.crosstab(datos['CLASE DE SITIO'].value_counts()[:6],columns=datos['DELITO']).plot(kind='bar')

