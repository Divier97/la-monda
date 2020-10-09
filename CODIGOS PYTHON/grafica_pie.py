# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:07:12 2020

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


from pylab import *
y = datos['CLASE DE SITIO'].value_counts()[:10]
pie(y)
xlabel('mi grafico')
title('titulo de mi grafico')
legend( (datos['CLASE DE SITIO'],), loc = 'upper left')
draw()
#savefig("mi-grafico1",dpi=300)
#close()
grid(True)
show()