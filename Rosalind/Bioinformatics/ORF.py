from DNA import *

strands = get_strands()

strand = strands[0]

result = "\n".join(strand.get_orfs())

print(result)
