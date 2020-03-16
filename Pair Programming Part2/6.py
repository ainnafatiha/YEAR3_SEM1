# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:12:41 2019

@author: Owner
"""


import urllib2
import re
list = ['P00750_UROT_HUMAN'
,'P01044_KNH1_BOVIN'
,'P08198_CSG_HALHA'
,'B3CNE0'
,'P11171_41_HUMAN'
,'Q81QB7'
,'Q8ER84'
,'Q3B391'
,'A1X8C2'
,'P04180_LCAT_HUMAN'
,'P81331'
,'Q9V730'
,'P49286']
 
for one in list:
    name = one.strip('\n')
    url = 'http://www.uniprot.org/uniprot/'+name+'.fasta'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    start = the_page.find('\nM')
    seq = the_page[start+1:].replace('\n','')
    seq = ' '+seq
    regex = re.compile(r'N(?=[^P][ST][^P])')
    index = 0
    out = []
    '''
    out = [m.start() for m in re.finditer(regex, seq)]
    '''
 
    index = 0
    while(index<len(seq)):
        index += 1
 
        if re.search(regex,seq[index:]) == None:
            break
 
 
        #print S[index:]
        if re.match(regex,seq[index:]) != None:
            out.append(index)
 
 
 
 
    if out != []:
        print name
        print ' '.join([ str(i) for i in out])
