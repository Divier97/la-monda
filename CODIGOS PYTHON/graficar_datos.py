# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:15:27 2020

@author: JESUS
"""
#separado por espacios en blancos
#datos=pd.read_csv('train.csv',header=0, delim_whitespace=True)
import pandas as pd
import numpy as np
from scipy.interpolate import interpld
from matplotlib import pyplot as plt
datos=pd.read_csv('train.csv',header=0)
x=datos.ix[:,0]
y=datos.ix[:,8]
print (datos)
print (x)
print (y)
plt.plot(x,y,'ro')
plt.ylabel('tarifa')
plt.xlabel('edad')
plt.show
#ajuste de datosa un polinomio de primer grado
coeficientes=np.polyfit(x,y,1)
polinomio=np.poly1d(coeficientes) 
print (polinomio)
f=interpld(x,y,1)
print (f(330))
ys=polinomio(x)
plt.plot(x,ys,'g^')