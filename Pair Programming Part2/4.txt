#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:30:19 2019

@author: ainna
"""

import math                                                                    
m = 7                                                                       
n = 31                                                                        
P = 2**m                                                                      
probability = 0                                                                
for i in range (n, P + 1):   
    #probability formula                                                   
    prob = (math.factorial(P) /                                                
            (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(
                P - i))                                                        
    probability += prob                                                        
print(probability)    
