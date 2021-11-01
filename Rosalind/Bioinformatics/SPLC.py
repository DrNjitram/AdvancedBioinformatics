from DNA import *

strands = read_fasta_file()

key_strand = strands.pop(0)

key_strand.remove_introns([strand.sequence for strand in strands])

print(key_strand.to_protein())
