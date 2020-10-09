# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:11:46 2020

@author: JESUS
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
datos=pd.read_csv('BD_casas.csv')

grupo = datos[['price','bedrooms','bathrooms','sqft_living']]

print(grupo)

#f, ax = plt.subplots(figsize=(8, 8))
#corr = grupo.corr()
#sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
#           cmap=sns.diverging_palette(220, 10, as_cmap=True),
 #           square=True, ax=ax)


Covariance = np.cov(datos['sqft_living'], datos['price'], ddof=0)[0][1]
print(Covariance)

x=datos['sqft_living']
y=datos['price']

#print(datos.corr())

cosas=sns.lmplot('price','sqft_living', datos, line_kws={'color':'red'})

modelo,x,x=cosas
resi=modelo.resid
plt.errorbar(x,y,xerr=0,yerr[resi, 0*resi],linestyles="None")