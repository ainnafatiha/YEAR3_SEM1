# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:30:04 2019

@author: Asus
"""

i = 1
f = open('rosalind_ini5 (1).txt')
for line in f.readlines():
    if i % 2 == 0 :
        print line
    i += 1