# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:28:27 2019

@author: Asus
"""

n = 32                      
k = 3                      
big = 1                    
small = 1                  
for months in range(1,n-1):
      bigger = big + small*k   
      small = big              
      big = bigger             
print(big)          