from DNA import *

strands = [_.sequence for _ in read_fasta_file()]

print(get_superstring(strands))
