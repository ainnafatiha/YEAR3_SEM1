from Bio import SeqIO

with open('/home/ainna/Downloads/rosalind_tfsq.txt') as input_data, open('/home/ainna/Downloads/Armory_008_TFSQ.txt', 'w') as output_data:
	SeqIO.convert(input_data, 'fastq', output_data, 'fasta' )
