# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:44:23 2020

@author: Richter
"""

"""  Initialisierung: Variablen löschen, Konsole leeren """    
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass
    
""" Bibliotheken importieren"""

import math as ma
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
# from scipy.stats import skew
from scipy.io import loadmat
# from IPython import get_ipython
from scipy.stats import t     # Normalverteitung
from scipy.stats import chi2     # Normalverteitung
#from scipy.stats import t, norm, chi2, f

data = loadmat('Schmelzwaerme')['VA']
x1 = np.array(data).reshape(data.shape[0]*data.shape[1])
data = loadmat('Schmelzwaerme')['VB']
x2 = np.array(data).reshape(data.shape[0]*data.shape[1])


"""Definition Nachkommastellen"""
KS=2

"""*****************************************************************"""
"""Bestimmung Datenumfang"""
"""*****************************************************************"""

x_min = np.amin(x1)
x_max = np.amax(x1)
N = x1.shape[0]
gamma = 0.95

"""*****************************************************************"""
""" Mittelwert berechen"""
"""*****************************************************************"""

x_quer = np.mean(x1)

print('Mittelwert:', round(x_quer, KS ) ,'Watt')

"""*****************************************************************"""
"""Berechnen der Standardabweichung"""
"""*****************************************************************"""

s = np.std(x1, ddof=1)

print('Standardabweichung:', round(s, KS))

"""*****************************************************************"""
"""Konfidenzbereiche für den Mittelwert"""
"""*****************************************************************"""

c1 = t.ppf((1-gamma)/2, N-1)
c2 = t.ppf((1+gamma)/2, N-1)
mu_min = x_quer -(c2*s/ma.sqrt(N))
mu_max = x_quer -(c1*s/ma.sqrt(N))

print('Mü_min =',round(mu_min, KS),' Mü_max=',round(mu_max,KS))

"""*****************************************************************"""
""" Konfidenzbereiche für die Standardabweichung """
"""*****************************************************************"""
s_c1 = chi2.ppf((1-gamma)/2, N-1)
s_c2 = chi2.ppf((1+gamma)/2, N-1)
sigma_max = ma.sqrt((s**2)*(N-1)/s_c1)
sigma_min = ma.sqrt((s**2)*(N-1)/s_c2)

print ('Standardabweichung Sigma min =' , round(sigma_min , KS) , ' Standardabweichung Sigma max: ', round(sigma_max , KS) )

fig = plt.figure(1, figsize=(12,4))
ax1 = fig.subplots(1)

histMin = np.floor(x_min*100)/100-0.05
histMax = np.ceil(x_max*100)/100+0.05
histStep = 0.01
x_freq, grenzen = np.histogram(x1)#, bins=np.arange(histMin, histMax, histStep))
ax1.hist(x1, 10, density=True)
ax1.grid(True, which='both', axis='both', linestyle='--')
    

