# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:48:58 2019

@author: Asus
"""
from scipy.special import comb

def calculateProbability(k, m, n):
    totalPop = k + m + n 
    totalCombos = comb(totalPop, 2)
    validCombos = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
    probability = validCombos/totalCombos
    return probability

print calculateProbability(25, 23, 23)
