# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:31:04 2020

@author: JESUS
"""

import pandas as pd
from matplotlib import pyplot as plt
datos=pd.read_csv('adult.csv')

print(datos)

#contar cuantos valores nulos hay en cada una de las columnas
col_names =datos.columns.tolist()

for column in col_names:
    print("valores nulos en <{0}>: {1}".format(column, datos[column].isnull().sum()))
    

print (datos.describe(include="all"))

#pandas Números de agrupación
age_groups = pd.cut(datos['edad'], bins=[19, 40, 65, 90])

print (pd.crosstab(age_groups, datos[' clase de trabajo']))


#agrupacion por calses y cuentas instancia tiene cada una 
print (pd.value_counts(datos[' clase de trabajo']))

print (datos[' educacion'].value_counts())

datos.boxplot(figsize=(9,9))
plt.show()