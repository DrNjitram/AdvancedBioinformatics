from DNA import *
from typing import List

strands = [fasta.sequence for fasta in read_fasta_file()]


def get_length(inp: str):
    return len(inp)


def check_substring(inp: List[str], substring: str):
    for strand in inp:
        if substring not in strand:
            return False
    return True


strands.sort(reverse=False, key=get_length)
key_strand = strands.pop(0)


longest_substring = key_strand[0]  # yes i know this is just [0] but bear with me
current_substring = longest_substring

print(key_strand)
print(strands)

for start_index in range(0, len(key_strand)):
    current_length = 1
    current_substring = key_strand[start_index]
    result = True
    while result:
        if result := check_substring(strands, current_substring):
            current_length += 1

            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring

            if current_length + start_index > len(key_strand):
                break

            current_substring = key_strand[start_index: start_index + current_length]

print(f"longest: {longest_substring}")