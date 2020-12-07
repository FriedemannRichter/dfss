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

data = [219.20, 228.51, 223.40, 220.27, 226.59, 228.68, 225.88, 226.21, 222.61, 224.55, \
        224.71, 224.31, 227.20, 222.68, 224.03, 223.66, 226.25, 228.78, 230.33, 231.27, \
        221.99, 222.81, 230.83, 226.13, 223.34, 229.20, 220.34, 223.61, 222.19, 228.36, \
        230.87, 227.23, 229.49, 229.69, 227.09, 223.47, 227.72, 225.99, 221.64, 223.32, \
        219.20, 228.51, 223.40, 220.27, 226.59, 228.68, 225.88, 226.21, 222.61, 224.55]
    
"""Werte aus Aufgabe übernehmen"""
gamma = 0.95;


value = dfss.DFSS(data, 3)

#value.singlePlot()
#value.histogram()
#print(value.histogram.__doc__)
#value.konfidenz(gamma)
#value.achsen('Leistung P/W', 'Relative Häufigkeit h(m)')
#value.erwartungswert()
#value.ausbeute(220)

