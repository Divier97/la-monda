# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:50:37 2020

@author: JESUS
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
datos=pd.read_csv('german.csv')

print(datos.count())



#datos.boxplot(figsize=(20,20))


#print(datos['Proposito'].describe())
#1
#cosas = datos.groupby('Proposito')['Monto_credito'].mean().plot(kind='bar',legend='Reverse',figsize=(6,6))
#2estatus de las personas que hacen mas prestamos

#cosa=sns.barplot(x='Estado_civil_sexo',y='Monto_credito', data=datos)

#perfil de los perfiles que hacen menos prestamos 
#cosa=sns.boxplot(x='Trabajo',y='Monto_credito', data=datos)

#perfil de las personas que hacen los prestamos mas costosos
#cosas = datos.groupby('Trabajo')['Monto_credito'].max().plot(kind='bar',legend='Reverse',figsize=(6,7))

#los prestamos menos costosos
#cosas = datos.groupby('Trabajo')['Monto_credito'].min().plot(kind='bar',legend='Reverse',figsize=(7,8))

#print (datos.corr(method="pearson"))
#plt.matshow(datos.corr())

############3
#punto 5
#plt.plot(datos['Monto_credito'],datos['Duracion_mes'], 'ro')
#plt.ylabel('Duracion_mes')
#plt.xlabel('Monto_credito')


#f, ax = plt.subplots(figsize=(8, 9))
#corr = datos.corr()
#sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
 #           cmap=sns.diverging_palette(220, 10, as_cmap=True),
#               square=True, annot=True, ax=ax)


#--------grupos de esad de creditos -------
#age_gro = pd.cut(datos['Edad'], bins=[18, 25, 35, 50, 65, 70, 85])
#print (pd.crosstab(age_gro, datos['Monto_credito']))

#cosa=sns.boxplot(x=age_gro,y='Monto_credito', data=datos)


age_gro = pd.cut(datos['Edad'], bins=[18, 25, 35, 50, 65, 70, 85])
print (pd.crosstab(age_gro, datos['Clasificacion']))
#plo = pd.crosstab(age_gro, datos['Clasificacion']).plot(kind='bar', title='Clasificacion',figsize=(9,8))






df= pd.DataFrame(datos['Edad'])
#gra=df.boxplot()

#cosa=sns.distplot(datos['Edad'])

# moto credito empleo actual
#cosa=sns.barplot(x='Empleo_actual',y='Monto_credito', data=datos)
#------------------------------------





d={'A40': 'automóvil (nuevo)' ,
   'A41': 'automóvil (usado)',
'A42': 'mobiliario / equipo',
'A43':'radio / televisión',
'A44': 'electrodomésticos',
'A45': 'reparaciones',
'A46': 'educación',
'A47': '(vacaciones - ¿no existe?)',
'A48' : 'reentrenamiento',
'A49': 'negocio',
'A410': 'otros'}
datos['Proposito'] = datos['Proposito'].apply(lambda x:d[x])
datos['Proposito'].head()


e={
'A71': 'desempleado', 
'A72': '... <1 año' ,
'A73': '1 <= ... <4 años', 
'A74':' 4 <= ... <7 años' ,
'A75': ' ..> = 7 años'  }
datos['Empleo_actual'] = datos['Empleo_actual'].apply(lambda x:e[x])
datos['Empleo_actual'].head()



c={
   'A11': '... <0 DM',
'A12': '0 <= ... <200 DM',
'A13': '...> = 200 DM / asignaciones salariales durante al menos 1 año',
'A14': 'no cuenta corriente'}
datos['Estado_cuenta_corriente'] = datos['Estado_cuenta_corriente'].apply(lambda x:c[x])
datos['Estado_cuenta_corriente'].head()



h={
   'A30': 'sin créditos tomados / todos los créditos pagados debidamente',
'A31': 'todos los créditos en este banco pagados debidamente',
'A32': 'créditos existentes pagados debidamente hasta ahora',
'A33' : 'retraso en el pago en el pasado',
'A34': 'cuenta crítica / otros créditos existentes (no en este banco)'}
datos['Historial_credito'] = datos['Historial_credito'].apply(lambda x:h[x])
datos['Historial_credito'].head()



cu={
    'A61': '... <100 DM',
'A62': '100 <= ... <500 DM',
'A63': '500 <= ... <1000 DM',
'A64': '..> = 1000 DM',
'A65': 'desconocido / sin cuenta de ahorro'}
datos['Cuenta_ahorro_bonos'] = datos['Cuenta_ahorro_bonos'].apply(lambda x:cu[x])
datos['Cuenta_ahorro_bonos'].head()


o={
   'A101': 'ninguno',
'A102':'cosolicitante' ,'A103': 'garante'}
datos['Otros_deudores'] = datos['Otros_deudores'].apply(lambda x:o[x])
datos['Otros_deudores'].head()


pl={
    'A141': 'banco',
'A142': 'tiendas',
'A143': 'ninguno'}
datos['Planes_cuotas'] = datos['Planes_cuotas'].apply(lambda x:pl[x])
datos['Planes_cuotas'].head()


v={
   'A151': 'alquiler',
'A152': 'propio',
'A153': 'gratis'}
datos['Vivienda'] = datos['Vivienda'].apply(lambda x:v[x])
datos['Vivienda'].head()


tl={
    'A191': 'ninguno',
'A192': 'sí, registrado bajo el nombre del cliente'}
datos['Telefono'] = datos['Telefono'].apply(lambda x:tl[x])
datos['Telefono'].head()

ex={
    'A201': 'sí',
'A202': 'no'}
datos['Extranjero'] = datos['Extranjero'].apply(lambda x:ex[x])
datos['Extranjero'].head()

pro={
     'A121': 'bienes inmuebles',
'A122': 'si no A121: ahorro de la sociedad de construcción acuerdo / seguro de vida',
'A123': 'si no A121 / A122: automóvil u otro, no en el atributo 6',
'A124': 'desconocido / sin propiedad'}
datos['Propiedad'] = datos['Propiedad'].apply(lambda x:pro[x])
datos['Propiedad'].head()


tra={
     'A171': 'desempleado / no calificado - no residente',
'A172' : 'no calificado - residente',
'A173': 'empleado calificado / funcionario',
'A174': 'gerencia / autónomo /empleado / funcionario altamente calificado'}
datos['Trabajo'] = datos['Trabajo'].apply(lambda x:tra[x])
datos['Trabajo'].head()



est={'A91': 'masculino: divorciado / separado',
'A92': 'femenino: divorciado / separado / casado',
'A93': 'masculino: soltero',
'A94': 'masculino: casado / viudo',
'A95': 'femenino: soltero'
     }
datos['Estado_civil_sexo'] = datos['Estado_civil_sexo'].apply(lambda x:est[x])
datos['Estado_civil_sexo'].head()

#cosas = datos.groupby('Proposito')['Monto_credito'].mean().plot(kind='bar',legend='Reverse',figsize=(6,6))


#perfil de las personas que hacen los prestamos mas costosos
#cosas = datos.groupby('Trabajo')['Monto_credito'].max().plot(kind='bar',legend='Reverse',figsize=(6,7))

#perfil menos prestamos
#cosa=sns.barplot(x=datos['Monto_credito'],y='Trabajo', data=datos)


#cosa=sns.barplot(x='Monto_credito',y='Estado_civil_sexo', data=datos)



#cosa=sns.barplot(x='Monto_credito',y='Empleo_actual', data=datos)


age_gro = pd.cut(datos['Edad'], bins=[18, 25, 35, 50, 65, 70, 85])
print (pd.crosstab(age_gro, datos['Clasificacion']))
#plo = pd.crosstab(age_gro, datos['Clasificacion']).plot(kind='bar', title='Clasificacion',figsize=(9,8))


#--------grupos de esad de creditos -------
#cosa=sns.boxplot(x=age_gro,y='Monto_credito', data=datos)

#menos costos
#cosas = datos.groupby('Trabajo')['Monto_credito'].max().plot(kind='bar',legend='Reverse',figsize=(6,7))


#cosa=sns.countplot(y='Trabajo',data=datos)
