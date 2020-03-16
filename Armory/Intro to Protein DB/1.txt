from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

with open('/home/ainna/Downloads/rosalind_ini.txt') as input_data:
	dna = Seq(input_data.read().strip(),IUPAC.unambiguous_dna)

dna_count = [str(dna.count(nucleotide)) for nucleotide in 'ACGT']

print ' '.join(dna_count)
with open('/home/ainna/Downloads/Armory_001_INI.txt', 'w') as output_data:
	output_data.write(' '.join(dna_count))
