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
import dfss
from scipy.io import loadmat
import numpy as np

#x = dfss.readMatlabFile('Schmelzwaerme')
x = loadmat('Schmelzwaerme')['VA']
data1 = np.array(x).reshape(x.shape[0]*x.shape[1])
x = loadmat('Schmelzwaerme')['VB']
data2 = np.array(x).reshape(x.shape[0]*x.shape[1])

    
"""Werte aus Aufgabe übernehmen"""
gamma = 0.95;

print('Werte VA')
value = dfss.DFSS(data1, 4)

# print('Werte VB')
# value = dfss.DFSS(data2, 3)

value.histogram()
value.konfidenzMittel(gamma, 20)
value.konfidenzVarianz(gamma)
value.normalverteilung()

# value.singlePlot()
# value.histogram()
# print(value.histogram.__doc__)
# value.konfidenz(gamma)
# value.achsen('Leistung P/W', 'Relative Häufigkeit h(m)')
# value.erwartungswert()
# value.ausbeute(220)

