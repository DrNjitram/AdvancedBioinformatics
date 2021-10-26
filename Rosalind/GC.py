from DNA import Strand
input = open("input.txt", "r")
strands = []

buffer_title = ""
buffer_data = ""
for line in input:
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

lengths = [_.GC_amount() for _ in strands]
max_index = lengths.index(max(lengths))
print(strands[max_index].title)

print(strands[max_index].GC_amount() * 100)

