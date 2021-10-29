from DNA import *

strands = get_strands()

lengths = [_.gc_amount() for _ in strands]
max_index = lengths.index(max(lengths))
print(strands[max_index].title)

print(round(strands[max_index].gc_amount() * 100, 6))

