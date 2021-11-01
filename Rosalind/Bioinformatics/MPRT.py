import urllib.request
from DNA import *
import re

with open("input.txt", "r") as inp:
    uniprots = [uniprot.strip() for uniprot in inp.readlines()]
    for uniprot in uniprots:
        urllib.request.urlretrieve("https://www.uniprot.org/uniprot/" + uniprot + ".fasta", "Data/" + uniprot + ".fasta")

    strands = []
    for uniprot in uniprots:
        strand = read_fasta_file("Data/" + uniprot + ".fasta", "protein")[0]
        strand.title = uniprot
        strands.append(strand)

    motif = "N{P}[ST]{P}"
    motif_regex = motif_to_regex(motif)

    for strand in strands:

        matches = re.finditer(motif_regex, strand.protein)

        results = [str(match.span()[0] + 1) for match in matches]
        if len(results) > 0:
            print(strand.title)
            print(" ".join(results))
