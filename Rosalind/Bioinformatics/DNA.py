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


class Strand:
    def __init__(self, sequence: str, title="", raw_type="DNA", protein=""):
        self.sequence = sequence.upper()
        self.raw_type = raw_type
        self.title = title
        self.protein = protein

    def reverse(self):
        """"
        Reverses the sequence

        :returns reversed sequence
        """
        self.sequence = self.sequence[::-1]
        return self.sequence

    def flip(self):
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

    def get_complement(self):
        """
        Get the complemented string
        Does not modify sequence

        :returns complement of sequence
        """
        if self.raw_type == "DNA":
            return "".join(["A" if char == "T" else "T" if char == "A" else "C" if char == "G" else "G" for char in self.sequence])
        else:
            return "".join(["A" if char == "U" else "U" if char == "A" else "C" if char == "G" else "G" for char in self.sequence])

    def get_reverse_complement(self):
        """"
        Get the reversed complement
        does not modify sequence

        :returns reverse complement of sequence
        """
        return self.get_complement()[::-1]

    def shift(self, amount=1):
        """
        Shift sequence by basepairs
        Used to obtain orf's
        """
        self.sequence = self.sequence[-amount:] + self.sequence[:-amount]

    def gc_amount(self):
        """
        Calculate the GC amount

        :returns fraction of sequence containing G or C
        """
        return (self.sequence.count("G") + self.sequence.count("C")) / len(self.sequence)

    def count_bases(self, base="ACGT"):
        """"
        :param base base pairs to obtain info from, default = "ACGT"

        :returns list with counts of A, C, G, T
        """
        all_bases = "ACGT"
        return [self.sequence.count(code) for code in all_bases if code in base]

    def to_protein(self, include_stop=False):
        """
        Create protein from the current sequence
        Will convert to RNA if type is DNA using flip()
        :param include_stop Will print out 'Stop' for stop codons. Otherwise will discard them

        :returns protein sequence
        """
        if self.raw_type == "DNA":
            self.flip()
            return self.to_protein(include_stop)
        else:
            self.protein = "".join([translation.get(self.sequence[i: i + 3], "") for i in range(0, len(self.sequence), 3)])
            if not include_stop:
                self.protein = self.protein.replace("Stop", "")
            return self.protein

    def get_frames(self):
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

    def get_orfs(self):
        """
        Obtain all reading open frames from the current sequence when converted to protein.
        Will return 6 frames (does include reverse complement frames)

        :returns six frames
        """
        return set(self.get_frames() + Strand(self.get_reverse_complement()).get_frames())

    def subs(self, sub: str):
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


def hamming_distance(strand1: Strand, strand2: Strand):
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

    for i in range(0, len(sequence1)):
        if sequence1[i] != sequence2[i]:
            result += 1
    return result


def get_strands(filename="input.txt"):
    """
    Returns a list of all sequences in the provided fasta format file as Strands

    :param filename file to open (default input.txt)

    :returns list of all strands
    """
    strands = []

    with open(filename, "r") as file:
        entries = [entry.split("\n") for entry in file.read().split(">")[1:]]

    for entry in entries:
        label = entry[0]
        data = "".join(entry[1:])
        strands.append(Strand(data, label))

    return strands


def read_file(filename="input.txt", crosses_lines=False):
    """
    Returns a list of all sequences in the provided file as Strands

    :param filename file to open
    :param crosses_lines set if strands are separated by linebreaks. Different strands are separated by empty lines.

    :returns list of all strands
    """
    strands = []

    with open(filename, "r") as file:
        entries = [entry.split("\n") for entry in file.read().split("\n\n")]

    if not crosses_lines:
        strands = [Strand(strand) for strand in entries[0]]
    else:
        for entry in entries:
            strands.append(Strand("".join(entry)))

    return strands
