from DNA import *

strand = read_file()[0]

print(" ".join(map(str, strand.count_bases())))