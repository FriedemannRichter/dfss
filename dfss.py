# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:17:47 2020

@author: Richter
"""

import matplotlib.pyplot as plt
import numpy as np
import math as ma
from scipy.stats import t, norm, chi2, f
from scipy.io import loadmat


class DFSS():
    def __init__(self, data, NKS = 2):
        """
        initialisiert ein dfss objekt
        
        Parameters
        ----------
        data : array_like
            Daten zum verarbeiten
        """
        # Daten der Klassen übergeben
        self.x = data
        self.NKS = NKS
        self.fig = None
        self.ax1 = None
        
        # Mittelwert berechnen
        self.quer = np.mean(self.x)
        print('Mittelwert: ', round(self.quer, self.NKS))
        # Minimalwert herrausfinden
        self.x_min = np.amin(self.x)
        print('Minimalwert: ', round(self.x_min, self.NKS))
        # Maximalwert herrausfinden
        self.x_max = np.amax(self.x)
        print('Maximalwert: ', round(self.x_max, self.NKS))
        # Anzahl bestimmen
        self.N = np.size(self.x)
        print('Werteanzahl: ', self.N)
        # Differenz zwischen maximal und Minimalwert
        self.diff = self.x_max - self.x_min
        # Standardabweichung berechnen
        self.s = np.std(data,ddof=1)
        print('Standardabweichung: ', round(self.s, self.NKS))
        
    def singlePlot(self):
        """
        einen single plot erstellen

        Returns
        -------
        None.

        """
        self.fig = plt.figure(1, figsize=(12,4))
        self.ax1 = self.fig.subplots(1)
    
    def histogram(self):
        """
        Ein histogramm erstellen

        Returns
        -------
        None.

        """
        #wenn noch kein plot definiert wurde erstellen
        if self.ax1 is None:
            self.singlePlot()
            
        if self.diff < 0.01:
            self.histMin = (np.floor((self.x_min*1000))/1000)-0.005
            self.histMax = (np.ceil((self.x_max*1000))/1000)+0.005
            self.histStep = 0.001
        elif self.diff < 0.1:
            self.histMin = (np.floor((self.x_min*100))/100)-0.05
            self.histMax = (np.ceil((self.x_max*100))/100)+0.05
            self.histStep = 0.01
        else:
            self.histMin = (np.floor(self.x_min*10)/10)-0.5
            self.histMax = (np.ceil(self.x_max*10)/10)+0.5
            self.histStep = 0.1
                                
        x_freq, grenzen = np.histogram(self.x, bins=np.arange(self.histMin, self.histMax, self.histStep))
        self.ax1.hist(self.x, grenzen, histtype='bar', color='b', weights=np.ones(self.N)/self.N/self.histStep, rwidth=1-self.histStep*10)
        self.ax1.grid(True, which='both', axis='both', linestyle='--')
    
    
    def konfidenzMittel(self, gamma, end = 0.2):
        """
        Konfidenz des Mittelwertes berechnen und in Plot zeichnen

        Parameters
        ----------
        gamma : nummeric
            gamma Wert.

        Returns
        -------
        None.

        """
        self.c1 = norm.ppf((1-gamma)/2)
        self.c2 = norm.ppf((1+gamma)/2)
        mu_min = self.quer - ((self.c2*self.s)/np.sqrt(self.N))
        mu_max = self.quer - ((self.c1*self.s)/np.sqrt(self.N))
        if self.ax1 is None:
            self.singlePlot()
            
        self.ax1.plot([mu_min,mu_min], [0,end], color='red')
        self.ax1.plot([mu_max,mu_max], [0,end], color='green')
        print('Mittelwert \u03bc min =' , round(mu_min , self.NKS))
        print('Mittelwert \u03bc max: ', round(mu_max , self.NKS))
        
        
    def konfidenzVarianz(self, gamma):
        """
        Konfidenz der Varianz berechnen und in Plot zeichnen

        Parameters
        ----------
        gamma : nummeric
            gamma Wert.

        Returns
        -------
        None.

        """
        s_c1 = chi2.ppf((1-gamma)/2, self.N-1)
        s_c2 = chi2.ppf((1+gamma)/2, self.N-1)
        sigma_max = ma.sqrt((self.s**2)*(self.N-1)/s_c1)
        sigma_min = ma.sqrt((self.s**2)*(self.N-1)/s_c2)
        print('Standardabweichung \u03C3 min =' , round(sigma_min , self.NKS))
        print('Standardabweichung \u03C3 max: ', round(sigma_max , self.NKS))
    
    
    def normalverteilung(self):
        """
        normalverteilung berechnen und in Plot zeichnen
        """
    
        x_n = np.linspace (self.histMin, self.histMax, 10000)
        F = norm.pdf(x_n, self.quer, self.s)

        # wenn plot noch nicht existiert erstellen
        if self.ax1 is None:
            self.singlePlot()
            
        self.ax1.plot(x_n, F, color='cyan')
        
        
    def achsen(self,xlabel,ylabel):
        self.ax1.set_xlabel(xlabel)
        self.ax1.set_ylabel(ylabel)
        
    def erwartungswert(self):
        x_z_min = self.quer + self.c1 * self.s * ma.sqrt(1+1/self.N)
        x_z_max = self.quer + self.c2 * self.s * ma.sqrt(1+1/self.N)
        print('Der zukuenftige Wert liegt mit 95% Wahrscheinlichkeit zwischen ', round(x_z_min , self.NKS) , 'Watt und ', round(x_z_max , self.NKS) ,'Watt')
        
    def ausbeute(self, value):
        p = t.cdf(( value - self.quer) / ( self.s * ma.sqrt(1+1/self.N) ),self.N-1)
        Ausbeute = 1 - p
        print ('Ausbeute =', round(Ausbeute * 100, 2 ) ,'%')

def readMatlabFile(file):
    data = loadmat(file)
    for x in data:
        if(x != '__header__' and x != '__version__' and x != '__globals__'):
            y = data[x]
    return y