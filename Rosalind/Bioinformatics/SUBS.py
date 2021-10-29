from DNA import *

strands = read_file()
print(" ".join([str(_) for _ in strands[0].subs(strands[1].sequence)]))