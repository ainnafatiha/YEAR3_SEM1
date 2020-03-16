from Bio.Seq import translate, CodonTable

with open('/home/ainna/Downloads/rosalind_2a.txt') as input_data:
	coding_dna, protein = [line.strip() for line in input_data.readlines()]

for table_id in CodonTable.ambiguous_generic_by_id.keys():
	if translate(coding_dna, table = table_id, stop_symbol = '', to_stop=False) == protein:
		genetic_code_variant = str(table_id)
		break

print genetic_code_variant
with open('/home/ainna/Downloads/Armory_010_PTRA.txt', 'w') as output_data:
	output_data.write(genetic_code_variant)
