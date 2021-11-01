from DNA import reverse_translation

with open("input.txt", "r") as file:
    strand = file.readline().strip()
    print(strand)

    options = 1
    for c in strand:
        options = (options * len(reverse_translation[c])) % 1000000

    options = (options * len(reverse_translation["Stop"])) % 1000000
    print(options)
