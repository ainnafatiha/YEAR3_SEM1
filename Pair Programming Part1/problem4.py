# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:29:55 2019

@author: Asus
"""

import math 
a=4624
b=9049
result = 0
for i in range(a,b+1):
    if i%2 == 1:
        result += i
        print result