from DNA import *

strand = Strand("GACCCAGCCTGTGATATGGTGTGATAGCGACCGCCGCCAACATACACGTTGTGATAGTGTGATAAGTGTGATATGTGATAGTCGCCCGTGTGATAGAGTGTGATATGTGATATGTGATATTTGGGATATGTGATATGTGATAACCTGTGATATTGTGATAGATAACTGTGTGATATGTGATATGTGATAGTTGTGATATTGTGATATGTGATATGTGATATTCGTGTGATATGTGATAGACCCAGTGTGATAGGAGTAATGTGATAGATGTGATACATGTGATATTCTGTGATAGTTTGTGATATGGGTGTGATACCATGTGATAAGATCCTGTGATAGTACTGTGATAATTACATGTGATAACTGGACCATATGTGATAGTGTGATATGTGATATGTGATAACTTGTGATATGTGATATGTGATATCTGTGATAGTGTGATAATGAGAGTGTGTGATACCAAGTGTGATAATTGTGATATGTGATATCTTGTGATAGATATGTGATAAAGCTTTGTGATAGTGGTTGTGATACGTTGTGATATGTGATAAGCTGTGATAGTGCTGTGATACCTGTGATATGTGATAGCTGTGATATGTGATAAATGTGATATGTGATACATATGTGATATGTGTGATACGGTCCTGTGATATCTGCGATGTGATAAGTTGTGATATGTGATAATGTGATACGAATTGTGATATATCGAATGTGATATGTGATATCAATAAGGTATGTGATAGTATAATTCCGACGTGCTTGTGATATGTGATAAGTTTTGTGATAACCATGTGATAGGTATGTGATACTTGAGGTGTGATATGTGTGATATTGTGATACACAGCTTGTGATATGTGATATTGTATGGATTCTAAATGTGATACTGTGATAGTGTGATA")

print(" ".join([str(_) for _ in strand.subs("TGTGATATG")]))