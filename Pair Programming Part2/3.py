from collections import Counter
from collections import OrderedDict
 
fh = open('consesus_and_profile_output2.txt', 'wt')
 
rosalind = OrderedDict()
seqLength = 0
with open('rosalind_cons.txt') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            rosalindName = line
            rosalind[rosalindName] = ''
            continue
        rosalind[rosalindName] += line
    seqLength = len(rosalind[rosalindName])
 
A, C, G, T = [], [], [], []
consensusSeq = ''
for i in range(seqLength):
    seq = ''
    for k in rosalind.keys():
        seq += rosalind[k][i]
    A.append(seq.count('A'))
    C.append(seq.count('C'))
    G.append(seq.count('G'))
    T.append(seq.count('T'))
    counts = Counter(seq)
    consensusSeq += counts.most_common()[0][0]
 
fh.write(consensusSeq + '\n')
fh.write('\n'.join(['A:\t' + '\t'.join(map(str, A)), 'C:\t' + '\t'.join(map(str, C)),
                    'G:\t' + '\t'.join(map(str, G)), 'T:\t' + '\t'.join(map(str, T))]))
                    
fh.close()
