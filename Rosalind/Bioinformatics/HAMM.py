from DNA import *

strand1 = Strand("TTCGTTCCTCCCGCAGTAGTCGCCCTAGAGCTAACATAGACTGTTGGGTGATCCGACACCGACGAGGTACGTTGAGCCGGAAGCAGTCTGTCCTAATTCGCTGATGCCCACCTGCGTAACAATTTTTCTTTGAGGTGGCAAGCGGCACACAAGCATTCAAGTAGAACGGCAGGCCTCTAGAGCATATTATTAACCCAACGAAATTGGTGATTTCGCGGAAACAACAGGAGGCCGAAGAGGAAATGTTGGCCGCTACGATACCCGGCAATCTCCTGAAGGATCGTTCCTACCGTTCATTTCTTGTGACAGCAGAGCCAGACTAGTCTAGACAAGTGCCACTGTATAGCTGCGTAGCATTCCCATCATTACCGGTGCGCGCACGTATGACTCTGGACACTAAGGCTCTACAAAACCGGTAGATCACCTAAATGGTAAGGTATTCGCACCAAAAACCCGTGCACCAACCTCCGAAAGACGCATTTGCCCGAGGGAACCCGGCCTGTGGCATCAACTTTAGACGCTCGGCGAGTAACTTATGGTAGTCTAGTCTCTGAACACCACCTCAGCCGAGGATGGTCGGTCTCAGCACAGAGGACAAGCGATGTGAGAAAATTTCATTTTATGAACCGCGCATTCAGCAGGATCGCTCCCCCAAGAGACGAGAAGACATAACGTGGGTCTTCGAAGATACCGGGGCCTACCTTCTGACCGCTTTAGGTAAATAAGAGGTTGTCAACAAACTATCTATACCTTGTGTGTACGCAAACGTGAACATGTAACCCGTTATGCTGCGCAGGATATACTCCGGCTAGAAGTACAACTACCCGTTCATGGGTGAGTAGAGTCCGGATCATGCGAAACGTCCGATTACCCATCTCAAATATGAAGCGCCTTCCTCGACACGGGTCAAAATGTATGTACAAGTGTGACTTGTCACACTTCTGAGAGTGCATAGTTATTCGGTCCGCTCATTATCAACATACTTATACT")
strand2 = Strand("TTGCTGATTACACCTCTTTTGCCCCCTGCTGTACTTACGACAGTAGGGCTTGCAGGACCTATAATGTTAGACCTAGGCAGTACCAGCACATGCTAATATGGGGGGGAACTCGGCAACCCCTATTAAGCTCTGGGAAATCAGCCCGCCCATAAGCTTACGAGTATCTAGACCGCCCTCCTGATCGCAACGTCAAACGGACTAAAAGGGTAAATGCGAGGATACCCCAAGATACGTGCCTGAAACAGGGGGTGTTACAGATGTCCTGGCTGTTAATTAGCCACCTCTCCTATCTTTGTATACTCCGGTCAGTACGACAATTCCCGTTTAGACACGTGGAATGTCGGACCAACGATGCGATGTCATTTTAGAGGTTGGTAACTCGTATTACACTACTTACTAAAACACTACTCCAGTGGTAGTTATGCTAAATCAGTTGTTAGTAGGATCAAGATCGCGTCCAATCACCACCGACAGTTGGTTATACCTGAGGTTGTTCGGCCCCAAGATGTCACTTTATATACGACGAGCGTTGCTTATCTAAACACGGTCACCAAAAAAGAGTTGGTTGAATGATCAGGGATGTAAACTCGGAGTATATCCGATCTAGGATATTTATACTACGTGACCCTCGCCTTCGGAGCTTTTCCTTACACTAGCGCACAACCCACATGACGTGTAGCTAGGAAGTCGCTCGGGCCTATATTCTAGTAGCAAGGGGTACAGAGAAGGTTGTGAAGAGACACCCTTGAACACTTCCGCAGTTGTTCCAGGTCATGGAGGACGAGAGAGGCCTGAAGCGAATCTCAAGCTAGTAGTACCAATAGCCACGGAGGAGTGAGTAGCGCGCGAAACATGCTGAGCGGCCGATCCTATTTCTCAAGACTGGCTAAACTTTCAATATGGGGATTCGAAGCAACGACCGAGCAGGACTACGAGCCCAACCTAGACTGGAAAGTTGAACAGGCGCGGGATTTTTTTCCAAGCGGTACA")

print(hamming_distance(strand1, strand2))