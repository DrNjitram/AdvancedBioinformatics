from DNA import *

strand = read_fasta_file()[0]

min_length = 4
max_length = 12

for position in range(len(strand.sequence) - min_length + 1):
    for length in range(min_length, max_length + 1):
        if position + length > len(strand.sequence):
            continue

        sub_strand = Strand(strand.sequence[position:position + length])
        if sub_strand.sequence == sub_strand.get_reverse_complement():
            print(position + 1, length)
