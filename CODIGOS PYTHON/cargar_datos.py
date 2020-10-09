# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:47:58 2020

@author: JESUS
"""

import pandas as pd
datos=pd.read_csv('train.csv',header=0)
#print (datos)
#print (datos.ix[0:3])
#print (datos.sort_values(by='Sex',ascending=False))
#print (datos[datos.ix[:,5]<18])
#sex=datos['Sex']
#print (sex[sex=='female'])

#cabecera=["ID","Sobrevivientes","Clase","Nombre","Sexo","Edad","Hermanos","Hijos","Ticket","Tarifa","Cabina","Embarked"]
#datos.columns = cabecera
#print (datos)

#informacion de los datos estadisticos como desviacion, frecuencia
#analisis estadisticos
print (datos.describe())
print (datos.describe(include="all"))