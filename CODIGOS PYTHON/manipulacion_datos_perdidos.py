# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 23:56:12 2020

@author: JESUS
"""

import pandas as pd
datos=pd.read_csv('train.csv',header=0)
cabecera=["ID","Sobrevivientes","Clase","Nombre","Sexo","Edad","Hermanos","Hijos","Ticket","Tarifa","Cabina","Embarked"]
datos.columns = cabecera

#axis=0 para eliminar filas
#axis=1 para eliminar columnas
#datos faltantes
#datos.dropna(axis =0)

#eliminar filas donde haya datos perdidos pero seleccionando una columna
#datos.dropna(subset = ["cabina"],axis =0)
#-----------------------------



#promedio de edad
print (datos["Edad"].mean())


#para remplazar datos faltantes 
#replace(data a remplazar, nuevo dato)
#promedio = 30
#datos["Edad"].replace(np.nan, promedio)



#####################################################
#cambiar datos de las culumnas por otros


d = {'male' : 'M', 'female': 'F'}

datos['Sexo'] = datos['Sexo'].apply(lambda x:d[x])
datos['Sexo'].head()

print (datos['Sexo'])


#pandas Números de agrupación
age_groups = pd.cut(datos['Edad'], bins=[19, 40, 65, 90])
#Úsalo en groupby para obtener el número medio
print (datos.groupby(age_groups)['Sobrevivientes'].mean())

#Tablas cruzadas por grupos de edad y género:
print (pd.crosstab(age_groups, datos['Sexo']))
print (pd.crosstab(age_groups, datos['Clase']))