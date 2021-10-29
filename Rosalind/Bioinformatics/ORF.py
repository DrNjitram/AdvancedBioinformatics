from DNA import *

strand = read_fasta_file()[0]

result = "\n".join(strand.get_orfs())

print(result)
