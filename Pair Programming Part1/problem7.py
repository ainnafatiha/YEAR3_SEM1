# -*- coding: utf-8 -*-
"""
Spyder Editor


This is a temporary script file.
"""

#! /usr/bin/python
s = "GACGGATTTAATGCCGAGATTTGTTAAGTGGGTAACCCTTGAGACAGATAATAGTCGTTTAGGTATACATTAAACAAACAGAAGTGAAGCATCAGGCAACCTATGCGCTGCTGATCAGGCCGTCGTCGTATTCGCTTGATCGACCGGATACCAGTCAGACTGTACGTGACTCTCTCCGGGCGGAAAACGCCGAAGTATCTTACGCAACATACTGACCTGAACTGATTTGTCCACATAGAAAGAGATAGGAGATAAGCGCGCCCCTTTCTCCGTACAGTTAGATCCGACGCCCTCTTGCGGAGATATTTCGTGGCGTGCAATGGCATCACGGTGTGTACAGTTTCTCGCATATAATACTTAAGACCGCCTTATGCAAGACCAGGCGGCTGTCGTAGTGCCACTAGAGCACTAGCCCGGCATATCAGACCCATTCGCACCCATCCAATGGAACCCGTGTATCTTGAACCATTATTCAAGTCCGTCAGGACCCGCAACGATGCATCACATTTTTCGCTATTAGCCCATTCAATTGTGGATTCGACGGTGCTATCCGCTACTATTCCATTTGAGCCAAACAACTTCGGTAGGTATAATACTGATCGACAAGCAGCTACGCTCGCCGGTCGTACGCATCGGGGTACAGACGTTTACAACCTGGGTGCCATCATGGACTATTATAGGGCGCCGGAAAATACCGATTGGGTGTACGTGTCTCCTTTGTCCGCATACCGCGTAATCACTCATCTGCGCTGATTCTCTTCACACGTTGCTGCACAAGATACGGGGAAAAGCGAGGTCTAAAGTCACGTCACGCAGGCGCTGGTAATTGTCTGGCCTCTTCCCGATAGCTTAAGTAAACCCCTTCTGACGACCAGTGATCAATCACGCATGCTCGGCTTTTCTATGCTAGTCCCACGATTGTTCCGTGTATTTTCGTGAAGGGGTGAGGCCAGGCGAAGCTCGTTAAAGCAAAAGACCATGCACCCTTACAAACCAAAGT"
count = 0

for i in s :
    if i == 'A':
        count = count + 1
        
print ("Count of A in s is : " +  str(count)) 

count = 0
for i in s :
    if i == 'C':
        count = count + 1
        
print ("Count of C in s is : " +  str(count)) 

count = 0
for i in s: 
    if i == 'G': 
        count = count + 1
  
# printing result  
print ("Count of G in s is : " +  str(count)) 

count = 0
for i in s :
    if i == 'T':
        count = count + 1
        
print ("Count of T in s is : " +  str(count)) 
