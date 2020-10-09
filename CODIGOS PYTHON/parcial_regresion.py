# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:14:25 2020

@author: JESUS
"""

import numpy as np
import pandas as pd
import pandas as pd
import seaborn as sb
import statsmodels.api as sm
import pylab
from seaborn import kdeplot
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
 
datos=pd.read_csv('iris.csv') 
#print(datos.cov())
print(datos.dtypes)


x=datos['petal.length']
y=datos['sepal.length']


_,idlx = np.unique(datos['variety'],return_inverse=True)
datos['variety'] = idlx
#print(datos.cov())

#
#Calcular el Coeficiente de Correlación, Covarianzas de las variables.

#print(datos.corr())
"""
f, ax = plt.subplots(figsize=(8, 8))
corr = datos.corr()
sb.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
           cmap=sb.diverging_palette(220, 10, as_cmap=True),
           square=True, annot=True ,ax=ax)
"""
#----------------------------


#Graficar relación entre la longitud del pétalo y la longitud del sépalo
#con las Especies o Grupos

#sb.pairplot(datos.dropna(), hue='variety',size=4,vars=['petal.length','sepal.length'],kind='scatter')

##---------------------------------------------



#signamos nuestra variable de entrada X para entrenamiento y las etiquetas Y.
dataX =datos[["sepal.length"]]
X_train = np.array(dataX)
y_train = datos['petal.length'].values
 
# Creamos el objeto de Regresión Linear
regr = linear_model.LinearRegression()
 
# Entrenamos nuestro modelo
regr.fit(X_train, y_train)
 
# Hacemos las predicciones que en definitiva una línea (en este caso, al ser 2D)
y_pred = regr.predict(X_train)
 
# Veamos los coeficienetes obtenidos, En nuestro caso, serán la Tangente
print('Coeficiente  \n', regr.coef_)
# Este es el valor donde corta el eje Y (en X=0)
print('término independiente <b>: \n', regr.intercept_)
# Error Cuadrado Medio
print("Error Cuadrado Medior: %.2f" % mean_squared_error(y_train, y_pred))
# Puntaje de Varianza. El mejor puntaje es un 1.0
print('Varianza score: %.2f' % r2_score(y_train, y_pred))

#ecuacion lineal
print("La ecuacion del modelo es igual a ->  ",'y =',regr.coef_, 'x',regr.intercept_ )

#cosas=sb.lmplot('sepal.length','petal.length', datos, line_kws={'color':'red'})
"""
x=datos['sepal.length']
y=datos['petal.length']
plt.scatter(x,y,color='blue')
plt.plot(x,y_pred,color='red', linewidth=3)
plt.title("regresion lineal")
plt.xlabel("longitud del sépalo")
plt.ylabel("longitud del pétalo")
plt.show()
"""

#Distribución de los Residuos
residuos=y_train - y_pred
#histograma de residuos
#plt.hist( residuos,color='blue')
#plt.show()
#-----------------------------------
#gráfico Q-Q
sm.qqplot(residuos, line='45')
pylab.show()
#----------------------------
"""
#Asociación lineal entre las Variables:
x=datos['petal.length']
plt.scatter(x,residuos,color='blue')
plt.axhline(y=0, xmin=0, xmax=8)
plt.title("regresion lineal")
plt.xlabel("longitud del sépalo")
plt.ylabel("residuos")
plt.show()
"""

#fig, ax = plt.subplots()
#ax.scatter(y_pred,y_train)
#plt.show()
# Quiero predecir cuántos "Shares" voy a obtener por un artículo con 2.000 palabras,
# según nuestro modelo, hacemos:
y_Dl = regr.predict([[4.4]])
print('Prediccion: %.2f '% y_Dl)


X = np.array(datos[["sepal.length","sepal.width","petal.length",'petal.width']])
Y = np.array(datos['variety'])
X.shape
"""

colores=['blue','red','green']
asignar=[]
for row in Y:
    asignar.append(colores[row])
    
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2],X[:,3], c=asignar,s=60)

"""

