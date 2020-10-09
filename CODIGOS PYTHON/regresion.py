# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:47:11 2020

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
datos=pd.read_csv('BD_casas.csv') 
print(datos.count())
x=datos['sqft_living']
y=datos['price']
 
# Represento los datos generados
#plt.scatter(x, y)
#plt.show()
# Visualizamos rápidamente las caraterísticas de entrada
#datos.drop(['price','bedrooms','bathrooms','sqft_living'],1).hist()
#plt.show()


#signamos nuestra variable de entrada X para entrenamiento y las etiquetas Y.
dataX =datos[["sqft_living"]]
X_train = np.array(dataX)
y_train = datos['price'].values
 
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
print("Mean squared error: %.2f" % mean_squared_error(y_train, y_pred))
# Puntaje de Varianza. El mejor puntaje es un 1.0
print('Varianza score: %.2f' % r2_score(y_train, y_pred))

cosas=sb.lmplot('price','sqft_living', datos, line_kws={'color':'red'})


# Quiero predecir cuántos "Shares" voy a obtener por un artículo con 2.000 palabras,
# según nuestro modelo, hacemos:
y_Dl = regr.predict([[800]])
print(y_Dl)
