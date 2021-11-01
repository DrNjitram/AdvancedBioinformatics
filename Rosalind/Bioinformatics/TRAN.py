from DNA import *

strand1, strand2 = read_fasta_file()

print(round(transition_transversion_ratio(strand1, strand2), 5))