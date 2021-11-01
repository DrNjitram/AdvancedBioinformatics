from DNA import *

overlap_length = 3

strands = read_fasta_file()

suffixes = {}
prefixes = {}

for strand in strands:
    suffix = strand.sequence[-overlap_length:]
    prefix = strand.sequence[:overlap_length]

    if suffix in suffixes:
        suffixes[suffix] = suffixes[suffix] + [strand.title]
    else:
        suffixes[suffix] = [strand.title]

    if prefix in prefixes:
        prefixes[prefix] = prefixes[prefix] + [strand.title]
    else:
        prefixes[prefix] = [strand.title]


for suffix in suffixes:
    if suffix in prefixes:
        for suffix_title in suffixes[suffix]:
            for prefix_title in prefixes[suffix]:
                if suffix_title != prefix_title:
                    print(suffix_title, prefix_title)
