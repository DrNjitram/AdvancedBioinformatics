from DNA import *

key_strand, substrand = map(get_sequence, read_fasta_file())
print(key_strand)
print(substrand)

locations = [0]
for char in substrand:
    locations.append(key_strand.find(char, locations[-1]) + 1)

print("".join(key_strand[_ - 1] for _ in locations[1:]))

print(" ".join(map(str, locations[1:])))