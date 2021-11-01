from DNA import *

strands = [strnd.sequence for strnd in read_fasta_file()]

print(get_consensus_strand(strands))

positional = ["".join(_) for _ in zip(*strands)]

data = []
for pos in positional:
    data.append((pos.count("A"), pos.count("C"), pos.count("G"), pos.count("T")))

keys = ["A", "C", "G", "T"]
index = 0
for entry in zip(*data):
    print(f"{keys[index]}: " + " ".join(map(str, entry)))
    index += 1