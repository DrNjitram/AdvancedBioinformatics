from DNA import *

strands = [strnd.sequence for strnd in read_fasta_file()]

positional = ["".join(_) for _ in zip(*strands)]



data = []
for pos in positional:
    data.append((pos.count("A"), pos.count("C"), pos.count("G"), pos.count("T")))

consensus_string = ""
for entry in data:
    max_entry = max(entry)
    consensus_string += "A" if max_entry == entry[0] else "C" if max_entry == entry[1] else "G" if max_entry == entry[2]  else "T"

print(consensus_string)
keys = ["A", "C", "G", "T"]
index = 0
for entry in zip(*data):
    print(f"{keys[index]}: " + " ".join(map(str, entry)))
    index += 1