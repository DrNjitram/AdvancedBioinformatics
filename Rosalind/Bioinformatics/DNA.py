"""
Author: Martijn Gobes

Provides a myriad of helper functions for sequence related functions.
"""

import sys
from typing import List, Set

translation = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G"
}

reverse_translation = {
    'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'],
    'D': ['GAU', 'GAC'], 'K': ['AAA', 'AAG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'Y': ['UAU', 'UAC'],
    'H': ['CAU', 'CAC'],
    'W': ['UGG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'M': ['AUG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
    'F': ['UUU', 'UUC'],
    'Stop': ['UAA', 'UAG', 'UGA'],
    'C': ['UGU', 'UGC'],
    'N': ['AAU', 'AAC']
}


class Strand:
    """
    Creates a strands class from a sequence of basepairs or protein
    """
    def __init__(self, sequence="", title="", raw_type="DNA", protein=""):
        """
        Returns a strand object

        :param sequence initialised sequence
        :param title initialised title
        :param raw_type initialised type (DNA or RNA)
        :param protein initialised protein string
        """
        self.sequence = sequence.upper()
        self.raw_type = raw_type
        self.title = title
        self.protein = protein

    def reverse(self) -> str:
        """"
        Reverses the sequence

        :returns reversed sequence
        """
        self.sequence = self.sequence[::-1]
        return self.sequence

    def flip(self) -> None:
        """"
        Flips the sequence from RNA to DNA and vice versa

        :returns flipped sequence
        """
        if self.raw_type == "DNA":
            self.raw_type = "RNA"
            self.sequence = self.sequence.replace("T", "U")
        else:
            self.raw_type = "DNA"
            self.sequence = self.sequence.replace("U", "T")

        return self.sequence

    def get_complement(self) -> str:
        """
        Get the complemented string
        Does not modify sequence

        :returns complement of sequence
        """
        if self.raw_type == "DNA":
            return "".join(["A" if char == "T" else "T" if char == "A" else "C" if char == "G" else "G" for char in self.sequence])
        # So it is RNA
        return "".join(["A" if char == "U" else "U" if char == "A" else "C" if char == "G" else "G" for char in self.sequence])

    def get_reverse_complement(self) -> str:
        """"
        Get the reversed complement
        does not modify sequence

        :returns reverse complement of sequence
        """
        return self.get_complement()[::-1]

    def shift(self, amount=1) -> None:
        """
        Shift sequence by basepairs
        Used to obtain orf's
        """
        self.sequence = self.sequence[-amount:] + self.sequence[:-amount]

    def gc_amount(self) -> float:
        """
        Calculate the GC amount

        :returns fraction of sequence containing G or C
        """
        return sum(map(lambda x: 1 if x in ("G", "C") else 0, self.sequence)) / len(self.sequence)

    def count_bases(self, base="ACGT") -> List[int]:
        """"
        :param base base pairs to obtain info from, default = "ACGT"

        :returns list with counts of A, C, G, T
        """
        all_bases = "ACGT"
        return [self.sequence.count(code) for code in all_bases if code in base]

    def to_protein(self, include_stop=False) -> str:
        """
        Create protein from the current sequence
        Will convert to RNA if type is DNA using flip()
        :param include_stop Will print out 'Stop' for stop codons. Otherwise will discard them

        :returns protein sequence
        """
        if self.raw_type == "DNA":
            self.flip()
            return self.to_protein(include_stop)

        self.protein = "".join([translation.get(self.sequence[i: i + 3], "") for i in range(0, len(self.sequence), 3)])
        if not include_stop:
            self.protein = self.protein.replace("Stop", "")
        return self.protein

    def get_frames(self) -> List[str]:
        """
        Obtain all reading frames from the current sequence when converted to protein.
        Will return 3 frames (does not include reverse complement frames)

        :returns three frames
        """

        frames = self.to_protein(True).split("Stop")[:-1]
        self.shift()
        frames += self.to_protein(True).split("Stop")[:-1]
        self.shift()
        frames += self.to_protein(True).split("Stop")[:-1]
        self.shift(-2)

        result = []

        for frame in frames:
            while "M" in frame:
                result.append(frame[frame.find("M"):])
                frame = frame[frame.find("M") + 1:]

        return result

    def get_orfs(self) -> Set[str]:
        """
        Obtain all reading open frames from the current sequence when converted to protein.
        Will return 6 frames (does include reverse complement frames)

        :returns six frames
        """
        return set(self.get_frames() + Strand(self.get_reverse_complement()).get_frames())

    def subs(self, sub: str) -> List[int]:
        """
        Find all locations of the a sequence in the current sequence

        :param sub sub-sequence to match

        :returns list of locations where sub is present in sequence
        """
        result = []
        seq = self.sequence
        while sub in seq:
            result.append(seq.find(sub) + 1)
            seq = seq[seq.find(sub) + 1:]

        result = [sum(result[:i + 1]) for i, _ in enumerate(result)]
        return result

    def remove_introns(self, introns: List[str]) -> str:
        """
        Remove all the strings in introns from its sequence.
        Modifies the sequence

        :param introns list of strings to remove

        :returns the modified internal sequence
        """
        for intron in introns:
            self.sequence = self.sequence.replace(intron, "")
        return self.sequence

    def __str__(self) -> str:  # Helper function to more easily print what is in the Strand class
        return (">" + self.title if self.title != "" else "") + (("\n" + self.sequence) if self.sequence != "" else "") + (("\n" + self.protein) if self.protein != "" else "")


def hamming_distance(strand1: Strand, strand2: Strand) -> int:
    """
    Calculate the Hamming distance of both strands

    :param strand1 Strand 1
    :param strand2 Strand 2

    :returns distance of sequence 1 to sequence 2
    """
    sequence1 = strand1.sequence
    sequence2 = strand2.sequence

    if len(sequence2) != len(sequence1):
        raise Exception("sequences must have equal length")
    result = 0

    for i, value in enumerate(sequence1):
        if value != sequence2[i]:
            result += 1
    return result


def read_fasta_file(filename="input.txt", sequence_type="DNA") -> List[Strand]:
    """
    Returns a list of all sequences in the provided fasta format file as Strands

    :param filename file to open
    :param sequence_type what type the input is (DNA, RNA or protein)

    :returns list of all strands
    """
    strands = []

    with open(filename, "r", encoding="utf-8") as file:
        entries = [entry.split("\n") for entry in file.read().split(">")[1:]]

    for entry in entries:
        label = entry[0]
        data = "".join(entry[1:])
        if sequence_type == "protein":
            strands.append(Strand(protein=data.strip(), title=label))
        else:
            strands.append(Strand(data.strip(), label, sequence_type))

    return strands


def read_file(filename="input.txt", crosses_lines=False, sequence_type="DNA") -> List[Strand]:
    """
    Returns a list of all sequences in the provided file as Strands

    :param filename file to open
    :param crosses_lines set if strands are separated by linebreaks. Different strands are separated by empty lines.
    :param sequence_type what type the input is (DNA, RNA or protein)

    :returns list of all strands
    """
    strands = []

    with open(filename, "r", encoding="utf-8") as file:
        entries = [entry.split("\n") for entry in file.read().split("\n\n")]

    if not crosses_lines:
        strands = [Strand(strand) for strand in entries[0]]
    else:
        for entry in entries:
            if sequence_type == "protein":
                strands.append(Strand(protein="".join(entry).strip()))
            else:
                strands.append(Strand("".join(entry).strip(), raw_type=sequence_type))

    return strands


def motif_to_regex(motif: str) -> str:
    """
    Takes a basepair motif and makes it into a regex string
    Detects overlapping motifs

    :param motif to convert

    :returns regex string
    """
    return r"(?=(" + motif.replace("{", "[^").replace("}", "]") + "))"


def get_sequence(strand: Strand) -> str:
    """
    Helper function to use in mapping
    Returns the sequence inside the strand

    :param strand Strand

    :returns the sequence of the strand
    """
    return strand.sequence


def transition_transversion_ratio(strand1: Strand, strand2: Strand) -> float:
    """
    Calculates the transition/transversion ratio for the provided strands

    :param strand1 Strand 1
    :param strand2 Strand 2

    :returns the ratio as float
    """
    transitions = 0
    transversion = 0

    sequence_1 = strand1.sequence
    sequence_2 = strand2.sequence

    for bp1, bp2 in zip(sequence_1, sequence_2):
        if bp1 != bp2:
            if (bp1, bp2) == ("A", "G") or (bp1, bp2) == ("G", "A") or (bp1, bp2) == ("T", "C") or (bp1, bp2) == ("C", "T"):
                transitions += 1
            else:
                transversion += 1

    return transitions / transversion


def get_superstring(strands: List[str]) -> str:
    """
    Produces the shortest superstring for the provided list of strings.
    This is optimised for the Rosalind problem and is NOT a general solution.

    :param strands list of strings to overlap

    :returns superstring of strands
    """
    highest_overlap = []
    total_length = len(strands)
    while len(strands) > 1:
        i = total_length - len(strands)

        sys.stdout.write('\r')
        sys.stdout.write(f"[{'=' * i:{total_length - 1}}] {(100 / (total_length- 1) * i):.1f}%")
        sys.stdout.flush()

        highest_overlap = [0, "", "", ""]
        for strand_1 in strands:
            for strand_2 in strands:
                if strand_2 == strand_1:
                    continue

                overlap = 0
                for length in range(len(strand_1)):
                    if strand_2.startswith(strand_1[-length:]):
                        overlap = length

                if overlap > highest_overlap[0]:
                    highest_overlap = [overlap, strand_1[:-overlap] + strand_2, strand_1, strand_2]

        strands.append(highest_overlap[1])
        strands.remove(highest_overlap[2])
        strands.remove(highest_overlap[3])
    sys.stdout.write('\r')
    return highest_overlap[1]


def get_consensus_strand(strands: List[str]) -> str:
    """
    Produces a consensus strand for all sequences in strands

    :param strands list of strings, length much b equal

    :returns consensus string
    """
    positional = ["".join(_) for _ in zip(*strands)]

    data = []
    for pos in positional:
        data.append((pos.count("A"), pos.count("C"), pos.count("G"), pos.count("T")))

    consensus_string = ""
    for entry in data:
        max_entry = max(entry)
        consensus_string += "A" if max_entry == entry[0] else "C" if max_entry == entry[1] else "G" if max_entry == entry[2] else "T"

    return consensus_string
