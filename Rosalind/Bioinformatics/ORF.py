from DNA import *

strand = get_strands()[0]

result = "\n".join(strand.get_orfs())

print(result)
