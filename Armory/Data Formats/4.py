import sys
import numpy as np
from Bio import SeqIO

def main():
    with open("/home/ainna/Downloads/bphr.txt") as f:
        threshold = int(f.readline().strip())
        fastq = np.array([rcd.letter_annotations["phred_quality"] for rcd in SeqIO.parse(f, "fastq")])
        fq = np.mean(fastq, axis=0)
    sys.stdout = open("bphrANS.out", "w")
    print len(fq[fq < threshold])

if __name__ == '__main__':
    main()
