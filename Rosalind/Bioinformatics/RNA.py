from DNA import *

strand = read_file()[0]
strand.flip()

print(strand.sequence)