# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:47:11 2020

@author: JESUS
"""

import pandas as pd
from matplotlib import pyplot as plt
datos=pd.read_csv('adult.csv')


#plot = datos[' clase de trabajo'].value_counts().plot(kind='bar',title='Clases de trabajos')


age_groups = pd.cut(datos[' horas por semana'], bins=[10, 20, 35, 50, 80])

print (pd.crosstab(age_groups, datos[' estado civil']))

print (datos[' estado civil'].value_counts())


#plot = pd.crosstab(age_groups, datos[' clase de trabajo']).plot(kind='bar',title='CLASES DE TRABAJO',figsize=(8,8))

print (datos[' ocupacion'])
print (datos[' fnlwgt'])

age_gro = pd.cut(datos[' ganancia de capital'], bins=[0, 1000, 2500, 5000, 15000, 20000, 30000])
print (pd.crosstab(age_gro, datos[' ocupacion']))
plo = pd.crosstab(age_gro, datos[' ocupacion']).plot(kind='bar', title='OCUPACION',figsize=(9,8))

print (datos[' educacion'])
#cosas = datos.groupby(' ocupacion')[' ganancia de capital'].sum().plot(kind='bar',legend='Reverse',figsize=(9,8))



