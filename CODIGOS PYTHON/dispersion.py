# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:09:48 2020

@author: JESUS
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



datos=pd.read_csv('adult.csv')


plt.scatter(x=datos[' horas por semana'], y=datos[' estado civil'])
plt.show()

# Dibuja los puntos en el marco
#surveys_plot + p.geom_point()

series = pd.Series(datos['edad'])
print (series.quantile([0,0.25,0.5,0.75,1]))
df= pd.DataFrame(datos['edad'])
gra=df.boxplot()

#cosas = datos.groupby('Proposito')['Monto_credito'].sum().plot(kind='bar',legend='Reverse',figsize=(9,8))


