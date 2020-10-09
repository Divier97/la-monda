# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:56:56 2020

@author: JESUS
"""

import pandas as pd
from matplotlib import pyplot as plt
datos=pd.read_excel('Datos.xlsx',header=0)
print (datos)
x=datos.ix[:,0] #mostrar datos solamente de les esta columna
y=datos.ix[:,7] #mostrar datos solamente de les esta columna
print (datos)
print (x)
print (y)
plt.plot(x,y,'ro')
plt.ylabel('MORTALIDAD')
plt.xlabel('PAIS')
plt.show
datos.describe(include = "all")
print (y.describe())
type(datos)

datos.hist(column='Mortalidad_Infantil', bins=10)
plt.show()



