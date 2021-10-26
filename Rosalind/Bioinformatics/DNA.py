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
        return self.sequence[::-1]

    def flip(self):
        if self.raw_type == "DNA":
            self.raw_type = "RNA"
            self.sequence = self.sequence.replace("T", "U")
        else:
            self.raw_type = "DNA"
            self.sequence = self.sequence.replace("U", "T")

    def complement(self):
        if self.raw_type == "DNA":
            return "".join(["A" if char == "T" else "T" if char == "A" else "C" if char == "G" else "G" for char in self.sequence])
        else:
            return "".join(["A" if char == "U" else "U" if char == "A" else "C" if char == "G" else "G" for char in self.sequence])

    def reverse_complement(self):
        return self.complement()[::-1]

    def shift(self, amount=1):
        self.sequence = self.sequence[-amount:] + self.sequence[:-amount]

    def gc_amount(self):
        return (self.sequence.count("G") + self.sequence.count("C"))/len(self.sequence)

    def to_protein(self, include_stop=False):
        if self.raw_type == "DNA":
            self.flip()
            return self.to_protein(include_stop)
        else:
            self.protein = "".join([translation.get(self.sequence[i: i + 3], "") for i in range(0, len(self.sequence), 3)])
            if not include_stop:
                self.protein = self.protein.replace("Stop", "")
            return self.protein

    def get_frames(self):
        if self.protein == "":
            self.to_protein(True)

        frames = self.protein.split("Stop")[:-1]
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
        return set(self.get_frames() + Strand(self.reverse_complement()).get_frames())

    def subs(self, sub):
        result = []
        seq = self.sequence
        while sub in seq:
            result.append(seq.find(sub) + 1)
            seq = seq[seq.find(sub) + 1:]

        result = [sum(result[:i + 1]) for i, _ in enumerate(result)]
        return result


def hamming_distance(strand1: Strand, strand2: Strand):
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
    file = open(filename, "r")
    strands = []

    buffer_title = ""
    buffer_data = ""
    for line in file:
        line = line.strip()
        if line == "":
            continue

        if line.startswith(">"):
            if buffer_title != "":
                strands.append(Strand(buffer_data, buffer_title))
            buffer_data = ""
            buffer_title = line.strip(">")
        else:
            buffer_data += line

    strands.append(Strand(buffer_data, buffer_title))

    return strands
