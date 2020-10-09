# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 00:39:34 2020

@author: JESUS
"""

import pandas as pd
from matplotlib import pyplot as plt
datos=pd.read_excel('Datos.xlsx',header=0)
print (datos)
#print (datos.describe())
#print (datos.dtypes)
#datos['Porcenteje_Plo'].hist(bins=10) 
#plt.xlabel("Duración en minutos")
#plt.ylabel("Frecuencia")
#plt.show()

#contar cuantos valores nulos hay en cada una de las columnas
col_names =datos.columns.tolist()

for column in col_names:
    print("valores nulos en <{0}>: {1}".format(column, datos[column].isnull().sum()))

#remplazar valores por otros
print (datos['Grupo '])

#para cuando la fecha este combinada con la hora ->> variable (DateAndTime)
#dataOfStatusTimings['Date']=[d.date() for d in dataOfStatusTimings['DateAndTime']]
#dataOfStatusTimings['Time']=[d.time() for d in dataOfStatusTimings['DateAndTime']]



datos = pd.get_dummies(datos, colmns =["Sexo"], drop_first = True)