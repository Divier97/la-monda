# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:47:16 2020

@author: JESUS
"""

import numpy as np
import pandas as pd
import pandas as pd

import seaborn as sb
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score 
datos=pd.read_csv('diabetes_csv.csv') 
cabecera=["#_veces_embarazad","concentra_glucosa_plasma","Presion_arterial_diastolica","Tríceps_pliegue_piel","insulina_sérica","Índice_masa_corporal","Función_pedigrí_diabetes","Edad","Clase"]
datos.columns = cabecera
print(datos.count())
f, ax = plt.subplots(figsize=(8, 8))
corr = datos.corr()
sb.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
           cmap=sb.diverging_palette(220, 10, as_cmap=True),
           square=True, ax=ax)

#signamos nuestra variable de entrada X para entrenamiento y las etiquetas Y.
dataX =datos[['Índice_masa_corporal']]
X_train = np.array(dataX)
y_train = datos['insulina_sérica'].values
 
# Creamos el objeto de Regresión Linear
regr = linear_model.LinearRegression()
 
# Entrenamos nuestro modelo
regr.fit(X_train, y_train)
 
# Hacemos las predicciones que en definitiva una línea (en este caso, al ser 2D)
y_pred = regr.predict(X_train)
 
# Veamos los coeficienetes obtenidos, En nuestro caso, serán la Tangente
print('pendiente <m> \n', regr.coef_)
# Este es el valor donde corta el eje Y (en X=0)
print('término independiente <b>: \n', regr.intercept_)
# Error Cuadrado Medio
print("Error Cuadrado Medio: %.2f" % mean_squared_error(y_train, y_pred))
# Puntaje de Varianza. El mejor puntaje es un 1.0
print('Varianza score: %.2f' % r2_score(y_train, y_pred))

#cosas=sb.lmplot('VALOR','CODIGO', datos, line_kws={'color':'red'})
y_Dl = regr.predict([[40]])
print(y_Dl)

print(datos['Edad'],datos['insulina_sérica'],datos['Índice_masa_corporal'])
