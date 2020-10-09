# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:05:22 2020

@author: JESUS
"""

import numpy as np
import pandas as pd
import pandas as pd
import statsmodels.api as sm
import seaborn as sb
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.model_selection import train_test_split
datos=pd.read_csv('diabetes_csv.csv') 
cabecera=["#_veces_embarazad","concentra_glucosa_plasma","Presion_arterial_diastolica","Tríceps_pliegue_piel","insulina_sérica","Índice_masa_corporal","Función_pedigrí_diabetes","Edad","Clase"]
datos.columns = cabecera
print(datos.count())
print(datos.keys())
# covarianza

grupo = datos[['#_veces_embarazad','concentra_glucosa_plasma','Presion_arterial_diastolica','Tríceps_pliegue_piel','insulina_sérica','Índice_masa_corporal','Función_pedigrí_diabetes','Edad']]
grupo = datos[['insulina_sérica','Índice_masa_corporal','Edad']]
covarianza=np.cov(np.array(grupo).T)
#covarianza = datos.cov()
print('Matriz de covarianza : \n',covarianza) # calcula matriz de covarianza

#correlacion de pearson
perarson=datos.corr(method='pearson')
print('correlacion de pearson : \n',perarson)

f, ax = plt.subplots(figsize=(8, 8))
corr = datos.corr()
sb.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
           cmap=sb.diverging_palette(220, 10, as_cmap=True),
           square=True, annot=True ,ax=ax)
# Para poder graficar en 3D, haremos una variable nueva que será la suma de los enlaces, comentarios e imágenes
suma = (datos["Edad"])
""" 
dataX2 =  pd.DataFrame()
dataX2["Índice_masa_corporal"] = datos["Índice_masa_corporal"]
dataX2["suma"] = suma
XY_train = np.array(dataX2)
z_train = datos['insulina_sérica'].values

X_train, X_test, y_train, y_test = train_test_split(XY_train, z_train , test_size=0.3, random_state=10)

#z_train, z_test, z_pred, z_p_test=train_test_split(XY_train,z_train,test_size=0.2)
regr2 = linear_model.LinearRegression()
 
# Entrenamos el modelo, esta vez, con 2 dimensiones
# obtendremos 2 coeficientes, para graficar un plano
regr2.fit(XY_train, z_train)


# Hacemos la predicción con la que tendremos puntos sobre el plano hallado
z_pred = regr2.predict(XY_train)
 
# Los coeficientes
print('Coefficients: \n', regr2.coef_)
# Error cuadrático medio
print("Error cuadrático medio: %.2f" % mean_squared_error(z_train, z_pred))
# Evaluamos el puntaje de varianza (siendo 1.0 el mejor posible)
print('Variance score: %.2f' % r2_score(z_train, z_pred))
#r cuadrado
#print ('Estadístico R_2: %.2f' % r2_score(z_train, z_train))
# calculamos el coeficiente de determinación R2
r2 = r2_score(z_train, z_pred)
print('Coeficiente de Determinación R2 = ' + str(r2))

fig = plt.figure()                   
ax = Axes3D(fig)
 
# Creamos una malla, sobre la cual graficaremos el plano
xx, yy = np.meshgrid(np.linspace(0, 3500, num=10), np.linspace(0, 60, num=10))
 
# calculamos los valores del plano para los puntos x e y
nuevoX = (regr2.coef_[0] * xx)
nuevoY = (regr2.coef_[1] * yy) 
 
# calculamos los correspondientes valores para z. Debemos sumar el punto de intercepción
z = (nuevoX + nuevoY + regr2.intercept_)
 
# Graficamos el plano
ax.plot_surface(xx, yy, z, alpha=0.2, cmap='viridis')
 
# Graficamos en azul los puntos en 3D
ax.scatter(XY_train[:, 0], XY_train[:, 1], z_train, c='cyan',s=30)
 
# Graficamos en rojo, los puntos que 
ax.scatter(XY_train[:, 0], XY_train[:, 1], z_pred, c='red',s=40)
 
# con esto situamos la "camara" con la que visualizamos
ax.view_init(elev=56., azim=65)
        
ax.set_xlabel('INDICE MASA CORPORAL')
ax.set_ylabel('EDAD')
ax.set_zlabel('INSULINA SERICA')
ax.set_title('Regresión Lineal con Múltiples Variables')                        
"""

z_Dosmil = regr2.predict([[70, 30]])
print(int(z_Dosmil))               


XY_train = sm.add_constant(XY_train)
model = sm.OLS(z_train, XY_train).fit() #Crea el modelo de regresión a partir del método de mínimos cuadrados ordinarios
print(model.summary() )#Muestra las estadísticas correspondientes al modelo

print(model.pvalues)

from seaborn import kdeplot

#Distribución de los Residuos
"""
residuos=z_train - z_pred
kdeplot(residuos)
"""