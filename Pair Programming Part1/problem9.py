# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:48:38 2019

@author: Asus
"""
sequence = "GCCGCGAAGATTAGTGAGGAAGGAACTTGCGAGTGTTACATGGCATTCCTCGCGGCTTTTTTCTCAATTTAGTTGAGGCTTGTACTATAAAGTGAATGAGATCGAGAGTTTTACAGAGACACCAACGAGACACTAAGTACTGAACGTCGGGAACAACTAAACTTCATGATGTAGATAACCGCGGGCAACCTGAGTGGACACCGAAACCGGGATTGTAGTTGTCTCATGTCCCGCTGGAACTTCAAAGTTCGCACCTTACATTTTCGCGGCTATTAGGTACACCGGCGTGTCCTAGACCCCCGCATGCCTTCAATTACCACCGCAACCCGGTGTCACAGTCAGGCTGCTGCAGGGTTACGAGTTGACTGCTCTATCTCTACTAGCGACCATAATCAAGCTAAGTAAGGAGATATCTAACCGTGTTAGGAAGTGGAGCTCAAACAAATCAAGTCTGGATAGTCCTTGTGGCGCGTTTCAATGCTGAAACCTCGCTAATGCGAAACAAAATCAGTGGTGTCTTGAGAATCAGGGCACAGGTTAACAGAGGAGCCGCTAACCCCTTTGCCAAGATCGCCGCTATTTATTCTAGGCATCCAGGGGACGTTGGGCTCCGCTGGTACACCCACATAATCTGATCAAGGGAAAAGACGGCGTCGACAAAATCTCCTCCCAACTGGCTCAAAGACGGCACAGTTTCGGTTGGCATCTACATCAGTTTAGGGGCAAGACCCTACGATCTGAAGGAAAGCGATCCCCTACAATAATGCACCCCCAGACTAGAGTTTAACGTGTAGCCAGGCATCG"
answer = []
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

for nucleotide in sequence:
    answer.append(complement[nucleotide])

print ''.join(answer[::-1])
